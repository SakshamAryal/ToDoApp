import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from todo.log import get_logger

#
# DOTENV = os.path.join(os.path.dirname(), ".env")

log = get_logger(__name__)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    )
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int


settings = Settings()
