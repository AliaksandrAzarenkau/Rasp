from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP, ForeignKey
from sqlalchemy.orm import DeclarativeBase

import datetime

from src.user.models import User


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    date = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    type = Column(String)
    description = Column(TEXT)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
