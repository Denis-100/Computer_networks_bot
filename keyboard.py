from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

networks = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Локальная сеть"),
    KeyboardButton(text="Глобальная сеть"),
    KeyboardButton(text="Городская сеть")],

    [KeyboardButton(text="Персональная сеть"),
    KeyboardButton(text="Виртуальная частная сеть")],
],
resize_keyboard=True,
input_field_placeholder="О какой сети хотите узнать?")

local_networks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подробнее", callback_data="local_info"),
     InlineKeyboardButton(text="Схема", callback_data="local_schema")]
])

global_networks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подробнее", callback_data="global_info"),
     InlineKeyboardButton(text="Схема", callback_data="global_schema")]
])

city_networks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подробнее", callback_data="city_info"),
     InlineKeyboardButton(text="Схема", callback_data="city_schema")]
])

personal_networks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подробнее", callback_data="personal_into"),
     InlineKeyboardButton(text="Схема", callback_data="personal_schema")]
])

vpn_networks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подробнее", callback_data="vpn_info"),
     InlineKeyboardButton(text="Схема", callback_data="vpn_schema")]
])
