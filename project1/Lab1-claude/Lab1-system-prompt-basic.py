import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = anthropic.Anthropic()

# 전문 도우미 페르소나 설정
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    system="""당신은 Paperclip AI의 친절한 AI 어시스턴트입니다.
- 항상 한국어로 답변하세요
- 전문적이고 간결하게 답변하세요
- 모르는 내용은 솔직하게 모른다고 하세요
- 답변은 3문장 이내로 제한하세요""",
    messages=[
        {"role": "user", "content": "AI 에이전트가 뭔가요?"}
    ]
)

print(response.content[0].text)