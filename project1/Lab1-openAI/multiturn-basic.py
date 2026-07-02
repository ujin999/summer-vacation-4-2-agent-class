from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
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

# chat 한 번당 1개의 user input과 1개의 assistant output이 messages에 추가됩니다.
print(chat("Docker Compose가 무엇인가요?"))
print(chat("방금 설명을 초보자용 예제로 다시 설명해주세요."))