from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# --- 1. 기본 설정 ---
load_dotenv()

# --- 2. 프롬프트 구성 ---
prompt = PromptTemplate.from_template(
    "{country}의 수도는 어디인가요?"
)

# --- 3. 사용모델 정의 ---
llm = ChatOpenAI(
    model="gpt-5.4-mini"
)

# --- 4. Chain 구성 및 실행 ---
chain = prompt | llm

result = chain.invoke({
    "country": "프랑스"
})

# --- 5. 결과출력 ---
print(result.content)