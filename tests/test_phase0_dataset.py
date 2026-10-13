
import json
import unittest
from pathlib import Path


DATASET_PATH = (
    Path(__file__).resolve().parent.parent
    / "Phase-0"
    / "spark_test_cases_50.json"
)


class TestPhase0Dataset(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads(
            DATASET_PATH.read_text(encoding="utf-8")
        )

    def test_dataset_contains_50_cases(self):
        self.assertEqual(len(self.cases), 50)

    def test_case_ids_are_unique(self):
        ids = [case["id"] for case in self.cases]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
