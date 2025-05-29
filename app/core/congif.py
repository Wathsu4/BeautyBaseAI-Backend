from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "BeautyBase AI"
    API_V1_STR: str = "/api/v1"

    # Database settings
    DATABASE_URL: str

    #OpenAI settings
    OPENAI_API_KEY: str = "OPENAI_API_KEY_HERE"

    #For pydantic-settings to load from .env file
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()