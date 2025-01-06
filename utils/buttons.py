from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


COLLABORATION = "🤝 Hamkorlik"
FEEDBACK = "💬 Fikr bildirish"
MYORDER = "🛒 Buyurtmalarim"
MYPROFILE = "👤 Shaxsiy Ma'lumotlarim"
ABOUT = "🤖 Bot haqida ma'lumot"


MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=COLLABORATION)
        ],
        [
            KeyboardButton(text=FEEDBACK),
            KeyboardButton(text=MYORDER),
        ],
        [
            KeyboardButton(text=MYPROFILE),
            KeyboardButton(text=ABOUT),
        ],
    ],
    resize_keyboard=True
)



BASE_BACK_TEXT = '🔙 Ortga'
BACK_TEXT = '⬅️ Ortga'


BACK = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BACK_TEXT)
        ]
    ],
    resize_keyboard=True
)




MAIN_BACK = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BASE_BACK_TEXT)
        ]
    ],
    resize_keyboard=True
)


REGISTER_PHONE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📲 Yuborish', request_contact=True)
        ]
    ],
    resize_keyboard=True
)


CHANGE_NAME = "Ismni o'zgartirish ✏️"
CHANGE_PHONE = "Telefon raqamni o'zgartirish 📱"


MYPROFILE_SETTINGS = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=CHANGE_NAME),
            KeyboardButton(text=CHANGE_PHONE),
        ],
        [
            KeyboardButton(text=BASE_BACK_TEXT)
        ]
    ],
    resize_keyboard=True
)

