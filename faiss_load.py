from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_openai import ChatOpenAI

OPEN_API_KEY = "sk-ttJFFNajeLV8y6rtF1iYXAoiNUbtaxcQUpVZIEEwZ7gGHVXY" 
embeddings = OpenAIEmbeddings(api_key=OPEN_API_KEY,base_url="https://api.chatanywhere.tech/v1")

prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:
 
<context>
{context}
</context>
 
Question: {input}""")

llm = ChatOpenAI(api_key=OPEN_API_KEY,base_url="https://api.chatanywhere.tech/v1") 
document_chain = create_stuff_documents_chain(llm, prompt)

vector = FAISS.load_local(folder_path="./local_db_data/data.db",embeddings=embeddings,allow_dangerous_deserialization=True)


# res = vector.similarity_search_with_score(query="vector stores的实现方式", k=2)
# print(res[0][0].page_content,res[0][1])
# print(res[1][0].page_content,res[1][1])

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)
response = retrieval_chain.invoke({"input": "vector stores的实现方式"})
print(response["answer"])
