import os

from pydantic.env_settings import BaseSettings
from pydantic.fields import Field


class Settings(BaseSettings):
    PROJECT_NAME: str = Field(
        default=os.getenv("PROJECT_NAME", "telnyx-gqa-chat"), env="PROJECT_NAME"
    )
    DB_PATH: str = Field(default=os.getenv("DB_PATH", "../db"), env="DB_PATH")
    OPENAI_API_KEY: str = Field(
        default=os.getenv("OPENAI_API_KEY"), env="OPENAI_API_KEY"
    )
    INDEX_NAME: str = Field(
        default=os.getenv("INDEX_NAME", "telnyx-test"), env="INDEX_NAME"
    )

    class Config:
        env_prefix = ""

    @property
    def BASE_DIR(self) -> str:
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


settings = Settings()
