# aiogram import
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

# kode import
from loader import dp
from utils.webapp import set_webapp_button 
from utils.env import WEBAPP_URL
from utils import texts, buttons
from services import getUser


async def Menu(message: Message, state: FSMContext):
    """
    Botning asosiy /start funksiyasi.
    """
    
    user_id = message.from_user.id
    user = getUser(user_id)
    
    set_webapp_button(WEBAPP_URL)
    await message.answer(texts.MENU.format(message.from_user.first_name), reply_markup=buttons.MENU)

    await state.finish()
