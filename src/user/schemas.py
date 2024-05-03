from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    name_tg: str
    tg_id: str
