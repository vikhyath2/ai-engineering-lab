import csv
import time
import uuid
from datetime import datetime, timezone

import duckdb
from openai import OpenAI, APIError

# 1. Connect to OpenAI
client = OpenAI(max_retries=0, timeout=90.0)

# 2. Model pricing: USD per 1 million tokens
models = {
    "gpt-5-nano": {"input": 0.05, "output": 0.40},
    "gpt-5-mini": {"input": 0.25, "output": 2.00},
    "gpt-5": {"input": 1.25, "output": 10.00},
}

# 3. Three prompts for every model
prompts = [
    "Explain what a data pipeline is in 3 sentences.",
    "Write a SQL query to find duplicate customer IDs.",
    "Explain 3 common causes of Spark OOM errors and "
    "give one practical fix for each. "
    "Keep your answer under 150 words."
]

# 4. Set up database
db = duckdb.connect("phase0_results.duckdb")

db.execute("""
CREATE TABLE IF NOT EXISTS token_experiments (
    run_id VARCHAR,
    created_at TIMESTAMP,
    model VARCHAR,
    prompt VARCHAR,
    input_tokens INTEGER,
    output_tokens INTEGER,
    reasoning_tokens INTEGER,
    latency_seconds DOUBLE,
    estimated_cost DOUBLE,
    status VARCHAR,
    response_text VARCHAR
)
""")

run_id = str(uuid.uuid4())
print("Experiment started:", run_id)

# 5. Send prompts to all three models
for model, prices in models.items():

    print(f"\n===== Testing {model} =====")

    for prompt in prompts:
        print("\nPrompt:", prompt)

        try:
            # Start measuring time
            start_time = time.perf_counter()

            response = client.responses.create(
                model=model,
                input=prompt,
                max_output_tokens=1000,
                reasoning={"effort": "low"},
            )

            # Measure elapsed time
            latency = time.perf_counter() - start_time

            # Collect token information
            usage = response.usage
            input_tokens = usage.input_tokens
            output_tokens = usage.output_tokens

            details = usage.output_tokens_details
            reasoning_tokens = (
                details.reasoning_tokens
                if details and details.reasoning_tokens
                else 0
            )

            # Cost in US dollars
            cost = (
                input_tokens * prices["input"]
                + output_tokens * prices["output"]
            ) / 1_000_000

            # Get generated answer
            answer = response.output_text

            # Save to DuckDB
            db.execute(
                """
                INSERT INTO token_experiments
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    run_id,
                    datetime.now(timezone.utc),
                    model,
                    prompt,
                    input_tokens,
                    output_tokens,
                    reasoning_tokens,
                    latency,
                    cost,
                    response.status,
                    answer,
                ],
            )

            print("Status:", response.status)
            print("Input tokens:", input_tokens)
            print("Output tokens:", output_tokens)
            print("Reasoning tokens:", reasoning_tokens)
            print(f"Latency: {latency:.2f} seconds")
            print(f"Estimated cost: ${cost:.8f}")
            print("Answer:", answer[:400])

        except APIError as error:
            print(f"API error for {model}: {error}")
            print("Skipping this request.")

# 6. Summarize results from this run
print("\n===== FINAL COMPARISON =====")

summary = db.execute(
    """
    SELECT
        model,
        COUNT(*) AS requests,
        SUM(input_tokens) AS input_tokens,
        SUM(output_tokens) AS output_tokens,
        ROUND(AVG(latency_seconds), 2) AS avg_latency,
        ROUND(SUM(estimated_cost), 8) AS total_cost
    FROM token_experiments
    WHERE run_id = ?
    GROUP BY model
    ORDER BY model
    """,
    [run_id],
).fetchall()

for row in summary:
    print(row)

# 7. Export this run for review
rows = db.execute(
    """
    SELECT * FROM token_experiments
    WHERE run_id = ?
    """,
    [run_id],
)

headers = [column[0] for column in rows.description]

with open("phase0_latest_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows.fetchall())
