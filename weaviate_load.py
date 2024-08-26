import weaviate
from weaviate.connect import ConnectionParams

# Connect to the Weaviate instance
clientV4 = weaviate.WeaviateClient(connection_params=ConnectionParams.from_params(
    "127.0.0.1",
    8080,
    False,
    "127.0.0.1",
    50051,
    False,
))

clientV4.collections.create("Article")

print(clientV4.collections.get("Article").data)
exit()


client = weaviate.Client(url="http://127.0.0.1:8080")


from langchain_community.retrievers import (
    WeaviateHybridSearchRetriever,
)

# class_obj = {
#     "class": "classname11",
#     "vectorizer": "text2vec-openai",
# }
# client.schema.create_class(class_obj)




retriever = WeaviateHybridSearchRetriever(
    client=client,
    index_name="LangChain",
    text_key="text",
    attributes=[],
    create_schema_if_missing=True,
)

retriever.invoke("aaaaa")
