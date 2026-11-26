from alembic import context
from sqlalchemy import text

from fixture.database import engine_for

if context.is_offline_mode():
    raise RuntimeError("Use the dedicated local migration connection")

with engine_for("migrate").connect() as connection:
    context.configure(connection=connection, version_table_schema="rafiq_fixture")
    with context.begin_transaction():
        if connection.execute(text("SELECT current_user")).scalar_one() != "rafiq_migrate":
            raise RuntimeError("Migration requires the dedicated fixture migration role")
        connection.execute(text("SELECT pg_advisory_xact_lock(8427150001)"))
        context.run_migrations()
