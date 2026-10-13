
import time
from openai import OpenAI

client = OpenAI()

# Start timer BEFORE the API request
start_time = time.perf_counter()

response = client.responses.create(
    model="gpt-5-mini",
    input="Explain what a data pipeline is in 3 sentences.",
    max_output_tokens=1000,
    reasoning={"effort": "low"}
)

# Stop timer AFTER the API response
latency = time.perf_counter() - start_time

print(f"\nResponse time: {latency:.2f} seconds")

print("\nAI Response:")
print(response.output_text)

print("\nToken Usage:")
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("Total tokens:", response.usage.total_tokens)

print("\nResponse Details:")
print("Response status:", response.status)
print("Incomplete details:", response.incomplete_details)
print(
    "Reasoning tokens:",
    response.usage.output_tokens_details.reasoning_tokens
)
