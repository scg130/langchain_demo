from langchain_openai import ChatOpenAI

# https://zhuanlan.zhihu.com/p/683550238
key = "sk-ttJFFNajeLV8y6rtF1iYXAoiNUbtaxcQUpVZIEEwZ7gGHVXY"

llm = ChatOpenAI(api_key=key,model="gpt-3.5-turbo",base_url="https://api.chatanywhere.tech/v1")

# print(llm.invoke("how can langsmith help with testing?").content)


from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

chain = prompt | llm 

print(chain.invoke({"input": "how can langsmith help with testing?"}).content)



