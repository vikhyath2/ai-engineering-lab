
from pydantic import BaseModel, ValidationError
import re


class SparkError(BaseModel):
    error_class: str
    stage_id: int
    table: str
    likely_cause: str


log = (
    "AnalysisException: Column 'customer_id' cannot "
    "be resolved in stage 14 for orders_daily"
)

# Start with a predictable, rule-based parser.
# We will replace this extraction step with an LLM later.
pattern = (
    r"(?P<error_class>\w+):.*"
    r"stage (?P<stage_id>\d+) for "
    r"(?P<table>\w+)"
)

match = re.search(pattern, log)

if match:
    try:
        result = SparkError(
            **match.groupdict(),
            likely_cause="Missing or unresolved column"
        )
        print(result.model_dump_json(indent=2))
    except ValidationError as exc:
        print("Validation failed:", exc)
else:
    print("Log did not match the expected pattern")
