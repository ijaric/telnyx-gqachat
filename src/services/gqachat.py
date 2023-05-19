from functools import lru_cache

from fastapi import Depends
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma

from src.core.settings import settings
from src.db.chromadb import get_chromadb
from src.models.gqachat import Reply


class GQAService:
    def __init__(self, vectordb):
        self.vectordb = vectordb

    async def get_answer(self, question: str = None) -> Reply | None:
        """
        Endpoint to get an answer for a question based on Telnyx's documentation

        Parameters:
        - `question`: The question

        Returns:
        A 'Reply' object that contains 'answer' and 'sources'
        """

        llm = ChatOpenAI(
            openai_api_key=settings.OPENAI_API_KEY,
            model_name=settings.GPT_MODEL,
            temperature=settings.GPT_TEMPERATURE,
        )

        qa_chain = load_qa_with_sources_chain(llm, chain_type="stuff")
        qa_source = RetrievalQAWithSourcesChain(
            combine_documents_chain=qa_chain, retriever=self.vectordb.as_retriever()
        )
        result = qa_source({"question": question}, return_only_outputs=True)

        if not result:
            return None

        return result


@lru_cache()
def get_qga_service(
    vectordb: Chroma = Depends(get_chromadb),
) -> GQAService:
    return GQAService(vectordb)
