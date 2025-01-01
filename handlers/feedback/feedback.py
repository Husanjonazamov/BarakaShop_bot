# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from states.state import Feedback
from utils.env import GROUP_ID



@dp.message_handler(content_types=['text'], state=Feedback.feedback)
async def feedback(message: Message, state: FSMContext):

    feedback = message.text
    username = message.from_user.username
    
    await state.update_data({'feedback': feedback})
    
    await bot.send_message(
        chat_id=GROUP_ID,
        text=texts.send_feedback(
            username=username,
            feedback=feedback
        )
    )
    
    await message.answer(texts.FEEDBACK_SUCCESS, reply_markup=buttons.MENU)
    
    await state.finish()