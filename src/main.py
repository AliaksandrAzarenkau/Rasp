from fastapi import FastAPI

from src.user.router import router as user_router
from src.diary.router import router as diary_router

app = FastAPI(
    title='TGDiary'
)

app.include_router(user_router)
app.include_router(diary_router)
