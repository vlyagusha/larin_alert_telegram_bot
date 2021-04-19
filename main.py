import logging
import os
import platform
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)
load_dotenv()

bot = Bot(token=os.environ.get("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply('''
Привет! Я - бот-инпектор
Вот что я умею:
/send или /say - отправить команду в чат
/open - открыть программу на удалённом компьютере
/shutdown - выключить удаленный компьютер
    ''')


@dp.message_handler(commands=['send', 'say'])
async def send(message):
    message_text = "Сообщение от " + message.from_user.full_name + ":\n" + message.get_args()
    await bot.send_message(os.environ.get("DESTINATION_CHAT_ID"), message_text)


@dp.message_handler(commands=['open'])
async def open_proc(message):
    program = message.get_args()
    res = os.system(f"open -a '{program}'")
    if res > 0:
        await message.answer(f"Не удалось найти программу '{program}'")


@dp.message_handler(commands=['run'])
async def open_proc(message):
    filename = message.get_args()
    os.popen(f'sh {filename}')


@dp.message_handler(commands=['shutdown'])
async def open_proc(message):
    if message.from_user.id == os.environ.get("ADMIN_USER_ID"):
        if platform.system() == 'Windows':
            os.system('shutdown /p /f')
        else:
            os.system('shutdown -h now')


@dp.message_handler(commands=['ostest'])
async def echo(message: types.Message):
    # await message.answer(message.text)
    await message.answer(platform.system())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
