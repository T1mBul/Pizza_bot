from aiogram.utils import executor
from create_bot import dp
from handlers import client, others, admin
from db import sqlite_db


async def on_startup(_):
    print('Бот онлайн')
    sqlite_db.sql_start()

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
others.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
