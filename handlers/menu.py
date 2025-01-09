# aiogram import
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

# kode import
from loader import dp, bot
from utils.webapp import set_webapp_button 
from utils.env import WEBAPP_URL
from utils import texts, buttons
from utils.buttons import send_menu_with_webapp
from services import getUser


async def Menu(message: Message, state: FSMContext):
    """
    Botning asosiy /start funksiyasi.
    """
    
    user_id = message.from_user.id
    user = getUser(user_id)
    
    
    text = texts.MENU.format(message.from_user.first_name)
    
    # set_webapp_button(WEBAPP_URL)
    await message.answer(
        text=text,
        reply_markup=send_menu_with_webapp(user_id)
    )
    text = texts.UNTEXT
    buttons.send_webapp_texts(user_id, text)

    await state.finish()
