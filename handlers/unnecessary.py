# aiogram import
from aiogram.types import Message

from loader import dp
from utils import texts, buttons


@dp.message_handler(content_types=['text'])
async def untext(message: Message):
    text = texts.UNTEXT
    user_id = message.from_user.id
    buttons.send_webapp_texts(user_id, text)