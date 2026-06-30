from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_template("{topic}에 대해 쉽게 설명해줘.")
model = ChatOpenAI(model="gpt-5.5")
print(f"모델: {model.model}, max_tokens: {model.max_tokens}, temperature: {model.temperature}")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

question = {"topic": "인공지능"}
result = chain.invoke(question)

print(result)
print(type(result))