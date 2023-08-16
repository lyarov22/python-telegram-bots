import telebot
from bs import first_new, last_new

hello = '''
        ✋Привет, я TechnoNews🦾
        Команды:
        привет
        новости
        понос дамиры
        пока
        '''

bot = telebot.TeleBot('5218192949:AAFog_tpFeCz-YcU-gNItv_ZIeYg2nB_lf8')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "привет":
        bot.send_message(message.from_user.id, hello)

    elif message.text == "новости":
        bot.send_message(message.from_user.id, first_new() + '\n' + last_new())

    elif message.text == "понос дамиры":
        bot.send_message(message.from_user.id, '[Понос Дамиры 2.0](https://chesschampion.kz/upload/global/untitled%20folder/Burabay/asylhan.jpg)', parse_mode='Markdown')

    elif message.text == "пока":
        bot.send_message(message.from_user.id, "понос")

bot.polling(none_stop=True, interval=0)
