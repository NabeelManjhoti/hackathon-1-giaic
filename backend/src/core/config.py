from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    openai_api_key: str
    qdrant_url: str
    qdrant_api_key: str
    database_url: str
    api_key: str
    environment: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()