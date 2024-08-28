
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = WebBaseLoader("https://blog.csdn.net/2401_84494441/article/details/140370935")
data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(data)


OPEN_API_KEY = "sk-ttJFFNajeLV8y6rtF1iYXAoiNUbtaxcQUpVZIEEwZ7gGHVXY" 
embeddings = OpenAIEmbeddings(api_key=OPEN_API_KEY,base_url="https://api.chatanywhere.tech/v1")
 
db = FAISS.from_documents(documents=split_docs,embedding=embeddings)
db.add_documents(split_docs)
db.save_local("./local_db_data/data.db")

