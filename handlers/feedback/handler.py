# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from states.state import Feedback





@dp.message_handler(lambda message: message.text.startswith(buttons.FEEDBACK), state='*')
async def feedback_handler(message: Message, state: FSMContext):
    """
    asosiy fikr bildirish handlari
    """
    
    await message.answer(texts.FEEDBACK_HANDLER, reply_markup=buttons.MAIN_BACK)
    
    await Feedback.feedback.set()