# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import Collobration




@dp.message_handler(lambda message: message.text.startswith(buttons.COLLABORATION))
async def collabration(message: Message, state: FSMContext):
    
    await message.answer(texts.NAME, reply_markup=buttons.MAIN_BACK)
    await Collobration.name.set()