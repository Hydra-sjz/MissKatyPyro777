# /usr/bin/nuhman/bughunter0 

from dotenv import load_dotenv
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from stickers import stickers
import google.generativeai as genai
import os
import PIL.Image
import random
import time
from misskaty import app
from misskaty.vars import GEMINI_API

genai.configure(api_key=GEMINI_API)




@app.on_message(filters.photo)
async def vision(bot, message: Message):
    try:
        model_name = "gemini-1.5-pro"
        sticker_id = random.choice(stickers)
        sticker = await message.reply_sticker(sticker_id)
        txt = await message.reply(f"Loading {model_name} ...")
        model = genai.GenerativeModel(model_name)
        await txt.edit("Downloading Photo ....")
        file_path = await message.download()
        caption = message.caption
        img = PIL.Image.open(file_path)
        await txt.edit("Gemini Vision Pro is At Work ⚠️.\n Pls Wait..")
        response = (
            model.generate_content([caption, img])
            if caption
            else model.generate_content(img)
        )
        os.remove(file_path)
        await txt.edit('@GojoSatoru_Xbot is cooking...')
        await sticker.delete()
        await txt.delete()
        if response.parts: # handle multiline resps
           for part in response.parts:
            await message.reply(part.text, reply_markup=GITHUB_BUTTON)
            time.sleep(2)
        elif response.text:
            await message.reply(response.text, reply_markup=GITHUB_BUTTON)
        else:
            await message.reply(
                "Couldn't figure out what's in the Image. Contact @xbots_x for help."
            )
    except Exception as e:
        await message.reply("Something Bad occured.")
        raise e
