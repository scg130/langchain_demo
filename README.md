python -m venv venv

pip install --upgrade pip

source venv/bin/activate

pip install -r requirements.txt

export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

deactivate






# 安装 Weaviate
# 可以选择使用 Docker 安装或直接从源码安装
docker run -d --name weaviate -p 8080:8080 -p 50051:50051 --restart=always -e QUERY_MAX_CONCURRENCY=5 -e ENABLE_MODULES="text2vec-openai,openai" semitechnologies/weaviate