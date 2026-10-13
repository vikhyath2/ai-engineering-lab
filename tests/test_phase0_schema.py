
import importlib.util
import unittest
from pathlib import Path

from pydantic import ValidationError


ROOT = Path(__file__).resolve().parent.parent

SCRIPT_PATH = ROOT / "Phase-0" / "evaluate_50_logs.py"

spec = importlib.util.spec_from_file_location(
    "phase0_evaluation",
    SCRIPT_PATH,
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

SparkError = module.SparkError


class TestSparkErrorSchema(unittest.TestCase):

    def test_valid_spark_error(self):
        result = SparkError(
            error_class="AnalysisException",
            stage_id=14,
            table="orders_daily",
            likely_cause="Column cannot be resolved",
        )

        self.assertEqual(result.error_class, "AnalysisException")
        self.assertEqual(result.stage_id, 14)

    def test_missing_stage_is_none(self):
        result = SparkError(
            error_class="AnalysisException",
            stage_id=None,
            table="orders_daily",
            likely_cause="Column cannot be resolved",
        )

        self.assertIsNone(result.stage_id)

    def test_invalid_exception_format(self):
        with self.assertRaises(ValidationError):
            SparkError(
                error_class="java.lang.OutOfMemoryError",
                stage_id=27,
                table="sales_transactions",
                likely_cause="Java heap space exhausted",
            )

    def test_missing_required_field(self):
        with self.assertRaises(ValidationError):
            SparkError(
                error_class="AnalysisException",
                stage_id=14,
                table="orders_daily",
            )


if __name__ == "__main__":
    unittest.main()
