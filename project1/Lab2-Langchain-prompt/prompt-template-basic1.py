from langchain_core.prompts import PromptTemplate

template = "{country}의 수도는 어디인가요?"
prompt_template = PromptTemplate.from_template(template)

prompt = prompt_template.format(country="프랑스")

print(prompt)
print(type(prompt))