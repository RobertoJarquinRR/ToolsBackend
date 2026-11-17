import os
from openai import OpenAI

apikey = os.getenv("API_KEY_GROQ_IA")
if not apikey:
    raise SystemExit("Define API_KEY_GROQ_IA en tu entorno o en tu archivo .env")

client = OpenAI(
    api_key=apikey,
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Explain the importance of fast language models",
    model="openai/gpt-oss-20b",
)
print(response.output_text)
