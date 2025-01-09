# handlers/start.py
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

# kode import
from loader import dp
from utils import texts, buttons
from services import getAbout

@dp.message_handler(lambda message: message.text.startswith(buttons.ABOUT), state='*')
async def back_handler(message: Message, state: FSMContext):

    about = getAbout()
    if about.get('status') and about.get('data'):
        description = about['data'][0].get('description')
        print(description)
    else:
        print("Description mavjud emas")
    
    
    await message.answer(description, reply_markup=buttons.MAIN_BACK)
    user_id = message.from_user.id
    buttons.send_webapp_texts(user_id, description)
