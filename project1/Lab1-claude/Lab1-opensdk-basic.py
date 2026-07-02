import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = anthropic.Anthropic()

# 기본 메시지 호출
message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Python의 장점을 3가지 설명해줘"}
    ]
)

# 응답 텍스트 출력
print(message.content[0].text)
print(f"입력 토큰: {message.usage.input_tokens}, 출력 토큰: {message.usage.output_tokens}")