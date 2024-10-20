import os
import asyncio
import PIL.Image
from pathlib import Path
import google.generativeai as genai
from pyrogram import Client, filters, enums
from pyrogram.types import Message

from misskaty import app
from misskaty.vars import OPENAI_KEY as GEMINI_API, LOG_CHANNEL


#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
genai.configure(api_key=GEMINI_API)

generation_config_cook = {
  "temperature": 0.35,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
}

model_text = genai.GenerativeModel("gemini-pro")
model = genai.GenerativeModel("gemini-pro-vision")
model_cook = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config_cook)
#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
ASKAI = """
🫶**LOG ALERT FOR AI @GojoSatoru_Xbot**

📛**Triggered Command** : /askai {}
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @GojoSatoru_Xbot AI

#askai
"""

IMGTT = """
🍃**LOG ALERT FOR AI**👾

📛**Triggered Command** : /aii {}
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @GojoSatoru_Xbot AI

#aii #ImageToTextmaker
"""

AICOOK = """
🕵️**LOG ALERT FOR AI**👾

📛**Triggered Command** : /aicook {}
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @GojoSatoru_Xbot AI

#aicook #ReplayToimgToCook
"""

AISELL = """
👾**LOG ALERT FOR AI**👾

📛**Triggered Command** : /aiseller {}
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @GojoSatoru_Xbot AI

#askai #ReplyToimgToselle
"""


#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
@app.on_message(filters.command("askai"))
async def say_ask(bot, message: Message):
    try:
        i = await message.reply_text("<code>Please Wait...</code>")

        if len(message.command) > 1:
         prompt = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
         prompt = message.reply_to_message.text
        else:
         await i.delete()
         await message.reply_text(
            f"<b>Usage: </b><code>/askai [prompt/reply to message]</code>"
        )
         return

        chat = model_text.start_chat()
        response = chat.send_message(prompt)
        await i.delete()

        await message.reply_text(f"**Question:**`{prompt}`\n**Answer:** {response.text}\n\n**Powered by**: @XBOTS_X | ©️ @GojoSatoru_Xbot", parse_mode=enums.ParseMode.MARKDOWN)
        await bot.send_message(LOG_CHANNEL, ASKAI.format(prompt, message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
    except Exception as e:
        await i.delete()
        await message.reply_text(f"An error occurred: {str(e)}")

@app.on_message(filters.command("aii"))
async def getaie(bot, message: Message):
    try:
        i = await message.reply_text("<code>Please Wait. Extracting image...</code>")

        base_img = await message.reply_to_message.download()

        img = PIL.Image.open(base_img)

        response = model.generate_content(img)
        await i.delete()

        await message.reply_text(
            f"**Detail Of Image:** {response.parts[0].text}\n\n**Powered by**: @XBOTS_X | ©️ @GojoSatoru_Xbot", parse_mode=enums.ParseMode.MARKDOWN
        )
        await bot.send_message(LOG_CHANNEL, IMGTT.format(base_img, message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
        os.remove(base_img)
    except Exception as e:
        await i.delete()
        await message.reply_text(str(e))

@app.on_message(filters.command("aicook"))
async def say_cook(bot, message: Message):
    try:
        i = await message.reply_text("<code>Some thing Cooking. please wait...</code>")

        base_img = await message.reply_to_message.download()

        img = PIL.Image.open(base_img)
        cook_img = [
        "Accurately identify the baked good in the image and provide an appropriate and recipe consistent with your analysis. ",
        img,
        ]

        response = model_cook.generate_content(cook_img)
        await i.delete()

        await message.reply_text(
            f"{response.text}\n\n**Powered by**: @XBOTS_X | ©️ @GojoSatoru_Xbot", parse_mode=enums.ParseMode.MARKDOWN
        )
        await bot.send_message(LOG_CHANNEL, AICOOK.format(base_img, message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
        os.remove(base_img)
    except Exception as e:
        await i.delete()
        await message.reply_text(f"please reply to an image.")
      
@app.on_message(filters.command("aiseller"))
async def say_sell(bot, message: Message):
    try:
        i = await message.reply_text("<code>Generating your request. please wait...</code>")
        if len(message.command) > 1:
         taud = message.text.split(maxsplit=1)[1]
        else:
         await i.delete()
         await message.reply_text(
            f"<b>Usage: </b><code>/aiseller [target audience] [reply to product image]</code>"
        )
         return

        base_img = await message.reply_to_message.download()

        img = PIL.Image.open(base_img)
        sell_img = [
        "Given an image of a product and its target audience, write an engaging marketing description",
        "Product Image: ",
        img,
        "Target Audience: ",
        taud
        ]

        response = model.generate_content(sell_img)
        await i.delete()

        await message.reply_text(
            f"{response.text}\n\n**Powered by**: @XBOTS_X | ©️ @GojoSatoru_Xbot", parse_mode=enums.ParseMode.MARKDOWN
        )
        await bot.send_message(LOG_CHANNEL, AISELL.format(taud, message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
        os.remove(base_img)
    except Exception as e:
        await i.delete()
        await message.reply_text(f"<b>Usage: </b><code>/aiseller [target audience] [reply to product image]</code>")
#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
