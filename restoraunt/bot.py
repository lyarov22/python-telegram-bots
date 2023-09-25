import logging
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up bot and dispatcher
bot = Bot(token='5815288942:AAEClXHXrnpvNWQvEfTsYomW7R6qFti3_Fk')
dp = Dispatcher(bot)

# Start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Welcome to Restaraunt Menu Bot")

# Echo
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)

@dp.message_handler(content_types=['photo'])
async def handle_photo(msg: types.Message):
    photo_id = msg.photo[-1].file_id
    photo_file = await bot.get_file(photo_id)
    photo_bytes = await photo_file.download()

    # Получаем описание товара от пользователя
    await bot.send_message(msg.chat.id, "Введите описание товара:")
    description_message = await bot.wait_for('message', check=lambda m: m.chat.id == msg.chat.id)
    description = description_message.text

    # Создаем кнопки
    button1 = dp.InlineKeyboardButton("В корзину", callback_data="add_to_cart")
    button2 = dp.InlineKeyboardButton("Узнать больше", url="https://www.example.com")

    # Создаем инлайн-клавиатуру и добавляем в нее кнопки
    inline_keyboard = dp.InlineKeyboardMarkup().row(button1, button2)

    # Отправляем фото и описание товара с инлайн-клавиатурой
    await bot.send_photo(msg.chat.id, photo_bytes, caption=description, reply_markup=inline_keyboard)

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)