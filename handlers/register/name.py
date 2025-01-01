# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import Register




@dp.message_handler(content_types=['text'], state=Register.name)
async def name(message: Message, state: FSMContext):
    
    name = message.text
    
    await state.update_data({
        'name': name
    })
    
    await message.answer(texts.REGISTER_PHONE, reply_markup=buttons.REGISTER_PHONE)
    
    await Register.phone.set()