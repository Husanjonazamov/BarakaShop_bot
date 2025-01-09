from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.env import WEBAPP_URL
from utils.env import BOT_TOKEN
import requests

COLLABORATION = "Hamkorlik"
FEEDBACK = "Fikr bildirish"
MYORDER = "Buyurtmalarim"
MYPROFILE = "Shaxsiy Ma'lumotlarim"
ABOUT = "Bot haqida ma'lumot"


def send_menu_with_webapp(user_id):
    menu = {
        "keyboard": [
            [{"text": COLLABORATION}], 
            [{"text": FEEDBACK}, {"text": MYPROFILE}],
            [{"text": MYORDER}, {"text": ABOUT}],
        ],
        "resize_keyboard": True,
        "one_time_keyboard": True 
    }
    
    return menu


def send_webapp_start(user_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    message = {
        "chat_id": user_id,
        "text": f"Bozorga kirish",
        "reply_markup": {
            "inline_keyboard": [
                [{
                    "text": "Bozor",
                    "web_app": {
                        "url": f"https://front.azamovdev.uz/?user_id={user_id}"
                    }
                }]
            ]
        }
    }
    response = requests.post(url, json=message)
    if response.status_code == 200:
        print("WebApp boshlash uchun xabar yuborildi!")
    else:
        print(f"Xatolik yuz berdi: {response.status_code}, {response.text}")



def send_webapp_texts(user_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    message = {
        "chat_id": user_id,
        "text": text,
        "reply_markup": {
            "inline_keyboard": [
                [{
                    "text": "Bozor",
                    "web_app": {
                        "url": f"https://front.azamovdev.uz/?user_id={user_id}"
                    }
                }]
            ]
        }
    }
    response = requests.post(url, json=message)
    if response.status_code == 200:
        print("WebApp boshlash uchun xabar yuborildi!")
    else:
        print(f"Xatolik yuz berdi: {response.status_code}, {response.text}")




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

