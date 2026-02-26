from openai import OpenAI
import os

apikey = "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"

client = OpenAI(
    api_key=( apikey), # type: ignore
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Explain the importance of fast language models",
    model="openai/gpt-oss-20b",
)
print(response.output_text)
