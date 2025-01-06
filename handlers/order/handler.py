# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import buttons, texts
from services import getOrder


@dp.message_handler(lambda message: message.text.startswith(buttons.MYORDER))
async def order_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    orders = getOrder(user_id)
    


    if orders and orders[0].get('order_items'):  
        for item in orders[0]['order_items']:
            item_total_price = int(float(item["quantity"]) * float(item["price"]))
            product = item['product']['name']
            color = item['color']['name']
            size = item['size']['size_name']
            quantity = item['quantity']
            price = int(float(item['price']))
            item_total_price = item_total_price
            main_image = item['product'].get('main_image', None)
            
        order_item = texts.order(
            product=product,
            color=color,
            size=size,
            quantity=quantity,
            price=price,
            item_total_price=item_total_price
        )        
        await message.answer(texts.ORDER_TEXT.format(message.from_user.first_name))
        if main_image:
            try:
                await message.answer_photo(photo=main_image, caption=order_item)
            except:
                await message.answer(order_item)
        else:
            await message.answer(order_item)
    else:
        # Agar buyurtmalar bo'lmasa
        await message.answer("Hozircha sizda hech qanday buyurtma mavjud emas.")
