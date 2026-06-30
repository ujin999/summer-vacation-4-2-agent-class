import asyncio
from openai import OpenAI, AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('LOCAL_API_KEY')

BASE_URL = "http://gpu.ai.wyhil.com:58500/v1/"
API_KEY = api_key
MODEL = "gemma-4-e4b-it"


def example_1_completion():
    client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

    response = client.completions.create(
        model=MODEL,
        prompt="vLLM의 장점을 3가지로 설명해 주세요.",
        max_tokens=8192,
        temperature=0.7,
    )

    print(response.choices[0].text)


def example_2_chat():
    client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "당신은 AI 인프라 강사입니다."},
            {"role": "user", "content": "vLLM이 무엇인지 쉽게 설명해 주세요."},
        ],
        max_tokens=8192,
        temperature=0.7,
    )

    print(response.choices[0].message.content)


def example_3_stream():
    client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

    stream = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "LLM 서빙에서 vLLM을 사용하는 이유를 설명해 주세요."}
        ],
        max_tokens=8192,
        temperature=0.7,
        stream=True,
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)

    print()


async def example_4_async():
    client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "PagedAttention이 무엇인지 쉽게 설명해 주세요."}
        ],
        max_tokens=8192,
        temperature=0.7,
    )

    print(response.choices[0].message.content)


async def example_5_batch():
    client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

    questions = [
        "vLLM이 무엇인가요?",
        "PagedAttention이 무엇인가요?",
        "LLM 서빙에서 batch 처리가 중요한 이유는 무엇인가요?",
        "vLLM을 AI Agent 서비스에 어떻게 활용할 수 있나요?",
    ]

    async def ask(question: str) -> str:
        response = await client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": question}
            ],
            max_tokens=8192,
            temperature=0.7,
        )
        return response.choices[0].message.content

    answers = await asyncio.gather(*[ask(q) for q in questions])

    for question, answer in zip(questions, answers):
        print("\n==============================")
        print("질문:", question)
        print("답변:", answer)


if __name__ == "__main__":
    print("\n[1] 일반 Completion 호출")
    example_1_completion()

    print("\n[2] Chat 호출")
    example_2_chat()

    print("\n[3] Stream 호출")
    example_3_stream()

    print("\n[4] Async 호출")
    asyncio.run(example_4_async())

    print("\n[5] Batch 호출")
    asyncio.run(example_5_batch())