from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document



OPEN_API_KEY = "sk-ttJFFNajeLV8y6rtF1iYXAoiNUbtaxcQUpVZIEEwZ7gGHVXY" 

loader = WebBaseLoader("https://blog.csdn.net/2401_84494441/article/details/140370935")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(api_key=OPEN_API_KEY,base_url="https://api.chatanywhere.tech/v1")


import weaviate
from langchain_weaviate.vectorstores import WeaviateVectorStore

# Connect to the Weaviate instance
weaviate_client = weaviate.connect_to_local(skip_init_checks=True)
db = WeaviateVectorStore.from_documents(docs, embeddings, client=weaviate_client)
docArr = [
    Document(
        metadata={
            "title": "Embracing The Future: AI Unveiled",
            "author": "Dr. Rebecca Simmons",
        },
        page_content="A comprehensive analysis of the evolution of artificial intelligence, from its inception to its future prospects. Dr. Simmons covers ethical considerations, potentials, and threats posed by AI.",
    ),
    Document(
        metadata={
            "title": "Symbiosis: Harmonizing Humans and AI",
            "author": "Prof. Jonathan K. Sterling",
        },
        page_content="Prof. Sterling explores the potential for harmonious coexistence between humans and artificial intelligence. The book discusses how AI can be integrated into society in a beneficial and non-disruptive manner.",
    )]
db.add_documents(docArr)
db.as_retriever()


# Search for similar documents
query = "vector stores的实现方式"
docs = db.similarity_search(query)


# print(db.search(query=query, search_type="similarity"))


# Print the first 100 characters of each result
for i, doc in enumerate(docs):
    print(f"\nDocument {i+1}:")
    print(doc.page_content[:200] + "...")