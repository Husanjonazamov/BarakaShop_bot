# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import PhoneChange




@dp.message_handler(lambda message: message.text.startswith(buttons.CHANGE_PHONE), state='*')
async def name_handler(message: Message, state: FSMContext):
    """
    foydalanuvchining profiledagi ismini o'zgartirish funksiyasi 
    """
    
    await message.answer(texts.PHONECHANGE, reply_markup=buttons.BACK)
    
    await PhoneChange.phone.set()
    
    
