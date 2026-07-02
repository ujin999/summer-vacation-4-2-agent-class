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


async def print_delay_message():
    while True:
        await asyncio.sleep(1)
        print("1초 후에 출력되는 메시지입니다.")


async def main():
    # AI 요청을 백그라운드에서 시작
    ask_task = asyncio.create_task(
        ask("RAG 시스템을 한 문장으로 설명해줘.")
    )

    # 1초마다 출력하는 작업도 시작
    print_task = asyncio.create_task(
        print_delay_message()
    )

    # AI 응답을 기다림
    result = await ask_task

    # AI 응답이 왔으므로 출력 작업 종료
    print_task.cancel()

    try:
        await print_task
    except asyncio.CancelledError:
        pass

    print("\nAI 응답:")
    print(result)


asyncio.run(main())

print("비동기 처리가 완료되었습니다.")