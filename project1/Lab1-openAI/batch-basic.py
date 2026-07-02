from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

MODEL = "gpt-5.4-mini"

items = [
    "Oracle 26ai",
    "Langfuse",
    "n8n",
    "Paperclip",
    "Hermes Agent"
]

for item in items:
    response = client.responses.create(
        model=MODEL,
        input=f"{item}를 3줄로 요약해줘."
    )

    print(f"\n## {item}")
    print(response.output_text)