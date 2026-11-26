from alembic import op

revision = "0001_local_fixture"
down_revision = None


def upgrade():
    op.execute("""
        CREATE TABLE rafiq_fixture.fixtures (
            id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
            owner_id text NOT NULL UNIQUE CHECK (owner_id IN ('driver-a', 'driver-b')),
            samples integer[] NOT NULL DEFAULT ARRAY[2, 4, 6]
                CHECK (samples = ARRAY[2, 4, 6]),
            status text NOT NULL DEFAULT 'queued',
            generation bigint NOT NULL DEFAULT 0 CHECK (generation >= 0),
            lease_until timestamptz,
            result jsonb,
            CHECK (
                (status = 'queued' AND generation = 0 AND lease_until IS NULL AND result IS NULL)
                OR (status = 'running' AND generation > 0 AND lease_until IS NOT NULL AND result IS NULL)
                OR (status = 'failed' AND generation > 0 AND lease_until IS NULL AND result IS NULL)
                OR (status = 'completed' AND generation > 0 AND lease_until IS NULL
                    AND result IS NOT NULL AND jsonb_typeof(result) = 'object')
            )
        )
    """)
    op.execute("ALTER TABLE rafiq_fixture.fixtures ENABLE ROW LEVEL SECURITY")
    op.execute("ALTER TABLE rafiq_fixture.fixtures FORCE ROW LEVEL SECURITY")
    op.execute("""
        CREATE POLICY api_read ON rafiq_fixture.fixtures FOR SELECT TO rafiq_api
        USING (owner_id = current_setting('rafiq.fixture_owner', true))
    """)
    op.execute("""
        CREATE POLICY api_create ON rafiq_fixture.fixtures FOR INSERT TO rafiq_api
        WITH CHECK (owner_id = current_setting('rafiq.fixture_owner', true))
    """)
    op.execute("""
        CREATE POLICY worker_read ON rafiq_fixture.fixtures FOR SELECT TO rafiq_worker
        USING (status IN ('queued', 'running', 'completed', 'failed'))
    """)
    op.execute("""
        CREATE POLICY worker_update ON rafiq_fixture.fixtures FOR UPDATE TO rafiq_worker
        USING (status IN ('queued', 'running'))
        WITH CHECK (status IN ('running', 'completed', 'failed'))
    """)
    op.execute("""
        GRANT SELECT (id, owner_id, status, result), INSERT (owner_id)
            ON rafiq_fixture.fixtures TO rafiq_api;
        GRANT SELECT (id, samples, status, generation, lease_until),
            UPDATE (status, generation, lease_until, result)
            ON rafiq_fixture.fixtures TO rafiq_worker;
        GRANT SELECT ON rafiq_fixture.alembic_version TO rafiq_api, rafiq_worker
    """)


def downgrade():
    op.execute("REVOKE SELECT ON rafiq_fixture.alembic_version FROM rafiq_api, rafiq_worker")
    op.drop_table("fixtures", schema="rafiq_fixture")
