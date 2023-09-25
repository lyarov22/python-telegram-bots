from SimpleQIWI import *
from time import sleep

import asyncio


token = "ab20ab34e9d2e8171fc39743be85adb1"  # https://qiwi.com/api
phone = "+77715724631"

api = QApi(token=token, phone=phone)

price = 0

period = '00:00:00'



# Добавляем пользователя
def save_user(user):
    user = user + period
    with open('users.txt', 'a') as user_file:
        user_file.write(user + '\n')

# Проверяем наличие в базе
def check_user(user):
    with open('users.txt') as users_file:
        for line in users_file:
            if line == user + '\n':
                return True
        return False

# Проверяем не истекло ли время
async def check_full():
    while True:
        if period == '00:00:00':
            isFull = False
            return False
        else:
            await asyncio.sleep(3600)

user = 'ali' # Получение id пользователя

# Принимаем платежи
isPay = False   # Проверка оплаты
isFull = False  # Проверка доступа
status = ""     # Инициализация статуса для вывода

# Если оплатил - сохраняем в базу
if (isPay == True):
    save_user(user)
    isPay = False
    



if (isFull == True):
    # Даём доступ к GPT-3
    pass

elif (isFull == False):
    # Забираем доступ к GPT-3
    pass

async def check_full():
    while True:
        # Если есть в базе - даём доступ
        if (check_user(user) == True):
            status = "Доступ предоставлен"
            print(status)
            isFull = True

        # Если нет в базе - забираем доступ
        elif (check_user(user) == False):
            status = "Доступ закрыт"
            print(status)
            isFull = False

        else:
            await asyncio.sleep(60) # В секундах


sub = '00:00:00'

is1d = False # 1d = 29 rub
is3d = False # 3d = 79 rub
is7d = False # 7d = 149 rub

def isDay():
    if (is1d == True):
        price = 29 
        is1d = False

    elif (is3d == True): 
        price = 79
        is3d = False

    elif (is7d == True):
        price = 149
        isd = False


price = 1                   # Минимальное значение при котором счет будет считаться закрытым
comment = api.bill(price)   # Создаем счет. Комментарий с которым должен быть платеж генерируется автоматически, но его можно задать                                 # параметром comment. Валютой по умолчанию считаются рубли, но ее можно изменить параметром currency

status = ("Переведите %i рублей на счет %s с комментарием '%s'" % (price, phone, comment))
print(status)

api.start()                 # Начинаем прием платежей

while (True and isPay == False):
    if api.check(comment):  # Проверяем статус
        status = "Платёж получен! Доступ предоставлен."
        print(status)
        isPay = True
        break
    
    sleep(1)

api.stop()                  # Останавливаем прием платежей