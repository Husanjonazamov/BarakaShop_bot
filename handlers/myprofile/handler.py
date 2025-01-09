# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from services import getUser


@dp.message_handler(lambda message: message.text.startswith(buttons.MYPROFILE), state='*')
async def myprofile_handler(message: Message, state: FSMContext):
    """
    foydalanuvchining profiledagi malumotlarni korish funksiyasi    
    """
    
    user_id = message.from_user.id
    user = getUser(user_id)
    
    name = user['name']
    phone = user['phone']
    
    await message.answer(
        text=texts.myProfile(
            name=name,
            phone=phone
        ),
        reply_markup=buttons.MYPROFILE_SETTINGS
    )
    user_id = message.from_user.id
    text = texts.UNTEXT
    buttons.send_webapp_texts(user_id, text)
    
