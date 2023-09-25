import re
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os, logging

from downloader import download_tiktok_video

logging.basicConfig(level=logging.INFO)

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

hosting_list = ['TikTok', 'Instagram Reels', 'YouTube Shorts', 'YouTube',]

# Создаем экземпляр бота и диспетчера
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(
    '''Hi, I'm a bot that downloads videos from popular video hosting sites.\n\nSend me a link to the video and I'll figure out what to download\n\nList of hosting services: /list''')

@dp.message_handler(commands=['list'])
async def list_command(message: types.Message):
    # Формируем строку с перечислением хостинг-сервисов
    hosting_string = "List of hosting services:\n\n"
    for service in hosting_list:
        hosting_string += f"- {service}\n"
    await message.reply(hosting_string)

# Обработка текстовых сообщений
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_text(message: types.Message):
    text = message.text
    chat_id = message.chat.id

    # Проверка ссылки на TikTok
    if re.search(r'(?:https?://)?(?:www\.)?vm\.tiktok\.com/', text):
        await message.reply("Скачиваю видео...")

        try:
            video_url = await download_tiktok_video(text)
            if video_url:
                await bot.send_video(message.chat.id, video_url)
            else:
                await message.reply("Не удалось получить ссылку на видео.")
        except Exception as e:
            await message.reply(f"Ошибка при скачивании видео: {str(e)}")

    # Проверка ссылок на Instagram Reels
    elif re.search(r'(?:https?://)?(?:www\.)?instagram\.com/reel/', text):
        await message.reply("Instagram Reels")

    # Проверка ссылок на YouTube Shorts
    elif re.search(r'(?:https?://)?(?:www\.)?youtube\.com/shorts/', text):
        await message.reply("YouTube Shorts")

    # Проверка ссылок на обычные видео YouTube
    elif re.search(r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[\w-]+', text):
        await message.reply("Обычное видео YouTube")

    else:
        await message.reply("Неизвестная ссылка")

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
