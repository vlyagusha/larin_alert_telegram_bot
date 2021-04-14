import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)
load_dotenv()

bot = Bot(token=os.environ.get("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['send'])
async def send(message):
    message_text = message.get_args()
    await bot.send_message(os.environ.get("DESTINATION_CHAT_ID"), message_text)


@dp.message_handler(commands=['open'])
async def open_proc(message):
    program = message.get_args()
    res = os.system(f"open -a '{program}'")
    if res > 0:
        await message.answer(f"Не удалось найти программу '{program}'")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
