import chatgpt

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


API_TOKEN = '5966015529:AAEWVcmoC8KhJ8MS0S7TdXuOsits93LSPPQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(Command("start"))
async def start_message(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Бонус"),
                KeyboardButton(text="Подписка"), 
            ]
        ]
    )
    await message.reply("Выбери действие:", reply_markup=keyboard)

@dp.message_handler(text="Бонус")
async def menu_bonus(message: types.Message):
    await bot.send_message(message.chat.id, "Bonus")

@dp.message_handler(text="Подписка")
async def menu_subscribe(message: types.Message):
    await bot.send_message(message.chat.id, "Subscribe")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.chat.id, chatgpt.returnPrompt(msg.text))

if __name__ == '__main__':
    executor.start_polling(dp)