from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

loader = WebBaseLoader("https://blog.csdn.net/2401_84494441/article/details/140370935")
data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(data)


OPEN_API_KEY = "sk-ttJFFNajeLV8y6rtF1iYXAoiNUbtaxcQUpVZIEEwZ7gGHVXY" 
embeddings = OpenAIEmbeddings(api_key=OPEN_API_KEY,base_url="https://api.chatanywhere.tech/v1")

cli = chromadb.HttpClient(host='127.0.0.1', port=8000)
docSearch = Chroma.from_documents(split_docs, embeddings,persist_directory="./chroma_data",collection_name="test",client=cli)
docSearch.add_documents(split_docs)