import os
from pathlib import Path
from dotenv import load_dotenv

import anthropic

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# 클라이언트 초기화 (ANTHROPIC_API_KEY 환경변수 자동 사용)
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