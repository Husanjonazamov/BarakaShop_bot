# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import Collobration

from asyncio import create_task


async def phone_task(message: Message, state: FSMContext):
    
    phone = message.text
    
    await state.update_data({
        'phone': phone
    })
    
    await message.answer(texts.LOCATION, reply_markup=buttons.BACK)
    await Collobration.location.set()
    
    
    
@dp.message_handler(content_types=['text'], state=Collobration.phone)
async def phone(message: Message, state: FSMContext):
    if message.text in [buttons.BACK_TEXT]:
        await message.answer(texts.NAME, reply_markup=buttons.MAIN_BACK)
        await Collobration.name.set()
    else:
        await create_task(phone_task(message, state))