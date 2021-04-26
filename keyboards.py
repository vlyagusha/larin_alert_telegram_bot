import emoji
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


button_warning = KeyboardButton(emoji.emojize('/say ⚠️ Осторожно! ⚠️ Посторонний! ⚠️'))
button_danger = KeyboardButton(emoji.emojize('/say ‼️ 🔥 Опасность! 🔥 ‼️'))

alert_kb = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(button_warning)\
    .add(button_danger)

remove_kb = ReplyKeyboardRemove()
