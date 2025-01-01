# aiogram import
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

# kode import
from loader import dp
from utils import texts, buttons
from services import getUser
from states.state import Register
from .menu import Menu

@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    """
    Botning asosiy /start funksiyasi.
    """
    
    user_id = message.from_user.id
    user = getUser(user_id)
    
    if not user:
        await message.answer(texts.REGISTER_FULLNAME)
        await Register.name.set()
    else:   
        await Menu(message, state)
