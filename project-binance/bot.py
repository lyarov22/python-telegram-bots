import logging
import asyncio
from binance.client import Client
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Введите свои api_key и api_secret
api_key = 'RV7XR1GtEaxvaqKPuWDomfMfq8ex95f0rjCsAQdSCSaSkWhhEnts1hQUKBQWH86O'
api_secret = 'JwvfW7vmjk17kt4fSXJG4aanN8QG3ZlRETv4IIjgXpbNeJSLPySodscgc6TDXUjS'

# Настройка логгера для отображения сообщений в консоли
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token='ваш_токен')
dp = Dispatcher(bot)

# Инициализация клиента Binance
client = Client(api_key, api_secret)

# Словарь соответствий между тикерами и названиями валют
currency_pairs = {
    "BTCUSDT": "Bitcoin",
    "ETHUSDT": "Ethereum",
    "ADAUSDT": "Cardano",
    "BNBUSDT": "Binance Coin",
    "DOTUSDT": "Polkadot",
    "XRPUSDT": "XRP",
    "SOLUSDT": "Solana",
    "LUNAUSDT": "Luna",
    "AVAXUSDT": "Avalanche",
    "ALGOUSDT": "Algorand"
}

# Функция для получения цены валютной пары
def get_currency_price(pair):
    ticker = client.get_symbol_ticker(symbol=pair)
    price = float(ticker['price'])
    return price

# Функция для вывода меню выбора валют
async def show_currency_menu(message: types.Message):
    # Создание кнопки для выбора всех валют
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Все валюты', callback_data='all')
    keyboard.add(button)

    # Отправка сообщения с кнопкой
    await bot.send_message(chat_id=message.chat.id, text='Выберите валюту:', reply_markup=keyboard)

# Функция для вывода цен всех валют
async def show_all_currency_prices(callback_query: types.CallbackQuery):
    # Формирование сообщения со всеми ценами валют
    text = 'Курсы валют:\n\n'
    for pair, name in currency_pairs.items():
        price = get_currency_price(pair)
        text += f'{name}: {price:.2f} USDT\n'
    # Отправка сообщения с ценами валют
    await bot.send_message(chat_id=callback_query.message.chat.id, text=text)

# Регистрация обработчика команды /start
@dp.message_handler(commands=['start'])
async def start_command_handler(message: types.Message):
    await show_currency_menu(message)

@dp.callback_query_handler(lambda callback_query: True)
async def process_callback(callback_query: types.CallbackQuery):
# Если нажата кнопка "Все валюты"
    if callback_query.data == 'all':
        # Формируем текст со всеми валютами и их курсами
        text = ''
        for pair, name in currency_pairs.items():
        price = get_currency_price(pair)
        text += f"{name}: {price:.2f} USDT\n"
        # Отправляем сообщение с текстом
        await bot.send_message(chat_id=callback_query.message.chat.id, text=text)
        # Если нажата кнопка выбора конкретной валюты
    else:
        # Вызываем функцию для вывода курса выбранной валюты
        await show_currency_price(callback_query)

if __name__ == '__main__':
    asyncio.run(dp.start_polling())
