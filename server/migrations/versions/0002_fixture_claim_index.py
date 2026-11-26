from alembic import op

revision = "0002_fixture_claim_index"
down_revision = "0001_local_fixture"


def upgrade():
    op.execute("""
        CREATE INDEX fixtures_claimable_id ON rafiq_fixture.fixtures (id)
        WHERE status IN ('queued', 'running')
    """)


def downgrade():
    op.drop_index("fixtures_claimable_id", table_name="fixtures", schema="rafiq_fixture")
