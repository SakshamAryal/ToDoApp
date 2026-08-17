import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr

from todo.log import get_logger

log = get_logger(__name__)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
    env_file=".env",
    env_prefix="TODO_",
    )