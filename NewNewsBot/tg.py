import aiogram
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, Message, ContentType
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import feedparser
import time

bot = Bot(token='')
dp = Dispatcher(bot)

feeds = ['https://www.ixbt.com/export/news.rss', 'Ixbt',
'https://habr.com/ru/rss/hubs/', 'Habr', 
'https://vc.ru/rss', 'VC.ru',
'https://3dnews.ru/breaking/rss/', '3DNews',
'https://doc.cnews.ru/inc/rss/news_top.xml', 'CNews',
'https://tproger.ru/feed/', 'TProger']

# Создаем кнопки с текстом
button1 = KeyboardButton(feeds[1])
button2 = KeyboardButton(feeds[3])
button3 = KeyboardButton(feeds[5])
button4 = KeyboardButton(feeds[7])
button5 = KeyboardButton(feeds[9])
button6 = KeyboardButton(feeds[11])

# Собираем все кнопки в один массив
keyboard = ReplyKeyboardMarkup([[button1, button2],[button3, button4], [button5, button6]])

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Привет! Выбери одну из кнопок", reply_markup=keyboard)

answer = 'ponos'

def parser(n):
    answer = 'Новости на %s\n' % (time.strftime("%H:%M:%S %d.%m.%Y"))
    rss_url = feeds[n]
    i = 0
    feed = feedparser.parse(rss_url)
 
    for post in feed.entries:
        i += 1
        if i == 16:
            break
        answer += (f"{i}. {post.title}\n{post.link}\n\n")  
    return answer

@dp.message_handler()
async def handle_message(message: Message):
    if message.text == feeds[1]:
        rss_url = 'https://www.ixbt.com/export/news.rss'
        feed = feedparser.parse(rss_url)

        for post in feed.entries:
            await message.answer(f"{post.title}\n{post.link}")
        

    elif message.text == feeds[3]:
        await message.answer(parser(2))

    elif message.text == feeds[5]:
        if message.text == feeds[1]:
            rss_url = 'https://vc.ru/rss'
            feed = feedparser.parse(rss_url)

            for post in feed.entries:
               await message.answer(f"{post.title}\n{post.link}")

    elif message.text == feeds[7]:
        await message.answer(parser(6))

    elif message.text == feeds[9]:
        await message.answer(parser(8))

    elif message.text == feeds[11]:
        await message.answer(parser(10))

if __name__ == '__main__':
    executor.start_polling(dp)
