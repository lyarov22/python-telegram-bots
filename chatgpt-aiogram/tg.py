from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling
import requests

API_TOKEN = '5886817050:AAGJvm9PwNx0fs_e7Lf-cJ9kbvCSSf_TeLk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'restart'])
async def start(message: types.Message):
    await message.reply('Hey! I am a chatbot. Lets start a conversation.')
    await message.reply('Please say something')

# End current conversation
@dp.message_handler(commands=['stop'])
async def stop_command(message: types.Message):
    await message.reply('OK, conversation ended. You can type /start or /restart to start a new conversation.')

# Handler for the text messages
@dp.message_handler(content_types=['text'])
async def process_message(message: types.Message):
    # Send request to chat gpt API
    response = requests.get('http://chatgpt.com/api', params={
        'message': message.text
    }).json()
    # Print the response
    await message.reply(response['text'])

# Execute the program
if __name__ == '__main__':
    start_polling(dp, skip_updates=True)