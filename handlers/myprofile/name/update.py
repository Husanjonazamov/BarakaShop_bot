# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import NameChange
from services import putName
from handlers.myprofile.handler import myprofile_handler

from asyncio import create_task


async def nameChange_task(message: Message, state: FSMContext):
    name = message.text
    user_id = message.from_user.id
    
    await state.update_data({
        'name': name
    })    

    putName(user_id, name)
    
    await message.answer(texts.SUCCESS_PROFILE)
    await myprofile_handler(message, state)
        
    
    
@dp.message_handler(content_types=['text'], state=NameChange.name)
async def nameChange(message: Message, state: FSMContext):
    if message.text in [buttons.BACK_TEXT]:
        await myprofile_handler(message, state)
    else:
        await create_task(nameChange_task(message, state))
