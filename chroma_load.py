from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
import chromadb

OPEN_API_KEY = "sk-ttJFFNajeLV8y6rtF1iYXAoiNUbtaxcQUpVZIEEwZ7gGHVXY" 
embeddings = OpenAIEmbeddings(api_key=OPEN_API_KEY,base_url="https://api.chatanywhere.tech/v1")

cli = chromadb.HttpClient(host='127.0.0.1', port=8000)
docsearch = Chroma(collection_name="test",persist_directory="./chroma_data", embedding_function=embeddings,client=cli)

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(api_key=OPEN_API_KEY,base_url="https://api.chatanywhere.tech/v1"),
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
    return_source_documents=True,
)

def doc_txt(search_query):
    result=qa.invoke(search_query)
    return result["result"]

prompts = [
    'vector stores的实现方式',
    'vector stores的功能特性',
]

for prompt in prompts:
    print('問:'+prompt+'\n答:'+doc_txt(prompt)+'\n')