# aiogram import
from aiogram.types import Message

from loader import dp
from utils import texts


@dp.message_handler(content_types=['text'])
async def untext(message: Message):
    await message.answer(texts.UNTEXT)