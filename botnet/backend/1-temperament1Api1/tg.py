from telebot import types
from modules import ru, en
import time
import telebot
import chatgpt
import asyncio
from datetime import datetime, timedelta

import payment2


bot = telebot.TeleBot("5988511703:AAGBZHypC7OdwW6Plgx-WyX2T9hd3ZDMYWw")

sub_time = None
target_time = None
tks = 0
dtime = None
isReq = False
isFree = True

# Create a handler
@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
  buttonFree = types.KeyboardButton('Токены')
  buttonSubscribe = types.KeyboardButton('Купить подписку')
  buttonMenu = types.KeyboardButton('Меню')
  buttonReq = types.KeyboardButton('Новый запрос')
  markup.add(buttonFree, buttonSubscribe, buttonMenu, buttonReq)
  bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=markup)

@bot.message_handler(commands=['menu'])
def menu(message):
  markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
  buttonFree = types.KeyboardButton('Токены')
  buttonSubscribe = types.KeyboardButton('Купить подписку')
  buttonMenu = types.KeyboardButton('Меню')
  buttonReq = types.KeyboardButton('Новый запрос')
  markup.add(buttonFree, buttonSubscribe, buttonMenu, buttonReq)
  bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=markup)


@bot.message_handler(func = lambda msg: msg.text == 'Токены')
def tokens(msg):
  global isFree, tks, target_time, dtime

  if isFree:
    tks += 10
    dtime = timedelta(0, 0, 0, 0, 1)
    target_time = datetime.now() + dtime
    bot.send_message(msg.chat.id, "Вы получили 10 бесплатных запросов.")
    bot.send_message(msg.chat.id, "Ваших токенов: " + str(tks))
    isFree = False
  elif str(target_time - datetime.now())[0] == '-':
    bot.send_message(msg.chat.id, 'Вы получили 10 бесплатных запросов.')
    tks += 10
    dtime = timedelta(0, 0, 0, 0, 1)
    target_time = datetime.now() + dtime
    bot.send_message(msg.chat.id, "Бонус через " + str(target_time - datetime.now()).split('.')[0])
    bot.send_message(msg.chat.id, "Ваших токенов: " + str(tks))
  else:
    bot.send_message(msg.chat.id, "Бонус через " + str(target_time - datetime.now()).split('.')[0])
    bot.send_message(msg.chat.id, "Ваших токенов: " + str(tks))

@bot.message_handler(func = lambda msg: msg.text == 'Купить подписку')
def tokens(msg):
  a = types.InlineKeyboardMarkup(row_width=1)
  button1 = types.InlineKeyboardButton('1 день: 29 руб.', callback_data="0")
  button3 = types.InlineKeyboardButton('3 дня: 79 руб.', callback_data="1")
  button7 = types.InlineKeyboardButton('7 дней: 149 руб.', callback_data="2")
  a.add(button1, button3, button7)
  bot.send_message(msg.chat.id, 'Выберите подписку', reply_markup=a)

@bot.callback_query_handler(func = lambda call: call.data in ["0", "1", "2"])
def subcall(call):
  if call.data == "0":
    payment2.price = 29
    print("нажал 29")
    #payment2.payment()
    bot.send_message(call.message.chat.id, str(payment2.payment()) + "Оплата киви, либо через админа @totaljerkface\n")

@bot.message_handler(func=lambda msg: msg.text not in [None, 'Токены'])
def echo_all(message):

  global isReq

  if isReq:
    bot.send_message(message.chat.id, chatgpt.returnPrompt(message.text))
    # isReq = False
  else:
    bot.send_message(message.chat.id, "Заплатите")

# Polling
bot.polling()


