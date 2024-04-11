from datetime import datetime

from pydantic import BaseModel


class EventCreate(BaseModel):
    id: int
    date: datetime
    type: str
    description: str
    user_id: int
