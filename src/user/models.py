from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase

import datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name_tg = Column(String, nullable=False)
    joined_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)