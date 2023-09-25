import telebot
import requests

from SimpleQIWI import *
from time import sleep

import chatgpt



token = "ab20ab34e9d2e8171fc39743be85adb1"         # https://qiwi.com/api
phone = "+77715724631"

version = "3"

api = QApi(token=token, phone=phone)

#398 - KZT 840 - USD 978 - EUR 643 - RUB

# Курс пары валют (коды валют в String)
def currency(api_access_token, currency_to, currency_from):
    s = requests.Session()
    s.headers = {'content-type': 'application/json'}
    s.headers['authorization'] = 'Bearer ' + api_access_token
    s.headers['User-Agent'] = 'Android v3.2.0 MKT'
    s.headers['Accept'] = 'application/json'
    res = s.get('https://edge.qiwi.com/sinap/crossRates')

    # все курсы
    rates = res.json()['result']
    
    # запрошенный курс
    rate = [x for x in rates if x['from'] == currency_from and x['to'] == currency_to]
    if (len(rate) == 0):
        print('No rate for this currencies!')
        return
    else:
        return rate[0]['rate']

# Конвертация в QIWI Кошельке (currency - код валюты String)
def exchange(api_access_token, sum_exchange, currency, to_qw):
    s = requests.Session()
    
    currencies = ['398', '840', '978'] #, '643']
    
    if currency not in currencies:
      print('This currency not available')
      return
    
    s.headers = {'content-type': 'application/json'}
    s.headers['authorization'] = 'Bearer ' + api_access_token
    s.headers['User-Agent'] = 'Android v3.2.0 MKT'
    s.headers['Accept'] = 'application/json'
    postjson = {"id":"","sum":{"amount":"","currency":""},"paymentMethod":{"type":"Account","accountId":"643"}, "comment":"'+comment+'","fields":{"account":""}}
    postjson['id'] = str(int(time.time() * 1000))
    postjson['sum']['amount'] = sum_exchange
    postjson['sum']['currency'] = currency
    postjson['fields']['account'] = to_qw
    res = s.post('https://edge.qiwi.com/sinap/api/v2/terms/1099/payments',json = postjson)
    return res.json()

def debug():
    info = ("Бот платёжка версия %s \n" % version)
  
    balances = ("На счету %s \n %s рублей \n %s тенге \n %s долларов \n %s евро \n"
    %(phone, api.balance[0], api.balance[1], api.balance[2], api.balance[3]))

    currencies = ("RUB/KZT %s \nKZT/RUB %s \n"
    % (str(currency(token, '643', '398')), str(currency(token, '398', '643'))))

    #print(info)
    #print(balances)
    #print(currencies)

    return info, balances, currencies
    

    

    


#ali - 1345303475 ali2 - 5509301823 ilya - 634826649 mitya - 5045372299 

users = ['1345303475', '5509301823', '634826649']#, '5045372299']

status = "Статус"
user = "user"

def pay():
    if (user in users):
        status += "Вы уже в списке. Введите /request" 
        #print(status)
        #validation()
        return True
        
    if (api.balance[0] > 10):

        #status = "Доступ открыт для пользователя %s" % user
        #print(status)
        #узнать курс чтобы перевести один рубль
        #kurs = currency(token, '643', '398')
        #СДЕЛАТЬ ЧТОБЫ ОН СПИСЫВАЛ ВСЁ ДЕЛИТЬ И СРАВНИВАТЬ
        #опорожнение баланса 
        #exchange(token, kurs, '398', '+77715724631')
        return True

    else:
        status = "Ожидание платежа"
        #print(status)
        return


if (pay() == True):
    status = "Доступ открыт для пользователя %s. Введите /request" % user



def validation():
    
    if user not in users:
        status = "Нет доступа"
        #print(status)
        
        return False

    status = "Сеанс начат"
    #print(status)

    #вызов основного тела бота
    
    return True

#pay()

#print("БД - ", users)
#print("ОБновить")

#debug()
#validation()


api.start()


#tg.py

bot = telebot.TeleBot('5668039202:AAGmWWnHdgdynOvbqCO7PzHXVXHT1_tJqvw')

user = ''
free = 3

start_text = "Привет, это бот который даёт доступ к нейросети GPT-3 от Open AI. \nОтправь /menu чтобы узнать все команды."
menu_text = "Попробовать - /free \nКупить подписку - /pay \nПроверка покупки - /valid \nОтладка: /debug \nЗапрос: /request"
free_text = "Вам доступно %i запросов" % (free)
pay_text = ("Меню оплаты \nПосле оплаты запустите ещё раз! \n Статус: %s" % status)
#valid_text = 
#debug_text = 
request_text = ("Статус: %s" % (status))

@bot.message_handler(commands=['start'])
def send_welcome(msg):
    CMD_HELP = start_text
    bot.reply_to(msg, CMD_HELP)

@bot.message_handler(commands=['menu'])
def send_menu(msg):
    CMD_MENU = menu_text
    bot.reply_to(msg, CMD_MENU)

@bot.message_handler(commands=['free'])
def send_free(msg):
    CMD_FREE = free_text
    bot.reply_to(msg, CMD_FREE)

@bot.message_handler(commands=['pay'])
def send_pay(msg):
    pay()
    CMD_PAY = pay_text
    bot.reply_to(msg, CMD_PAY)

@bot.message_handler(commands=['valid'])
def send_valid(msg):
    validation()
    #user = msg.chat.id
    CMD_VALID = ("Ваш айди: %i \nСтатус: %s" % (user, status))
    bot.reply_to(msg, CMD_VALID)

@bot.message_handler(commands=['debug'])
def send_debug(msg):
    debug()
    user = msg.chat.id
    info, balances, currencies = debug()
    CMD_DEBUG = (info + '\n' + balances + '\n' + currencies)
    bot.reply_to(msg, CMD_DEBUG)


@bot.message_handler(commands=['request'])
def send_request(msg):

    CMD_REQUEST = request_text
    bot.reply_to(msg, CMD_REQUEST)

if (pay() == True or free == 0):
        @bot.message_handler(func=lambda msg: msg.text is not None)
        def echo_all(message):
            bot.send_message(message.chat.id, chatgpt.returnPrompt(message.text))
            if (pay() == False):
                bot.send_message(message.chat.id, ("Осталось: %i запросов" % free))
                free -= 1

bot.polling()