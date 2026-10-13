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

Create and activate a Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Set your OpenAI API key locally:

```bash
export OPENAI_API_KEY="your-api-key"
```

Run an example evaluation:

```bash
python Phase-0/evaluate_50_logs.py
```

**Note:** API usage may incur charges. Use synthetic test logs and never commit API keys or sensitive information.

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
- Pydantic validates data structure, but factual accuracy requires separate testing.
- Token usage, latency, and cost can vary significantly across model configurations.
- Evaluation datasets help identify recurring extraction failures.
- Reliable AI applications require more than a successful API response.

## Project Status

In progress — Phase 0 exercises are being documented and verified before moving to Phase 1.