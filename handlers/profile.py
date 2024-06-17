from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, FSInputFile

from config import bot
from database.a_db import AsyncDatabase
from database import sql_queries

router = Router()


@router.callback_query(lambda call: call.data == 'my_profile')
async def my_profile_call(call: CallbackQuery,
                          db=AsyncDatabase()):
    user = await db.execute_query(
        query=sql_queries.SELECT_PROFILE_QUERY,
        params=(
            call.from_user.id,
        ),
        fetch="one"
    )
    print(user)
    photo = FSInputFile(user['PHOTO'])
    await bot.send_photo(
        chat_id=call.from_user.id,
        photo=photo,
        caption=f"Name: {user['NICKNAME']}\n"
                f"Bio: {user['BIO']}\n"
    )
