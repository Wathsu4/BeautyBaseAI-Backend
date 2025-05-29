# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "BeautyBase AI"
    API_V1_STR: str = "/api/v1"

    # Database
    DATABASE_URL: str

    # OpenAI
    OPENAI_API_KEY: str = "YOUR_OPENAI_API_KEY_HERE" # Will be overridden by .env

    # For pydantic-settings to load from .env file
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()