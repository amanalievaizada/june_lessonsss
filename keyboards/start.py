from aiogram import Dispatcher
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


async def start_menu_keyboard():
    registration_button = InlineKeyboardButton(
        text="Registration",
        callback_data="registration"

    )
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [registration_button],

    ])
    return markup
