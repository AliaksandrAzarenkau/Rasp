import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from fastapi import Depends
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from config import BOT_TOKEN
from user.router import post_user
from user.schemas import UserCreate

logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

user_data = {}


def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="+", callback_data="event_good"),
            types.InlineKeyboardButton(text="-", callback_data="event_bad")
        ],
        [types.InlineKeyboardButton(text="Подтвердить", callback_data="event_submit")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@dp.message(Command("start"))
async def cmd_numbers(message: types.Message):
    user_id = str(message.from_user.id)
    username = str(message.from_user.username)
    await post_user(UserCreate(tg_id=user_id, name_tg=username), tg_flag=True)

    await message.answer("Что нужно отметить?", reply_markup=get_keyboard())


@dp.callback_query(F.data.startswith("event_"))
async def callbacks_event(callback: types.CallbackQuery):
    event = {}
    action = callback.data.split("_")[1]

    if action == 'bad':
        print('bad')
    elif action == 'good':
        print('good')
    elif action == "submit":
        await callback.message.edit_text(f"Запомнили!")
        await callback.answer()


@dp.message(F.text)
async def get_message(message: types.Message):
    print(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
