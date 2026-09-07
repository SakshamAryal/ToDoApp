import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from todo.log import get_logger

log = get_logger(__name__)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    )
    POSTGRES_HOST : str
    POSTGRES_PORT : str
    POSTGRES_DB : str
    POSTGRES_USER : str
    POSTGRES_PASSWORD:str
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int


# def database_url_builder()
settings = Settings()
