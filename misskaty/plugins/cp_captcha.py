from pyrogram import Client, enums

import misskaty.strings as strings
from misskaty import custom_filter, app
from misskaty.ultis_ex.wmilia_m.chat_status import isBotCan, isUserCan
from misskaty.ultis_ex.wmilia_m.welcome_mongo import SetCaptcha, isGetCaptcha
#from Emilia.pyro.connection.connection import connection
from misskaty.ultis_ex.wmilia_m.decorators import *

CAPTCHA_WELCOME_TRUE = ["on", "yes"]
CAPTCHA_WELCOME_FALSE = ["off", "no"]


@app.on_message(custom_filter.command(commands="captcha"))
@anonadmin_checker
async def Captcha(client, message):
    chat_id = message.chat.id

    if (
        not str(chat_id).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)

    if not await isBotCan(message, privileges="can_restrict_members", silent=True):
        await message.reply(
            "I need to be admin with the right to restrict to enable CAPTCHAs.",
            quote=True,
        )
        return

    if not await isUserCan(message, privileges="can_restrict_members", silent=True):
        await message.reply(
            "You need to be admin with the right to restrict to enable CAPTCHAs.",
            quote=True,
        )
        return

    if len(message.text.split()) >= 2:
        get_args = message.text.split()[1]

        if get_args in CAPTCHA_WELCOME_TRUE:
            await message.reply(
                "CAPTCHAs have been enabled. I will now mute people when they join.",
                quote=True,
            )
            captcha = True
            await SetCaptcha(chat_id, captcha)

        elif get_args in CAPTCHA_WELCOME_FALSE:
            await message.reply(
                "CAPTCHAs have been disabled. Users can join normally.", quote=True
            )
            captcha = False
            await SetCaptcha(chat_id, captcha)

    elif len(message.text.split()) == 1:
        if await isGetCaptcha(chat_id):
            CaptchaSetting = "Users will be asked to complete a CAPTCHA before being allowed to speak in the chat."
        else:
            CaptchaSetting = "Users will NOT be muted when joining the chat."

        await message.reply(
            (
                f"{CaptchaSetting}\n\n"
                "To change this setting, try this command again followed by one of yes/no/on/off"
            ),
            quote=True,
        )
