from aiogram import executor
from loader import bot, dp
from utils.env import ADMIN

import handlers


async def on_startup(dp):
    """
    Botni ishga tushiradi
    """
    await bot.send_message(ADMIN, 'Bot ishga tushdi')


executor.start_polling(dp, on_startup=on_startup, skip_updates=True)