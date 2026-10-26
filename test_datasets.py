"""Automated integrity tests for the PulmoVision example datasets."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_datasets import load_pair  # noqa: E402


class DatasetValidationTests(unittest.TestCase):
    def test_trial_pair_has_at_least_1000_matching_rows(self):
        self.assertGreaterEqual(len(load_pair("trial")), 1000)

    def test_test_pair_has_at_least_1000_matching_rows(self):
        self.assertGreaterEqual(len(load_pair("test")), 1000)

    def test_trial_and_test_ids_are_disjoint(self):
        trial = {row["id"] for row in load_pair("trial")}
        test = {row["id"] for row in load_pair("test")}
        self.assertTrue(trial.isdisjoint(test))

    def test_schema_fields_are_importer_compatible(self):
        expected = {"id", "lobe", "diameter_mm", "hu", "spiculation", "fev1_percent"}
        for split in ("trial", "test"):
            rows = load_pair(split)
            self.assertTrue(rows)
            self.assertEqual(set(rows[0]), expected)


if __name__ == "__main__":
    unittest.main()
