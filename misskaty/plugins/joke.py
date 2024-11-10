from pyrogram import Client
from requests import get

from misskaty import app
from misskaty.ultis_ex.wmilia_m.decorators import *


@app.on_message(filters.command(["joke", "jokes", "funny"]))
@rate_limit(10, 60)
async def joke(client, message):
    try:
        joke = get("https://v2.jokeapi.dev/joke/Any").json()
        try:
            get1 = joke["setup"]
            get2 = joke["delivery"]
            await message.reply(f"{get1}\n{get2}")
        except BaseException:
            get3 = joke["joke"]
            await message.reply(get3)
    except Exception as e:
        return await message.reply(
            str(e) + "\nPlease report to support chat @SpiralTechDivision"
        )
