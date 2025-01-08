REGISTER_FULLNAME = \
"""
<b>
Ismingizni kiriting!
</b>
"""

REGISTER_PHONE = \
"""
Telefon raqamingizni kiriting yoki pasdagi <b>Yuborish Tugmasini bosing</b>!
"""


ERROR_PHONE = \
"""
<b>
Iltimos, faqat raqam kiriting
</b>
"""

NAMECHANGE = \
"""
<b>
Ismingizni kiriting!
</b>
"""

PHONECHANGE = \
"""
<B>Telefon raqamingizni kiriting</b>!
"""

SUCCESS_PROFILE = \
"""
<b>
✅ Ma'lumot muvaffaqiyatli o'zgartirildi!
</b>
"""



MENU = \
"""
<b>
Assalomu alaykum {}!
</b>
"""



FEEDBACK_HANDLER = \
"""
<b>
Bu bo'lim orqali siz adminga xabar yuborishingiz va shikoyatingizni qoldirishingiz mumkin.
Fikringizni kiriting!
</b>
"""


MAIN_BACK = \
"""
<b>
🏠 Asosiy Menyu
</b>
"""


FEEDBACK_SUCCESS = \
"""
<b>Sizning fikringiz adminga yuborildi ✅</b>
"""






def send_feedback(**kwargs):
    feedback = ''
    
    feedback += f"<b>Yangi fikr:</b>\n\n"
    feedback += f"<b>Foydalanuvchi: @{kwargs['username']}</b>\n"
    feedback += f"<b>Fikr: {kwargs['feedback']}</b>\n"
    
    return feedback
    
    
def myProfile(**kwargs):
    profile = ''
    
    profile += f"👤 Mening Malumotlarim!\n\n"
    profile += f"📝 Ism: {kwargs['name']}\n\n"
    profile += f"📱 Telefon raqam: {kwargs['phone']}"
    
    return profile


# colobration

NAME = \
"""
Hamkorlik uchun ismingizni kiriting! ✨
"""

PHONE = \
"""
Telefon raqamingizni kiriting 📱
"""

LOCATION = \
"""
Manzilingizni kiriting. 
Misol: (Farg'ona viloyati, Beshariq tumani) 📍
"""

INFO = \
"""
Hamkorlik haqida ma'lumot kiriting. 
Nimalar sotmoqchisiz? 🛍️
"""




def collaboration(**kwargs):
    collaboration_text = ''
    
    collaboration_text += f"Yangi xabar 📩:\n\n"
    collaboration_text += f"Ism ✨:  {kwargs['name']}\n"
    collaboration_text += f"Telefon raqam 📱:  {kwargs['phone']}\n"
    collaboration_text += f"Telegram:  @{kwargs[ 'username']}\n"
    collaboration_text += f"Manzil 📍:  {kwargs['location']}\n"
    collaboration_text += f"Ma'lumot 📝: {kwargs['info']}\n"
    
    return collaboration_text
    
    
    
SUCCESS_COLLABORATION = \
"""
Sizning xabaringiz adminga yuborildi ✅. Tez orada siz bilan bog'lanishadi 📞.
"""



def order(**kwargs):
    order = ''
    
    order += f"🤩 <b>Mahsulot:</b> {kwargs['product']}\n"
    order += f"🎨 <b>Mahsulot Rangi:</b> {kwargs['color']}\n"
    order += f"📏 <b>Mahsulot O'lchami:</b> {kwargs['size']}\n"
    order += f"🛒 <b>Mahsulot Miqdori:</b> {kwargs['quantity']} ta\n"
    order += f"💵 <b>Mahsulot Narxi:</b> {kwargs['price']}\n"
    order += f"💰 <b>Umumiy Narxi:</b> {kwargs['item_total_price']}\n"
    
    return order

    
    

ORDER_TEXT = \
"""
{} Sizning Buyurtmalaringiz.
"""


ORDER_NOT = \
"""
Hozircha sizda hech qanday buyurtma mavjud emas. 
"""



UNTEXT = \
"""
sizni bozorimizda koʼrib turganimizdan hursandmiz marhamat bozorga qarab yoʼl oling hammasi qoʼlingizda bozor tugmasini bosing deb chiqsin
"""