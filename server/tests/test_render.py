import json
import unittest

from fixture.render import RenderSnapshot


COMPLETED_FIXTURE = {
    "id": "a81afdf7-3edb-4245-89b9-2bb58376bdf8",
    "status": "completed",
    "result": {"version": 1, "method": "synthetic-mean-v1", "count": 3, "mean": 4},
}


class RenderSnapshotTests(unittest.TestCase):
    def test_completed_result_supplies_labels_values_and_units(self):
        snapshot = RenderSnapshot.from_fixture(json.dumps(COMPLETED_FIXTURE))

        self.assertEqual(snapshot.rows, (
            ("Samples", "2, 4, 6 (unitless)"),
            ("Sample count", "3 samples"),
            ("Mean", "4 (unitless)"),
            ("Method", "synthetic-mean-v1"),
            ("Result version", "1"),
        ))

    def test_incompatible_fixture_data_cannot_supply_a_snapshot(self):
        result = COMPLETED_FIXTURE["result"]
        for changes in (
            {"status": "queued", "result": None},
            {"status": "failed", "result": None},
            {"result": {**result, "version": 2}},
            {"result": {**result, "version": True}},
            {"result": {**result, "method": "unknown"}},
            {"result": {**result, "count": 4}},
            {"result": {**result, "mean": 5}},
            {"result": {**result, "mean": float("nan")}},
            {"result": {**result, "label": "unexpected content"}},
        ):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                RenderSnapshot.from_fixture(json.dumps({**COMPLETED_FIXTURE, **changes}))
