from telebot import types

def ruButtons():
	markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
	buttonFree = types.KeyboardButton('Токены')
	buttonSubscribe = types.KeyboardButton('Купить подписку')
	buttonMenu = types.KeyboardButton('Меню')
	buttonValid = types.KeyboardButton('Проверка')
	buttonReq = types.KeyboardButton('Новый запрос')
	markup.add(buttonFree, buttonSubscribe, buttonMenu, buttonValid, buttonReq)
	return markup