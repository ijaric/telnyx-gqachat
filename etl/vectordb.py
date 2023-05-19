import chromadb
from chromadb.utils import embedding_functions

from settings import settings

client_settings = chromadb.config.Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=settings.DB_PATH,
    anonymized_telemetry=False,
)


def get_collection(collection_name: str):
    client = chromadb.Client(client_settings)
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=settings.OPENAI_API_KEY, model_name="text-embedding-ada-002"
    )

    collection = client.get_or_create_collection(
        name=collection_name, embedding_function=openai_ef
    )

    return collection
