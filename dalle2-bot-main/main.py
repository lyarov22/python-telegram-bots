import os
from background import keep_alive #импорт функции для поддержки работоспособности

import pip
pip.main(['install', 'aiogram'])

import time
import dalle2

import aiogram
from aiogram import Bot, Dispatcher, executor, types

token = os.environ['BOT_TOKEN']

bot = Bot(token=token)
dp = Dispatcher(bot)

about = "Dalle-2 Aiogram Bot v1\n 1request - 0.02$ \n@totaljerkface"

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(about)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("[%s](%s)" % (message.text, dalle2.returnPrompt(message.text)), parse_mode="MarkdownV2")

keep_alive()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

