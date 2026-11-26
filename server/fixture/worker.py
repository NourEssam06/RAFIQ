import json
import logging
import signal
import subprocess
import sys
import time
from pathlib import Path
from random import uniform
from threading import Event
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from fixture.database import engine_for, schema_ready

HEARTBEAT = Path("/tmp/rafiq-fixture-worker.heartbeat")
R_SCRIPT = Path(__file__).resolve().parents[1] / "r" / "synthetic_mean.R"
LEASE_SECONDS = 30
R_TIMEOUT_SECONDS = 10
HEARTBEAT_MAX_AGE_SECONDS = 20
IDLE_POLL_SECONDS = 0.5
MAX_DB_BACKOFF_SECONDS = 4
CLAIM = text("""
    WITH candidate AS (
        SELECT id FROM rafiq_fixture.fixtures
        WHERE status IN ('queued', 'running')
            AND (status = 'queued' OR lease_until <= clock_timestamp())
        ORDER BY id LIMIT 1 FOR UPDATE SKIP LOCKED
    )
    UPDATE rafiq_fixture.fixtures AS fixture
    SET status = 'running', generation = generation + 1,
        lease_until = clock_timestamp() + :lease_seconds * interval '1 second'
    FROM candidate WHERE fixture.id = candidate.id
    RETURNING fixture.id, fixture.generation, fixture.samples
""")
PUBLISH = text("""
    UPDATE rafiq_fixture.fixtures
    SET status = :status, result = CAST(:result AS jsonb), lease_until = NULL
    WHERE id = :id AND generation = :generation AND status = 'running'
        AND lease_until > clock_timestamp()
""")


class MeanResult(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)

    version: Literal[1]
    method: Literal["synthetic-mean-v1"]
    count: int = Field(gt=0)
    mean: float


def calculate(samples: list[int]) -> MeanResult:
    process = subprocess.run(
        ["Rscript", "--vanilla", str(R_SCRIPT)],
        input=json.dumps({"version": 1, "method": "synthetic-mean-v1", "samples": samples}),
        text=True,
        capture_output=True,
        timeout=R_TIMEOUT_SECONDS,
        check=True,
    )
    result = MeanResult.model_validate_json(process.stdout)
    if samples != [2, 4, 6] or result.count != 3 or abs(result.mean - 4) > 0.000001:
        raise ValueError("R result is incompatible with the fixture input")
    return result


def claim_loop(engine, stopping: Event):
    backoff = 0
    while not stopping.is_set():
        try:
            with engine.begin() as connection:
                if not schema_ready(connection, "worker"):
                    raise FixtureSchemaUnavailable
                if stopping.is_set():
                    return
                job = connection.execute(CLAIM, {"lease_seconds": LEASE_SECONDS}).mappings().first()
            if backoff:
                logging.info("Synthetic worker claim loop recovered")
                backoff = 0
            HEARTBEAT.touch()
            if job is None:
                stopping.wait(IDLE_POLL_SECONDS)
                continue

            try:
                result = calculate(job.samples).model_dump_json()
            except (subprocess.SubprocessError, ValueError):
                logging.warning("Synthetic R calculation failed validation or execution")
                result = None

            with engine.begin() as connection:
                connection.execute(
                    PUBLISH,
                    {
                        "id": job.id,
                        "generation": job.generation,
                        "status": "completed" if result is not None else "failed",
                        "result": result,
                    },
                )
        except (SQLAlchemyError, FixtureSchemaUnavailable):
            HEARTBEAT.unlink(missing_ok=True)
            if not backoff:
                logging.warning("Synthetic worker database or schema unavailable")
            backoff = min(MAX_DB_BACKOFF_SECONDS, max(1, backoff * 2))
            stopping.wait(uniform(backoff / 2, backoff))


class FixtureSchemaUnavailable(Exception):
    pass


def run_worker():
    stopping = Event()
    signal.signal(signal.SIGTERM, lambda *_: stopping.set())
    signal.signal(signal.SIGINT, lambda *_: stopping.set())
    HEARTBEAT.unlink(missing_ok=True)
    engine = engine_for("worker")
    logging.basicConfig(level=logging.INFO)
    try:
        subprocess.run(
            [
                "Rscript", "--vanilla", "-e",
                'stopifnot(getRversion() == "4.6.2", packageVersion("jsonlite") == "2.0.0")',
            ],
            check=True,
            timeout=R_TIMEOUT_SECONDS,
        )
        claim_loop(engine, stopping)
    finally:
        HEARTBEAT.unlink(missing_ok=True)
        engine.dispose()


def heartbeat_is_fresh() -> bool:
    try:
        age = time.time() - HEARTBEAT.stat().st_mtime
    except FileNotFoundError:
        return False
    return 0 <= age < HEARTBEAT_MAX_AGE_SECONDS


if __name__ == "__main__":
    if sys.argv[1:] == ["--check-health"]:
        sys.exit(0 if heartbeat_is_fresh() else 1)
    run_worker()
