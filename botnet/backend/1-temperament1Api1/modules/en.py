from telebot import types

def ruButtons():
	markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
	buttonFree = types.KeyboardButton('Tokens')
	buttonSubscribe = types.KeyboardButton('Subscribe')
	buttonMenu = types.KeyboardButton('Menu')
	buttonValid = types.KeyboardButton('Check')
	buttonReq = types.KeyboardButton('New requests')
	markup.add(buttonFree, buttonSubscribe, buttonMenu, buttonValid, buttonReq)
	return markup