import os
from pathlib import Path
from dotenv import load_dotenv

from openai import OpenAI

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

client = OpenAI(
)
MODEL = "gpt-5.4-mini"

messages = [
    {
        "role": "system",
        "content": "당신은 친절한 개발 강사입니다."
    }
]

def chat(user_input: str):
    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    assistant_message = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message

print(chat("Docker Compose가 무엇인가요?"))
print(chat("방금 설명을 초보자용 예제로 다시 설명해주세요."))