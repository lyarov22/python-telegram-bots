import os
from background import keep_alive #импорт функции для поддержки работоспособности
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time
import chatgpt

token = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(token)
about = "GPT-3 telebot Bot v1 \n@totaljerkface"

@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, about)

@bot.message_handler(func=lambda msg: msg.text is not None)
def echo_all(message):
  bot.send_message(message.chat.id, chatgpt.returnPrompt(message.text))

keep_alive()#запускаем flask-сервер в отдельном потоке. Подробнее ниже...
bot.polling(non_stop=True, interval=0) #запуск бота