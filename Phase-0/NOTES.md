# Phase 0 — Engineering Notes

## Objective

Understand how to work with LLM APIs, extract structured information, measure model usage, and evaluate the reliability of AI-generated responses.

## 1. Structured Extraction

Built Python exercises to extract diagnostic details from Spark error logs using the OpenAI API and Pydantic.

Key concepts:

- Using an LLM to interpret unstructured logs.
- Defining structured output fields with Pydantic.
- Separating schema validation from factual correctness.
- Comparing extracted information against expected results.

**Lesson learned:** A response can follow the required JSON schema while still containing incorrect information.

## 2. Token Economics

Experimented with different OpenAI model configurations to understand:

- Input and output tokens.
- Response latency.
- Estimated API costs.
- Differences in model behavior across prompts.

**Lesson learned:** Model selection should consider accuracy, latency, and cost together rather than assuming the largest model is always necessary.

## 3. Evaluation Framework

Created a labeled dataset containing 50 Spark log examples.

The evaluation script supports checking extraction results against expected fields and measuring performance.

**Verified result:**

- Dataset validation: 50 unique labeled cases.
- Dataset successfully loaded from the repository root.
- Validation completed without API calls.

**Not yet verified in this document:**

- Full 50-case LLM evaluation accuracy.
- Field-level accuracy across all cases.
- Total token usage and API cost for the full evaluation.

## 4. Problems Encountered

### Dataset file-path issue

The evaluation script originally used a relative path to load the JSON dataset. This could fail when running the script from another directory.

Updated the path handling to use the Python script's own location.

**Result:** The dataset successfully validates when executed from the repository root.

## 5. Next Improvements

- Record actual model comparison measurements.
- Run and analyze a controlled LLM evaluation.
- Add automated regression tests.
- Improve error handling where necessary.
- Continue to Phase 1 after completing the remaining verification.

## 6. Key Takeaways

1. API integration is only the starting point of an AI application.
2. Pydantic helps enforce structured output, but does not guarantee correct facts.
3. Evaluations help identify where model outputs differ from expected results.
4. Token usage and latency should be measured.
5. Reproducible tests and clear documentation make AI projects easier to maintain.
