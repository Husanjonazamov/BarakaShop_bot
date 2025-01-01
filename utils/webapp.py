# utils/webapp.py

import requests
from utils.env import BOT_TOKEN 

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/setChatMenuButton"

def set_webapp_button(webapp_url):
    menu_button = {
        "type": "web_app",
        "text": "Bozor",
        "web_app": {
            "url": webapp_url
        }
    }

    response = requests.post(API_URL, json={"menu_button": menu_button})

    if response.status_code == 200:
        print("MenuButtonWebApp muvaffaqiyatli o'rnatildi!")
    else:
        print(f"Xato: {response.status_code}, {response.text}")
        
    return response.json()
