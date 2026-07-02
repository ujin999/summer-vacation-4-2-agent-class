import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# client를 AsyncOpenAI로 생성합니다.
client = AsyncOpenAI()
MODEL = "gpt-5.4-mini"

async def ask(prompt: str):
    response = await client.responses.create(
        model=MODEL,
        input=prompt
    )
    return response.output_text

async def main():
    prompts = [
        "Docker를 한 문장으로 설명해줘.",
        "Kubernetes를 한 문장으로 설명해줘.",
        "RAG를 한 문장으로 설명해줘."
    ]

    results = await asyncio.gather(
        *(ask(prompt) for prompt in prompts)
    )

    for i, result in enumerate(results, start=1):
        print(f"\n--- 결과 {i} ---")
        print(result)

asyncio.run(main())

print("비동기 처리가 완료되었습니다.")