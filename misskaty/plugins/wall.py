from requests import get 
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from misskaty import app
@app.on_message(filters.command(['wall']))
async def WallbpapersCom(client, message):
    chat_id = message.chat.id
    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("Input image name for search 🔍")

    msg = await message.reply("🔍")
    
    images = get(f"https://hoshi-api-f62i.onrender.com/api/wallpaper?query={query}").json()
    media_group = []
    count = 0

    if not images:
       return await message.reply_text(
         text=f"**✨ No wallpapers found for query: `{message.text.split(None, 1)[1]}`, Ask other I wish to send you ❤️**"
       )
      
    for url in images["images"][:8]:
        media_group.append(InputMediaPhoto(media=url))
        count += 1
    
    await msg.edit(f"⚡ Fetched {count} wallpapers...")
    
    try:
        await client.send_media_group(
            chat_id=chat_id, 
            media=media_group,
            reply_to_message_id=message.id
        )
        return await msg.delete()
    except Exception as e:
        await msg.delete()
        return await message.reply(f"Error\n{e}")

# DONE: Wallpaperf

import asyncio
import random


from misskaty import tle as telethn
from misskaty.custom_filter import register
from misskaty.ultis_ex.wmilia_m.decorators import *


@usage("/wall [query]")
@example("/wall naruto")
@description("This will send desired wallpaper.")
@register(pattern="wall2")
@rate_limit(40, 60)
async def some1(event):
    try:
        inpt: str = (
            event.text.split(None, 1)[1]
            if len(event.text) < 3
            else event.text.split(None, 1)[1].replace(" ", "%20")
        )
    except IndexError:
        return await usage_string(event, some1)

    Emievent = await event.reply("Sending please wait...")
    try:
        r = get(
            f"https://bakufuapi.vercel.app/api/wall/wallhaven?query={inpt}&page=1"
        ).json()

        list_id = [r["response"][i]["path"] for i in range(len(r["response"]))]
        item = (random.sample(list_id, 1))[0]
    except BaseException:
        await event.reply("Try again later or enter correct query.")
        await Emievent.delete()
        return

    await telethn.send_file(event.chat_id, item, caption="Preview", reply_to=event)
    await telethn.send_file(
        event.chat_id, file=item, caption="wall", reply_to=event, force_document=True
    )
    await Emievent.delete()
    await asyncio.sleep(5)
