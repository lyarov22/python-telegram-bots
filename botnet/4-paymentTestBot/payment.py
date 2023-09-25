from SimpleQIWI import *
from time import sleep
import time
import requests

from tg import user, CMD_DEBUG

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

    

    

    


#ali - 1345303475 ali2 - 5509301823 ilya - 634826649 mitya - 5045372299 

users = ['1345303475', '5509301823', '634826649', '5045372299']

status = "statusPONOSS"

def pay():
    if (user in users):
        status = "Вы уже в списке"
        print(status)

        #validation()

        return
        
    if (api.balance[0] < 10):
        
        #Проверка на то, есть ли уже в базе юзер
        if (user not in users):
                users.append(user)
                
                #запуск основного тела бота
                validation()
        
        status = "Доступ открыт для пользователя %s" % user
        print(status)
        
        #узнать курс чтобы перевести один рубль
        #kurs = currency(token, '643', '398')

        #СДЕЛАТЬ ЧТОБЫ ОН СПИСЫВАЛ ВСЁ ДЕЛИТЬ И СРАВНИВАТЬ
        
        #опорожнение баланса 
        #exchange(token, kurs, '398', '+77715724631')
        
        return True

    else:
        status = "Ожидание платежа"
        print(status)

        return

def validation():
    
    if user not in users:
        status = "Нет доступа"
        print(status)
        
        return False

    status = "Сеанс начат"
    print(status)

    #вызов основного тела бота
    
    return True

#pay()

print("БД - ", users)

print("ОБновить")
#debug()
#validation()


api.start()
