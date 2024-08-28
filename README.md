python -m venv venv

pip install --upgrade pip

source venv/bin/activate

pip install -r requirements.txt

export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

deactivate


 
# 运行 Chroma 的 Docker 容器
docker run -d --name chromadb -p 8000:8000 -e IS_PERSISTENT=TRUE -e ANONYMIZED_TELEMETRY=TRUE chromadb/chroma




# 安装 Weaviate
# 可以选择使用 Docker 安装或直接从源码安装
docker run -d --name weaviate -p 8080:8080 -p 50051:50051 --restart=always -e QUERY_MAX_CONCURRENCY=5 -e ENABLE_MODULES="text2vec-openai,openai" semitechnologies/weaviate