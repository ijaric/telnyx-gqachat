from pydantic import BaseModel


class Reply(BaseModel):
    answer: str
    sources: str
