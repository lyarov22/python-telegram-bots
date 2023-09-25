import telebot
import chatgpt

from qiwip2py import QiwiP2P
from datetime import timedelta

SECRET_KEY = "ab20ab34e9d2e8171fc39743be85adb1"
qiwi_p2p = QiwiP2P(secret_key=SECRET_KEY)
bill = qiwi_p2p.create_bill(bill_id='test', amount=1.99, custom_fields={'themeCode': THEME_CODE},
                            expiration_datetime=timedelta(hours=3))
print(bill.pay_url)

# и если требуется ссылка на форму, а не создание счёта через API

qiwi_p2p = QiwiP2P(public_key=PUBLIC_KEY)
bill = qiwi_p2p.create_bill(bill_id='test2', amount=1.99, custom_fields={'themeCode': THEME_CODE},
                            expiration_datetime=timedelta(hours=3), success_url='http://random.cat',
                            return_pay_link=True)
print(bill)

bot = telebot.TeleBot("5966015529:AAEWVcmoC8KhJ8MS0S7TdXuOsits93LSPPQ")

# Create a handler
@bot.message_handler(commands=['start'])
def start(message):
  sent = bot.send_message(message.chat.id, 'Hello, what can I do for you?')

@bot.message_handler(func=lambda msg: msg.text is not None)
def echo_all(message):
     bot.send_message(message.chat.id, chatgpt.returnPrompt(message.text))

# Polling
bot.polling()