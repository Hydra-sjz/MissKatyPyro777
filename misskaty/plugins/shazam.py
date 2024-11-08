import os
import asyncio
from shazamio import Shazam
from plugins.humanbyte import humanbytes
from pyrogram import filters, Client
import datetime
import requests
import time
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.cmd import edit_or_reply, runcmd, fetch_audio








@Client.on_message(filters.command(["audify"]))
async def shazamm(client, message):
    rsr1 = await edit_or_reply(message, "⏳")
    if not message.reply_to_message:
        await rsr1.edit("Reply Audio or Video.")
        return
    if os.path.exists("friday.mp3"):
        os.remove("friday.mp3")
    kkk = await fetch_audio(client, message)
    downloaded_file_name = kkk
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    await rsr1.edit("🔍")
    r = requests.post("https://starkapi.herokuapp.com/shazam/", files=f)
    try:
        xo = r.json()
    except JSONDecodeError:
        await rsr1.edit("**Song not found😔**")
        return
    if xo.get("success") is False:
        await rsr1.edit("**Song not found😔**")
        os.remove(downloaded_file_name)
        return
    xoo = xo.get("response")
    zz = xoo[1]
    zzz = zz.get("track")
    if not zzz:
        await rsr1.edit("**Song not found😔**")
        return
    nt = zzz.get("images")
    image = nt.get("coverarthq")
    by = zzz.get("subtitle")
    title = zzz.get("title")
    messageo = f"""<b><u>Identify Finished ✅</b></u>\n
<b>📁 Song Name : </b> {title}\n
<b>🎙️ Artist : </b>{by}
"""
    await client.send_photo(message.chat.id, image, messageo, reply_to_message_id=message.reply_to_message.message_id, parse_mode="HTML")
    os.remove(downloaded_file_name)
    await rsr1.delete()

	
