from sqlalchemy import Column, String, Integer
from app.db.session import Base


class User(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
