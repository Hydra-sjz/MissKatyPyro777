import os
import asyncio
import PIL.Image
from pathlib import Path
import google.generativeai as genai
from pyrogram import Client, filters, enums

import html
import privatebinapi

from cachetools import TTLCache
from openai import APIConnectionError, APIStatusError, AsyncOpenAI, RateLimitError

from pyrogram.errors import MessageTooLong
from pyrogram.types import Message

from misskaty import app
from misskaty.core import pyro_cooldown
from misskaty.helper import check_time_gap, post_to_telegraph, use_chat_lang
from misskaty.vars import COMMAND_HANDLER, GOOGLEAI_KEY, OPENAI_KEY, OWNER_ID, SUDO, LOG_CHANNEL

__MODULE__ = "ChatBot"
__HELP__ = """
/ai - Generate text response from AI using Gemini AI By Google.
/ask - Generate text response from AI using OpenAI.
"""

#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
genai.configure(api_key=GOOGLEAI_KEY)

generation_config_cook = {
  "temperature": 0.35,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
}

model_text = genai.GenerativeModel("gemini-pro")
model = genai.GenerativeModel("gemini-1.5-flash")
model_cook = genai.GenerativeModel(model_name="gemini-1.5-flash",
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
@app.on_message(filters.command("askai", COMMAND_HANDLER) & pyro_cooldown.wait(10))
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

@app.on_message(filters.command("aii", COMMAND_HANDLER) & pyro_cooldown.wait(10))
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

@app.on_message(filters.command("aicook", COMMAND_HANDLER) & pyro_cooldown.wait(10))
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
      
@app.on_message(filters.command("aiseller", COMMAND_HANDLER) & pyro_cooldown.wait(10))
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

gptai_conversations = TTLCache(maxsize=4000, ttl=24*60*60)
gemini_conversations = TTLCache(maxsize=4000, ttl=24*60*60)

async def get_openai_stream_response(is_stream, key, base_url, model, messages, bmsg, strings):
    ai = AsyncOpenAI(api_key=key, base_url=base_url)
    answer = ""
    num = 0
    try:
        response = await ai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
            stream=is_stream,
        )
        if not is_stream:
            answer += response.choices[0].message.content
            if len(answer) > 4000:
                answerlink = await privatebinapi.send_async("https://bin.yasirweb.eu.org", text=answer, expiration="1week", formatting="markdown")
                await bmsg.edit_msg(
                    strings("answers_too_long").format(answerlink=answerlink.get("full_url")),
                    disable_web_page_preview=True,
                )
            else:
                await bmsg.edit_msg(f"{html.escape(answer)}\n<b>Powered by:</b> <code>Gemini 1.5 Flash</code>")
        else:
            async for chunk in response:
                if not chunk.choices or not chunk.choices[0].delta.content:
                    continue
                num += 1
                answer += chunk.choices[0].delta.content
                if num == 30 and len(answer) < 4000:
                    await bmsg.edit_msg(html.escape(answer))
                    await asyncio.sleep(1.5)
                    num = 0
            if len(answer) > 4000:
                answerlink = await privatebinapi.send_async("https://bin.yasirweb.eu.org", text=answer, expiration="1week", formatting="markdown")
                await bmsg.edit_msg(
                    strings("answers_too_long").format(answerlink=answerlink.get("full_url")),
                    disable_web_page_preview=True,
                )
            else:
                await bmsg.edit_msg(f"{html.escape(answer)}\n\n<b>Powered by:</b> <code>GPT 4o</code>")
    except APIConnectionError as e:
        await bmsg.edit_msg(f"The server could not be reached because {e.__cause__}")
        return None
    except RateLimitError as e:
        if "billing details" in str(e):
            return await bmsg.edit_msg(
                "This openai key from this bot has expired, please give openai key donation for bot owner."
            )
        await bmsg.edit_msg("You're got rate limit, please try again later.")
        return None
    except APIStatusError as e:
        await bmsg.edit_msg(
            f"Another {e.status_code} status code was received with response {e.response}"
        )
        return None
    except Exception as e:
        await bmsg.edit_msg(f"ERROR: {e}")
        return None
    return answer


@app.on_message(filters.command("ai2", COMMAND_HANDLER) & pyro_cooldown.wait(10))
@app.on_bot_business_message(
    filters.command("ai2", COMMAND_HANDLER) & pyro_cooldown.wait(10)
)
@use_chat_lang()
async def gemini_chatbdot(_, ctx: Message, strings):
    if len(ctx.command) == 1:
        return await ctx.reply_msg(
            strings("no_question").format(cmd=ctx.command[0]), quote=True, del_in=5
        )
    if not GOOGLEAI_KEY:
        return await ctx.reply_msg("GOOGLEAI_KEY env is missing!!!")
    uid = ctx.from_user.id if ctx.from_user else ctx.sender_chat.id
    msg = await ctx.reply_msg(strings("find_answers_str"), quote=True)
    if uid not in gemini_conversations:
        gemini_conversations[uid] = [{"role": "system", "content": "Kamu adalah AI dengan karakter mirip kucing bernama MissKaty AI yang diciptakan oleh Yasir untuk membantu manusia mencari informasi."}, {"role": "user", "content": ctx.input}]
    else:
        gemini_conversations[uid].append({"role": "user", "content": ctx.input})
    ai_response = await get_openai_stream_response(False, GOOGLEAI_KEY, "https://gemini.yasirapi.eu.org/v1", "gemini-1.5-flash", gemini_conversations[uid], msg, strings)
    if not ai_response:
        gemini_conversations[uid].pop()
        if len(gemini_conversations[uid]) == 1:
            gemini_conversations.pop(uid)
        return
    gemini_conversations[uid].append({"role": "assistant", "content": ai_response})

@app.on_message(filters.command("ask2", COMMAND_HANDLER) & pyro_cooldown.wait(10))
@use_chat_lang()
async def openai_chatfbot(self, ctx: Message, strings):
    if len(ctx.command) == 1:
        return await ctx.reply_msg(
            strings("no_question").format(cmd=ctx.command[0]), quote=True, del_in=5
        )
    if not OPENAI_KEY:
        return await ctx.reply_msg("OPENAI_KEY env is missing!!!")
    uid = ctx.from_user.id if ctx.from_user else ctx.sender_chat.id
    is_in_gap, _ = await check_time_gap(uid)
    if is_in_gap and (uid != OWNER_ID or uid not in SUDO):
        return await ctx.reply_msg(strings("dont_spam"), del_in=5)
    pertanyaan = ctx.input
    msg = await ctx.reply_msg(strings("find_answers_str"), quote=True)
    if uid not in gptai_conversations:
        gptai_conversations[uid] = [{"role": "system", "content": "Kamu adalah AI dengan karakter mirip kucing bernama MissKaty AI yang diciptakan oleh Yasir untuk membantu manusia mencari informasi."}, {"role": "user", "content": pertanyaan}]
    else:
        gptai_conversations[uid].append({"role": "user", "content": pertanyaan})
    ai_response = await get_openai_stream_response(True, OPENAI_KEY, "https://models.inference.ai.azure.com" if uid == OWNER_ID else "https://duckai.yasirapi.eu.org/v1", "gpt-4o" if uid == OWNER_ID else "gpt-4o-mini", gptai_conversations[uid], msg, strings)
    if not ai_response:
        gptai_conversations[uid].pop()
        if len(gptai_conversations[uid]) == 1:
            gptai_conversations.pop(uid)
        return
    gptai_conversations[uid].append({"role": "assistant", "content": ai_response})
