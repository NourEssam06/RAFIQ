import os

from sqlalchemy import create_engine, text

SCHEMA_REVISION = "0002_fixture_claim_index"


def engine_for(role: str):
    if os.environ.get("RAFIQ_MODE") != "local-fixture":
        raise RuntimeError("The synthetic fixture requires RAFIQ_MODE=local-fixture")
    return create_engine(
        os.environ[f"RAFIQ_{role.upper()}_DATABASE_URL"],
        connect_args={
            "connect_timeout": 3,
            "options": "-c statement_timeout=5000",
            "keepalives_idle": 2,
            "keepalives_interval": 1,
            "keepalives_count": 3,
            "tcp_user_timeout": 5000,
        },
        hide_parameters=True,
        pool_pre_ping=True,
        pool_timeout=3,
    )


def schema_ready(connection, role: str) -> bool:
    return connection.execute(
        text("""
            SELECT current_user = :role AND version_num = :revision
            FROM rafiq_fixture.alembic_version
        """),
        {"role": f"rafiq_{role}", "revision": SCHEMA_REVISION},
    ).scalar_one_or_none() is True
