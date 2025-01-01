# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from states.state import Register
from handlers.menu import Menu
from services import createUser
from utils import texts

# add import
import re


@dp.message_handler(content_types=['contact', 'text'], state=Register.phone)
async def name(message: Message, state: FSMContext):
    
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text

    if not re.match(r'^\+?\d+$', phone): 
        await message.answer(texts.ERROR_PHONE)
        return  


    await state.update_data({'phone': phone})
    data = await state.get_data()
    user_id = message.from_user.id
    name = data.get('name')
    
    user = {
        'user_id': user_id,
        'name': name,
        'phone': phone
    }
    
    createUser(user)
    
    await Menu(message, state)