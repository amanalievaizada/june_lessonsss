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
    profile_button = InlineKeyboardButton(
        text="My Profile",
        callback_data="my_profile"

    )
    like_button = InlineKeyboardButton(
        text="View profiles",
        callback_data="all_profiles"

    )
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [registration_button],
        [profile_button],
        [like_button],

    ])
    return markup
