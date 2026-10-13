# AI Engineering Lab

A hands-on learning repository focused on building, testing, and understanding applications powered by large language models (LLMs).

The project explores practical AI engineering concepts through Python exercises, API integrations, structured data extraction, model evaluation, and token usage analysis.

## Current Work — Phase 0: LLM Foundations

### 1. Structured Extraction from Spark Logs

Built Python exercises that use an LLM to extract useful diagnostic information from Apache Spark error logs.

The exercises focus on:

- Identifying error classes, stage IDs, table names, and likely causes.
- Using Pydantic to define and validate structured output.
- Comparing extracted information with expected results.
- Understanding the difference between a correctly formatted response and a factually correct response.

### 2. Token Economics and Model Comparison

Explored the behavior of OpenAI models using practical prompts related to data engineering.

Measured:

- Input and output token usage.
- API response latency.
- Estimated request costs.
- Differences in responses across model configurations.

The purpose is to understand model selection beyond response quality alone.

### 3. Structured Extraction Evaluation

Developed an evaluation exercise using 50 Spark log test cases.

The evaluation focuses on checking whether AI-generated outputs match expected fields and identifying extraction errors.

## Technologies

- Python
- OpenAI API
- Pydantic
- DuckDB
- JSON
- SQL
- Git and GitHub

## Repository Structure

```text
AI-Engineering/
├── Phase-0/
│   ├── phase0_extraction.py
│   ├── first_llm_call.py
│   ├── spark_log_extractor.py
│   ├── spark_log_batch.py
│   ├── evaluate_extraction.py
│   ├── evaluate_50_logs.py
│   ├── spark_test_cases_50.json
│   ├── token_economics.py
│   └── test_openai.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/vikhyath2/ai-engineering-lab.git
cd ai-engineering-lab
```

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Set your OpenAI API key for exercises requiring API access:

```bash
export OPENAI_API_KEY="your-api-key"
```

Never commit API keys or sensitive logs.

## Running Automated Tests

Phase 0 includes six automated regression tests built
with Python's unittest framework.

Run all tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

Current tests cover:

- Validation of the 50-case dataset size
- Verification of unique test-case IDs
- Pydantic validation of valid Spark errors
- Nullable stage ID handling
- Rejection of invalid exception-name formats
- Rejection of missing required fields

Latest local result: 6 tests passed.

These tests do not require OpenAI API calls.

## Running the 50-Log Evaluation

Validate the dataset without API calls:

```bash
python Phase-0/evaluate_50_logs.py
```

Evaluate five cases using the OpenAI API:

```bash
python Phase-0/evaluate_50_logs.py --run --limit 5
```

Evaluate all 50 cases:

```bash
python Phase-0/evaluate_50_logs.py --run --limit 50
```

The last two commands make billable API requests.

Dataset validation has passed for 50 unique labeled cases.
Full model evaluation results have not yet been verified.

## Learning Roadmap

- Phase 0 — LLM Foundations and Evaluations
- Phase 1 — API Integration and Agent Loops
- Phase 2 — Context Engineering and RAG
- Phase 3 — Tools, MCP, and Subagents
- Phase 4 — LangChain and LangGraph
- Phase 5 — Evaluations and Observability
- Phase 6 — Enterprise AI Architecture
- Phase 7 — Pipeline Incident Copilot

## Key Lessons

- Structured responses make AI outputs easier to integrate with applications.
- Pydantic validates data structure but does not guarantee factual accuracy.
- Token usage, latency, and cost vary across model configurations.
- Evaluation datasets help identify extraction failures.
- Automated regression tests help detect unexpected changes.
- Reliable AI applications require more than successful API responses.

## Project Status

Phase 0 implementation and initial automated tests completed.

Current verification:
- 50 unique labeled Spark log cases validated.
- 6 automated regression tests passed.
- Dataset validation runs without API charges.

Full model accuracy benchmarking and additional reliability
testing remain future improvements.

Engineering observations are documented in
[Phase 0 Notes](Phase-0/NOTES.md).
