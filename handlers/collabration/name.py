# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import Collobration

from asyncio import create_task


async def name_task(message: Message, state: FSMContext):
    
    name = message.text
    print(name)
    
    await state.update_data({
        'name': name
    })
    
    await message.answer(texts.PHONE, reply_markup=buttons.BACK)
    await Collobration.phone.set()
    
    
    
@dp.message_handler(content_types=['text'], state=Collobration.name)
async def name(message: Message, state: FSMContext):
    await create_task(name_task(message, state))