import logging
import os
import platform
import keyboards as kb
import firewall
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)
load_dotenv()

bot = Bot(token=os.environ.get("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply('''
Привет! Я - бот-инспектор
Вот что я умею:
/send <сообщение> или /say <сообщение> - отправить сообщение в чат
/echo <сообщение> - проверка связи
    ''', reply_markup=kb.alert_kb)


@dp.message_handler(commands=['send', 'say'])
async def send(message):
    if not firewall.is_allowed(message.from_user.id):
        await message.answer('Отказано в доступе', reply_markup=kb.remove_kb)
        return
    message_text = message.get_args()
    await bot.send_message(os.environ.get("DESTINATION_CHAT_ID"), message_text, reply_markup=kb.remove_kb)


@dp.message_handler(commands=['open'])
async def open_proc(message):
    if not firewall.is_admin(message.from_user.id):
        await message.answer('Отказано в доступе', reply_markup=kb.remove_kb)
        return

    program = message.get_args()
    if platform.system() == 'Windows':
        os.startfile(f'{program}')
        res = 0
    else:
        res = os.system(f"open -a '{program}'")

    if res > 0:
        answer = f"Не удалось найти программу '{program}'"
    else:
        answer = "Успешно"
    await message.answer(answer, reply_markup=kb.alert_kb)


@dp.message_handler(commands=['run'])
async def run_proc(message):
    if not firewall.is_admin(message.from_user.id):
        await message.answer('Отказано в доступе', reply_markup=kb.remove_kb)
        return

    filename = message.get_args()
    if platform.system() == 'Windows':
        os.startfile(f'{filename}')
    else:
        os.popen(f'sh {filename}')


@dp.message_handler(commands=['shutdown'])
async def shutdown_proc(message):
    if not firewall.is_admin(message.from_user.id):
        await message.answer('Отказано в доступе', reply_markup=kb.remove_kb)
        return

    if platform.system() == 'Windows':
        res = os.system('shutdown /s /t 1')
    else:
        res = os.system('shutdown -h now')

    if res > 0:
        answer = f"Код ответа {res}"
    else:
        answer = "Успешно"
    await message.answer(answer, reply_markup=kb.alert_kb)


@dp.message_handler(commands=['echo'])
async def echo(message: types.Message):
    await message.answer(message.text, reply_markup=kb.alert_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
