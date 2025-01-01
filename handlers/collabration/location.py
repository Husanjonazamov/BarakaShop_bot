# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import Collobration

from asyncio import create_task


async def location_task(message: Message, state: FSMContext):
    
    location = message.text
    
    await state.update_data({
        'location': location
    })
    
    await message.answer(texts.INFO, reply_markup=buttons.BACK)
    await Collobration.info.set()
    
    
    
@dp.message_handler(content_types=['text'], state=Collobration.location)
async def location(message: Message, state: FSMContext):
    if message.text in [buttons.BACK_TEXT]:
        await message.answer(texts.PHONE, reply_markup=buttons.BACK)
        await Collobration.phone.set()
    else:
        await create_task(location_task(message, state))