from langchain_chroma import Chroma
import chromadb
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA

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

search_query = "weaviate client"

print(qa.invoke(search_query)["result"])