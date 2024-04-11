from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    name_tg: str
    joined_at: datetime
