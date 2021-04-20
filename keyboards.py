from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_alert = KeyboardButton('/say Attention!!!')

alert_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_alert)
