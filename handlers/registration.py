from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, file, FSInputFile
from aiogram import Dispatcher

from config import bot
from database.a_db import AsyncDatabase
from database import sql_queries
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class Registration(StatesGroup):
    name = State()
    bio = State()
    photo = State()


@router.callback_query(lambda call: call.data == 'registration')
async def registration_start(call: CallbackQuery,
                             state: FSMContext):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Please send me your Nickname"

    )
    await state.set_state(Registration.name)


@router.message(Registration.name)
async def process_nickname(message: types.Message,
                           state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    print(data)
    await bot.send_message(
        chat_id=message.chat.id,
        text="Tell me about yourself"
    )
    await state.set_state(Registration.bio)


@router.message(Registration.bio)
async def process_bio(message: types.Message,
                      state: FSMContext):
    await state.update_data(bio=message.text)
    data = await state.get_data()
    print(data)
    await bot.send_message(
        chat_id=message.chat.id,
        text="please send me your photo"
    )
    await state.set_state(Registration.photo)


@router.message(Registration.photo)
async def process_photo(message: types.Message,
                        state: FSMContext,
                        db=AsyncDatabase()):
    photos = message.photo
    print(photos)
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    await bot.download_file(
        file_path,
        "media/" + file_path

    )

    data = await state.get_data()
    await db.execute_query(
        query=sql_queries.INSERT_PROFILE_QUERY,
        params=(
            None,
            message.from_user.id,
            data['name'],
            data['bio'],
            "media" + file_path
        ),
        fetch="none"
    )

    photo = FSInputFile("media/" + file_path)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption=f"Name:{data['name']}\n"
                f"Bio:{data['bio']}\n"
    )
