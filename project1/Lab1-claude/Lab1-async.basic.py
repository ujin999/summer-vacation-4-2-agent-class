import asyncio
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

async def ask(client, question):
    response = await client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": question}]
    )
    return response.content[0].text

async def main():
    # 비동기 클라이언트 초기화
    async with anthropic.AsyncAnthropic() as client:
        questions = [
            "Python이란?",
            "JavaScript이란?",
            "Go언어란?",
        ]

        # 3개 질문 동시 병렬 처리
        tasks = [ask(client, q) for q in questions]
        answers = await asyncio.gather(*tasks)

        for q, a in zip(questions, answers):
            print(f"Q: {q}{a[:100]}...\n")

asyncio.run(main())