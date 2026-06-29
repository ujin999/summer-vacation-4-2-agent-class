from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {
            "role": "system",
            "content": "당신은 친절한 AI 비서입니다."
        },
        {
            "role": "user",
            "content": "Oracle Database 26ai의 주요 특징을 설명해주세요."
        }
    ]
)

print(response.choices[0].message.content)