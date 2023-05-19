import orjson
from pydantic import BaseModel, AnyHttpUrl, Field


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class OrjsonMixin:
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class FAQMetadata(BaseModel, OrjsonMixin):
    id: str = None
    title: str = None
    url: AnyHttpUrl = None


class Document(BaseModel, OrjsonMixin):
    page_content: str
    metadata: dict = Field(default_factory=dict)


class Documents(BaseModel, OrjsonMixin):
    __root__: Document
