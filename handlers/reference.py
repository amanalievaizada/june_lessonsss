from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, FSInputFile, InlineKeyboardMarkup
from aiogram.utils.deep_linking import create_start_link

from config import bot
from database.a_db import AsyncDatabase
from database import sql_queries
from keyboards.reference_menu import reference_menu_keyboard
import binascii
import os

router = Router()


@router.callback_query(lambda call: call.data == "reference_menu")
async def reference_menu_call(call: CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Hello, this is reference menu\n"
             " you can create reference link\n"
             "please share with your friends and get your bonus",
        reply_markup=await reference_menu_keyboard()
    )


@router.callback_query(lambda call: call.data == "reference_link")
async def reference_link_call(call: CallbackQuery,
                              db=AsyncDatabase()):
    user = await db.execute_query(
        query=sql_queries.SELECT_USER_QUERY,
        params=(
            call.from_user.id,

        ),
        fetch="one"
    )
    print(user)

    if user['REFERENCE_LINK'] is None:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await create_start_link(bot=bot, payload=token)
        await db.execute_query(
            query=sql_queries.UPDATE_USER_LINK_COLUMN_QUERY,
            params=(
                link,
                call.from_user.id,

            ),
            fetch="none"
        )
        await bot.send_message(
            chat_id=call.from_user.id,
            text="this is  new reference link\n"
                 f"{link}"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"this is old reference link\n"
                 f"{user['REFERENCE_LINK']}"
        )


@router.callback_query(lambda call: call.data == "balance")
async def balance_call(call: CallbackQuery,
                       db=AsyncDatabase()):
    user = await db.execute_query(
        query=sql_queries.SELECT_USER_QUERY,
        params=(
            call.from_user.id,

        ),
        fetch="one"
    )

    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"your balance: {user['BALANCE']}"
    )
