import json
import logging
import subprocess
import sys
import time
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from fixture.database import engine_for, schema_ready

HEARTBEAT = Path("/tmp/rafiq-fixture-worker.heartbeat")
METHOD = Path(__file__).resolve().parents[1] / "r" / "synthetic_mean.R"
LEASE_SECONDS = 30
R_TIMEOUT_SECONDS = 10
CLAIM = text("""
    WITH candidate AS (
        SELECT id FROM rafiq_fixture.fixtures
        WHERE status = 'queued' OR (status = 'running' AND lease_until <= clock_timestamp())
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
        ["Rscript", "--vanilla", str(METHOD)],
        input=json.dumps({"version": 1, "method": "synthetic-mean-v1", "samples": samples}),
        text=True,
        capture_output=True,
        timeout=R_TIMEOUT_SECONDS,
        check=True,
    )
    result = MeanResult.model_validate_json(process.stdout)
    if result.count != len(samples) or not min(samples) <= result.mean <= max(samples):
        raise ValueError("R result is incompatible with the fixture input")
    return result


def run_worker():
    HEARTBEAT.unlink(missing_ok=True)
    engine = engine_for("worker")
    subprocess.run(
        [
            "Rscript", "--vanilla", "-e",
            'stopifnot(getRversion() == "4.6.2", packageVersion("jsonlite") == "2.0.0")',
        ],
        check=True,
        timeout=R_TIMEOUT_SECONDS,
    )
    while True:
        try:
            with engine.begin() as connection:
                if not schema_ready(connection, "worker"):
                    raise RuntimeError("Worker requires the fixture schema and role")
                job = connection.execute(CLAIM, {"lease_seconds": LEASE_SECONDS}).mappings().first()
            HEARTBEAT.touch()
            if job is None:
                time.sleep(0.5)
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
            HEARTBEAT.touch()
        except SQLAlchemyError:
            HEARTBEAT.unlink(missing_ok=True)
            logging.warning("Synthetic worker database operation unavailable")
            time.sleep(1)


if __name__ == "__main__":
    if sys.argv[1:] == ["--check-health"]:
        sys.exit(0 if HEARTBEAT.exists() and time.time() - HEARTBEAT.stat().st_mtime < 20 else 1)
    run_worker()
