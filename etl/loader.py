from typing import Type

from chromadb.api.models.Collection import Collection


def load_data(collection: Type[Collection], data: dict[list]):
    try:
        collection.add(
            documents=data["texts"], metadatas=data["metadatas"], ids=data["ids"]
        )
    except Exception as error:
        raise ValueError(error)
