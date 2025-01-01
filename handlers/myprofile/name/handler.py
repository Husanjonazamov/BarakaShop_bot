# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import NameChange




@dp.message_handler(lambda message: message.text.startswith(buttons.CHANGE_NAME), state='*')
async def name_handler(message: Message, state: FSMContext):
    """
    foydalanuvchining profiledagi ismini o'zgartirish funksiyasi 
    """
    
    await message.answer(texts.NAMECHANGE, reply_markup=buttons.BACK)
    
    await NameChange.name.set()
    
    
