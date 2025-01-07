import aiohttp
import os
from aiogram import types
from tempfile import NamedTemporaryFile

async def download_and_send_image(image_urls: list, caption: str, message: types.Message):
    media_files = []
    
    async with aiohttp.ClientSession() as session:
        for image_url in image_urls:
            try:
                async with session.get(image_url) as resp:
                    if resp.status == 200:
                        photo = await resp.read()

                        with NamedTemporaryFile(delete=False, mode='wb') as tmp_file:
                            tmp_file.write(photo)
                            tmp_file.close()

                            media_files.append(types.InputMediaPhoto(media=open(tmp_file.name, 'rb'), caption=caption if image_url == image_urls[0] else None))

                            os.remove(tmp_file.name)
                    else:
                        print('---')
                        return
            except Exception as e:
                print(f"error: {e}")
                return

    if media_files:
        await message.answer_media_group(media=media_files)
