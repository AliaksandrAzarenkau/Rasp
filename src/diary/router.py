from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.diary.models import Event
from src.diary.schemas import EventCreate

router = APIRouter(
    prefix='/diary',
    tags=['Diary']
)


@router.get('/get', response_model=EventCreate)
async def get_events(event_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Event).where(Event.type == event_type)
    result = await session.execute(query)
    return result.all()  #Переделать после добавления валидации scalars().


@router.post('/add_event')
async def post_event(new_event: EventCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Event).values(**new_event.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}
