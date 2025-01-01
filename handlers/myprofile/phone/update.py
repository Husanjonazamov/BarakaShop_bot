# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import PhoneChange
from services import putPhone
from handlers.myprofile.handler import myprofile_handler
from asyncio import create_task


async def phoneChange_task(message: Message, state: FSMContext):

    phone = message.text
    user_id = message.from_user.id
    
    await state.update_data({
        'phone': phone
    })    
    
    putPhone(user_id, phone)
    
    await message.answer(texts.SUCCESS_PROFILE)
    await myprofile_handler(message, state)
    
    
@dp.message_handler(content_types=['text'], state=PhoneChange.phone)
async def phoneChange(message: Message, state: FSMContext):
    if message.text in [buttons.BACK_TEXT]:
        await myprofile_handler(message, state)
    else:
        await create_task(phoneChange_task(message, state)) 
    