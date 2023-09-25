import telebot
import chatgpt
while True:
  try:
    bot = telebot.TeleBot("5904516415:AAHL21ImS5Acnnm-lfBhRvjyy1my80y5cUk")
  # Create a handler
    @bot.message_handler(commands=['start'])
    def start(message):
      sent = bot.send_message(message.chat.id, 'Hello, what can I do for you?')

    @bot.message_handler(func=lambda msg: msg.text is not None)
    def echo_all(message):
        bot.send_message(message.chat.id, chatgpt.returnPrompt(message.text))

    # Polling
    bot.polling()

  except Exception:
    print("error")

