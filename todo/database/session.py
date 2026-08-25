from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from todo.config import settings

ENGINE = create_engine(settings.DATABASE_URL, echo=False, pool_pre_ping=True)
SESSION = sessionmaker(ENGINE)
