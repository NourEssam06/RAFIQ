import unittest

from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError

from fixture.database import engine_for, schema_ready
from fixture.worker import CLAIM, PUBLISH, calculate

FIXTURES = "rafiq_fixture.fixtures"


class FixtureIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = engine_for("api")
        cls.worker = engine_for("worker")

    @classmethod
    def tearDownClass(cls):
        cls.api.dispose()
        cls.worker.dispose()

    def test_runtime_roles_have_scoped_grants_and_row_policies(self):
        with self.api.connect() as connection:
            self.assertTrue(schema_ready(connection, "api"))
            self.assertEqual(connection.execute(
                text(f"SELECT count(id) FROM {FIXTURES}")
            ).scalar_one(), 0)
            connection.execute(text("SELECT set_config('rafiq.fixture_owner', 'driver-a', true)"))
            self.assertEqual(connection.execute(
                text(f"SELECT owner_id FROM {FIXTURES}")
            ).scalars().all(), ["driver-a"])
            with self.assertRaises(ProgrammingError) as denied:
                connection.execute(text(f"INSERT INTO {FIXTURES} (owner_id) VALUES ('driver-b')"))
            self.assertEqual(denied.exception.orig.sqlstate, "42501")
            self.assertIn("row-level security policy", str(denied.exception.orig))

        with self.api.connect() as connection:
            self.assertEqual(connection.execute(
                text(f"SELECT count(id) FROM {FIXTURES}")
            ).scalar_one(), 0)
            with self.assertRaises(ProgrammingError) as denied:
                connection.execute(text(f"UPDATE {FIXTURES} SET result = NULL"))
            self.assertIn("permission denied", str(denied.exception.orig))

        with self.worker.connect() as connection:
            self.assertTrue(schema_ready(connection, "worker"))
            with self.assertRaises(ProgrammingError) as denied:
                connection.execute(text(f"SELECT owner_id FROM {FIXTURES}"))
            self.assertIn("permission denied", str(denied.exception.orig))

    def test_reclaimed_generation_is_the_only_one_that_can_publish(self):
        with self.api.begin() as connection:
            connection.execute(text("SELECT set_config('rafiq.fixture_owner', 'driver-b', true)"))
            connection.execute(text(f"INSERT INTO {FIXTURES} (owner_id) VALUES ('driver-b')"))
            fixture_id = connection.execute(text(f"SELECT id FROM {FIXTURES}")).scalar_one()

        with self.worker.begin() as connection:
            first = connection.execute(CLAIM, {"lease_seconds": 0}).mappings().one()
            self.assertEqual(first.id, fixture_id)

        result = calculate(first.samples)
        self.assertEqual(result.model_dump(), {
            "version": 1, "method": "synthetic-mean-v1", "count": 3, "mean": 4,
        })
        publication = {"id": fixture_id, "status": "completed", "result": result.model_dump_json()}
        with self.worker.begin() as connection:
            self.assertEqual(connection.execute(
                PUBLISH, {**publication, "generation": first.generation}
            ).rowcount, 0)

        with self.worker.begin() as connection:
            second = connection.execute(CLAIM, {"lease_seconds": 30}).mappings().one()
            self.assertEqual(second.id, fixture_id)
            self.assertEqual(second.generation, first.generation + 1)

            with self.worker.begin() as competing_worker:
                self.assertIsNone(competing_worker.execute(
                    CLAIM, {"lease_seconds": 30}
                ).mappings().one_or_none())

        with self.worker.begin() as connection:
            self.assertEqual(connection.execute(
                PUBLISH, {**publication, "generation": first.generation}
            ).rowcount, 0)
            self.assertEqual(connection.execute(
                PUBLISH, {**publication, "generation": second.generation}
            ).rowcount, 1)

        with self.worker.begin() as connection:
            self.assertEqual(connection.execute(
                PUBLISH, {**publication, "generation": second.generation}
            ).rowcount, 0)

        with self.api.begin() as connection:
            connection.execute(text("SELECT set_config('rafiq.fixture_owner', 'driver-b', true)"))
            self.assertEqual(connection.execute(
                text(f"SELECT result FROM {FIXTURES}")
            ).scalar_one(), result.model_dump())
