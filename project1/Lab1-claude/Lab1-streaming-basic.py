import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = anthropic.Anthropic()

# 스트리밍 컨텍스트 매니저 사용
with client.messages.stream(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "한국 역사를 요약해줘"}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

# 스트림 완료 후 전체 메시지 접근
final_message = stream.get_final_message()
print(f"\n총 토큰: {final_message.usage.output_tokens}")