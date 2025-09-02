# backend/sanctum/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    """
    Manages application settings and environment variables.
    """
    # Load settings from a .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Database
    DATABASE_URL: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # LLM
    OPENAI_API_KEY: Optional[str] = None


# Create a single, reusable instance of the settings
settings = Settings()
