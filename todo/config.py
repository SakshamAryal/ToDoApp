from pydantic_settings import BaseSettings, SettingsConfigDict
from todo.log import get_logger

log = get_logger(__name__)

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int


# def database_url_builder()
settings = Settings()
