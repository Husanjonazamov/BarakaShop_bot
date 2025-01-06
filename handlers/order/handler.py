# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import buttons, texts
from services import getOrder
from handlers.order.getimage import download_and_send_image


@dp.message_handler(lambda message: message.text.startswith(buttons.MYORDER))
async def order_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    orders = getOrder(user_id)

    if orders:
        for order in orders:
            order_items = order.get('order_items', [])
            if order_items:
                for item in order_items:
                    item_total_price = int(float(item["quantity"]) * float(item["price"]))
                    product = item['product']['name']
                    color = item['color']['name']
                    size = item['size']['size_name']
                    quantity = item['quantity']
                    price = int(float(item['price']))
                    main_image = item['product'].get('main_image')
                    color_image = item['color'].get('image')

                    order_item = texts.order(
                        product=product,
                        color=color,
                        size=size,
                        quantity=quantity,
                        price=price,
                        item_total_price=item_total_price
                    )

                    image_urls = []
                    if main_image:
                        image_urls.append(main_image)
                    if color_image:
                        image_urls.append(color_image)

                    if image_urls:
                        try:
                            await download_and_send_image(image_urls, order_item, message)
                        except Exception as e:
                            print(f"Xatolik: {e}")
                            await message.answer(order_item)
                    else:
                        await message.answer(order_item)
    else:
        await message.answer(texts.ORDER_NOT)
