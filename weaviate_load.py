import weaviate
with weaviate.connect_to_local(
    host="localhost",
    port=8080,
    grpc_port=50051,
) as client:
    client.is_ready()
    if not client.collections.exists("Article"):
        client.collections.create("Article")
    else:   
        print(client.collections.get("Article"))

    from langchain_community.retrievers import (
        WeaviateHybridSearchRetriever,
    )

    retriever = WeaviateHybridSearchRetriever(
        client=client,
        index_name="LangChain",
        text_key="text",
        attributes=[],
        create_schema_if_missing=True,
    )

    retriever.invoke("aaaaa")




