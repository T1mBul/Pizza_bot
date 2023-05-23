from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_1 = KeyboardButton('/Режим_работы')
kb_2 = KeyboardButton('/Локация')
kb_3 = KeyboardButton('/Меню')
kb_4 = KeyboardButton('Поделиться номером телефона', request_contact=True)
kb_5 = KeyboardButton('Отправить геолокацию', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(kb_1, kb_2, kb_3).add(kb_4).add(kb_5)
