# handlers/start.py
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp
from utils import texts, buttons
from .start import start_handler


@dp.message_handler(lambda message: message.text.startswith(buttons.BASE_BACK_TEXT), state='*')
async def back_handler(message: Message, state: FSMContext):
    """
    Botning asosiy back (ortga) funksiyasi.
    """
    await start_handler(message, state)


