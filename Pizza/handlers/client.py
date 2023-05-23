from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from db import sqlite_db

async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита! Спасибо за выбор нашей пиццерии!',
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через личные сообщения, напишите ему:'
                            ' \nhttps://t.me/Pizza_HutSpbBot')


async def pizza_opentime_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 10:00 до 00:00; Сб-Вс Круглосуточно')


async def pizza_adress_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'г. Санкт-Петербург, ул. Дыбенко, д. 20')

async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_opentime_command, commands='Режим_работы')
    dp.register_message_handler(pizza_adress_command, commands='Локация')
    dp.register_message_handler(pizza_menu_command, commands='Меню')
