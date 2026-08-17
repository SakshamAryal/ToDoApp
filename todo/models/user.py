from sqlalchemy import Column, String, Integer

from todo.database.base_class import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    username = Column(String, unique=True)
    



