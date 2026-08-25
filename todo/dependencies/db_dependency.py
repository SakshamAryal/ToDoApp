from sqlalchemy.orm import Session
from todo.database.session import SESSION
from typing import Generator

def get_db() -> Generator[Session, None, None]:
    db = SESSION()
    try:
        yield db
    finally:
        db.close()
