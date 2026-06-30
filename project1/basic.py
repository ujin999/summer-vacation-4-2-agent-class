import os
from pathlib import Path
from dotenv import load_dotenv

from openai import OpenAI

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

client = OpenAI(
)

response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {
            "role": "system",
            "content": "당신은 친절한 AI 비서입니다."
        },
        {
            "role": "user",
            "content": "Oracle Database 26ai의 주요 특징을 설명해주세요."
        }
    ]
)

print(response.choices[0].message.content)