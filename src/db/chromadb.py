import chromadb
from core.settings import settings
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

client_settings = chromadb.config.Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=settings.DB_PATH,
    anonymized_telemetry=False,
)

embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)

vectordb = Chroma(
    collection_name=settings.INDEX_NAME,
    embedding_function=embeddings,
    client_settings=client_settings,
    persist_directory=settings.DB_PATH,
)


async def get_chromadb():
    return vectordb
