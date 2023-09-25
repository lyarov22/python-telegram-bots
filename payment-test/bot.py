import config
import logging
import chatgpt

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



# log

logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# prices
tarif = 0
PRICE = types.LabeledPrice(label="Subscribe", amount=500*100) # amount need be in cents!


# menu
@dp.message_handler(Command("start"))
async def start_message(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
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
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [   
                KeyboardButton(text="1 час"),
                KeyboardButton(text="1 день"),
                KeyboardButton(text="3 дня"),
                KeyboardButton(text="7 дней"), 
            ]
        ]
    )
    await message.reply("Выберите тариф:", reply_markup=keyboard)

# tarifs

@dp.message_handler(text="1 час")
async def menu_1h(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="Telegram"),
                KeyboardButton(text="Qiwi"), 
            ]
        ]
    )
    await message.reply("Выбери тип оплаты:", reply_markup=keyboard)
    tarif = 1

@dp.message_handler(text="1 день")
async def menu_1d(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="Telegram"),
                KeyboardButton(text="Qiwi"), 
            ]
        ]
    )
    await message.reply("Выбери тип оплаты:", reply_markup=keyboard)
    tarif = 2

@dp.message_handler(text="3 дня")
async def menu_3d(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="Telegram"),
                KeyboardButton(text="Qiwi"), 
            ]
        ]
    )
    await message.reply("Выбери тип оплаты:", reply_markup=keyboard)
    tarif = 3

@dp.message_handler(text="7 дней")
async def menu_7d(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="Telegram"),
                KeyboardButton(text="Qiwi"), 
            ]
        ]
    )
    await message.reply("Выбери тип оплаты:", reply_markup=keyboard)
    tarif = 4

# chat-gpt request

# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.chat.id, chatgpt.returnPrompt(msg.text))

photo = 'https://i.ibb.co/ZHFVyS4/149-1-0.png'


# buy
@dp.message_handler(text="Telegram")
async def telegram(message: types.Message):
    if config.PAYMENTS_TOKEN.split(":")[1] == 'TEST':
        await bot.send_message(message.chat.id, "Форма оплаты:")

    PRICE = types.LabeledPrice(label="Subscribe", amount=12345*100)
    if (tarif == 1): 
        PRICE = types.LabeledPrice(label="Subscribe", amount=90*100)
    if (tarif == 2): 
        PRICE = types.LabeledPrice(label="Subscribe", amount=290*100)
    if (tarif == 3): 
        PRICE = types.LabeledPrice(label="Subscribe", amount=790*100)
    if (tarif == 4): 
        PRICE = types.LabeledPrice(label="Subscribe", amount=1490*100)

    await bot.send_invoice(
        message.chat.id,
        title="Subcribe",
        description="Simple description",
        provider_token=config.PAYMENTS_TOKEN,
        currency="rub",
        photo_url=photo,
        photo_width=400,
        photo_height=400,
        is_flexible=False,
        prices=[PRICE],
        start_parameter="one-month-subcription",
        payload="test-invoice-payload"
    )

# pre checkout (nust be answered in 10 sec)
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):

    print("SUCCESSFUL PAYENT:")
    payment_info = message.successful_payment.to_python()
    
    for key, value in payment_info.items():
        print(f"{key} = {value}")
    
    await bot.send_message(message.chat.id, 
    f"Payment for the amount {message.successful_payment.total_amount // 100} {message.successful_payment.currency} passed successfully")

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)