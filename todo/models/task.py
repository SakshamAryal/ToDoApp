from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime

from todo.database.base_class import Base

class Task(Base):
    __table_name__ = 'tasks'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    priority: int = Column(Integer)
    deadline: datetime = Column(DateTime)
    description: str = Column(String)
    completed: bool = Column(Boolean)
    created_at: datetime = Column(DateTime)
    updated_at: datetime = Column(DateTime)

