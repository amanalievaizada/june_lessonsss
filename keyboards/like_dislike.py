from aiogram import Dispatcher
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


async def like_dislike_keyboard(tg_id):
    like_button = InlineKeyboardButton(
        text="Like",
        callback_data=f"like_{tg_id}"

    )
    dislike_button = InlineKeyboardButton(
        text="Dislike",
        callback_data="dislike"

    )
    donate_button = InlineKeyboardButton(
        text="Donate",
        callback_data=f"donate_{tg_id}"

    )

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [like_button],
        [dislike_button],
        [donate_button],

    ])
    return markup


async def after_donate_keyboard(tg_id):
    profiles_button = InlineKeyboardButton(
        text="Continue View Profile",
        callback_data="all_profiles"

    )
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [profiles_button],


    ])
    return markup