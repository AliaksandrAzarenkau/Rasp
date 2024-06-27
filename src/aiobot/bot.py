from aiogram import Bot, Dispatcher, types, Router
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

from config import BOT_TOKEN
from user.router import post_user
from user.schemas import UserCreate

import asyncio
import logging
from typing import List

logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)
form_router = Router()

class Form(StatesGroup):
    action_to_do = State()
    next_action = State()

@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    """
    Send start message and transmit user data to user.post_user router
    """
    await state.set_state(Form.action_to_do)

    await create_user(message)

    await message.answer(
        "Привет, что нужно сделать?",
        reply_markup=get_keyboard(["Добавить запись", "Посмотреть записи"]))

@form_router.message(Form.action_to_do, F.text.casefold() == "Добавить запись")
async def create_event(message: Message, state: FSMContext) -> None:
    print('+')
    await state.update_data(action_to_do=message.text)
    await state.set_state(Form.next_action)
    print(message.text)
    await message.answer(
        "Готово! Что дальше?",
        reply_markup=get_keyboard(['Добавить ещё одну', 'Пока всё']),
    )
    await command_start(message=message)

# @dp.message(Command("start"))
# async def cmd_numbers(message: types.Message):
#     """
#     Send start message and transmit user data to user.post_user router
#     """
#     data = await get_user_info(message)
#     await post_user(UserCreate(tg_id=data.get('user_id'),
#                                name_tg=data.get('username'),
#                                tg_flag=True))
#
#     await message.answer("Привет, что нужно сделать?", reply_markup=get_keyboard())


# @dp.callback_query(F.data.startswith("event_"))
# async def callbacks_event(callback: types.CallbackQuery):
#     action = callback.data.split("_")[1]
#
#     if action == 'create':
#
#
#         print('data')
#
#     if action == 'get':
#         print('good')
#     elif action == "submit":
#         await callback.message.answer(text='Готово!')
#         await callback.message.answer("Что нужно сделать?", reply_markup=get_keyboard())



# @dp.message(F.text)
# async def get_message(message: types.Message):
#     return message.text
def get_keyboard(options: List[str]) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=options[0]),
                KeyboardButton(text=options[1]),
            ]
        ],
        resize_keyboard=True,
    )

    return keyboard


async def create_user(message: types.Message):
    user_id = str(message.from_user.id)
    username = str(message.from_user.username)

    await post_user(UserCreate(tg_id=user_id, name_tg=username), tg_flag=True)


async def main():
    dp = Dispatcher()
    dp.include_router(form_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
