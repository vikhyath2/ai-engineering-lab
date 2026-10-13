
import os
import time
from openai import OpenAI

# 1. Create the API client
client = OpenAI()

# 2. Choose a model
model_name = os.getenv("OPENAI_MODEL", "gpt-5-mini")

# 3. Define the user's question
prompt = "Explain what a data pipeline is in 3 sentences."

# 4. Start measuring response time
start_time = time.perf_counter()

# 5. Send a request to the OpenAI API
response = client.responses.create(
    model=model_name,
    input=prompt,
    max_output_tokens=1000,
    reasoning={"effort": "low"}
)

# 6. Calculate request latency
latency = time.perf_counter() - start_time

# 7. Display the model's answer
print("\nAI Response:")
print(response.output_text)

# 8. Display response metadata
print("\nResponse Details:")
print("Model:", response.model)
print("Status:", response.status)
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("Total tokens:", response.usage.total_tokens)
print(f"Latency: {latency:.2f} seconds")
