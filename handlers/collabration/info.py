# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from states.state import Collobration
from utils.env import ADMIN

from asyncio import create_task


async def info_task(message: Message, state: FSMContext):

    username = message.from_user.username or message.from_user.first_name

    data = await state.get_data()
    name = data.get('name')
    phone = data.get('phone')
    location = data.get('location')

    info = message.text
    await state.update_data({'info': info})
    
    caption = texts.collaboration(
        name=name,
        phone=phone,
        username=username,
        location=location,
        info=info
    )
    
    await bot.send_message(
        chat_id=ADMIN,
        text=caption
    )
    
    await message.answer(texts.SUCCESS_COLLABORATION, reply_markup=buttons.MAIN_BACK)
    user_id = message.from_user.id
    text = texts.UNTEXT
    buttons.send_webapp_texts(user_id, text)
    await state.finish()
    
    
    
@dp.message_handler(content_types=['text'], state=Collobration.info)
async def info(message: Message, state: FSMContext):
    if message.text in [buttons.BACK_TEXT]:
        await message.answer(texts.LOCATION, reply_markup=buttons.BACK)
        await Collobration.location.set()
    else:
        await create_task(info_task(message, state))