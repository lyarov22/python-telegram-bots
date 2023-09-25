import telebot
import chatgpt
from telebot import types

bot = telebot.TeleBot("5886491082:AAHrDrGLXjEFu1Cr1akX060ns0r1DRIAWSs")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, я бот илюши для отладки")









bot.polling()