from langchain_chroma import Chroma
import chromadb

# 配置 Chroma 连接设置（本地持久化设置）
persist_directory = "./chroma_data"

cli = chromadb.HttpClient(host='127.0.0.1', port=8000)
# 创建 Chroma 实例并配置连接设置
db = Chroma(
    collection_name="test",
    client=cli,
    persist_directory=persist_directory,
)


# 打印 Chroma 实例信息
print(db)

