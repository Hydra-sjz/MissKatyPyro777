from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup

from misskaty import custom_filter, app
from misskaty.ultis_ex.wmilia_m.button_gen import button_markdown_parser
from misskaty.ultis_ex.wmilia_m.chat_status import CheckAdmins
from misskaty.ultis_ex.wmilia_m.welcome_fillings import Welcomefillings
from misskaty.ultis_ex.wmilia_m.welcome_send_message import SendWelcomeMessage
from misskaty.ultis_ex.wmilia_m.welcome_mongo import (
    DEFAUT_WELCOME,
    GetCaptchaSettings,
    GetCleanService,
    GetWelcome,
    GetWelcomemessageOnOff,
    SetWelcomeMessageOnOff,
    isGetCaptcha,
    isWelcome,
)
#from Emilia.pyro.connection.connection import connection

WELCOME_TRUE = ["on", "yes"]
WELCOME_FALSE = ["off", "no"]


@app.on_message(custom_filter.command(commands="welcome"))
async def Welcome(client, message):
    chat_id = message.chat.id

    if not await CheckAdmins(message):
        return

    if len(message.text.split()) >= 2:
        GetWelcomeArg = message.text.split()[1]
        if GetWelcomeArg in WELCOME_TRUE:
            await SetWelcomeMessageOnOff(chat_id, welcome_message=True)
            await message.reply(
                "I'll be welcoming all new members from now on!", quote=True
            )

        elif GetWelcomeArg in WELCOME_FALSE:
            await SetWelcomeMessageOnOff(chat_id, welcome_message=False)
            await message.reply("I'll stay quiet when new members join.", quote=True)

        elif GetWelcomeArg == "noformat":
            await welcomeformat(message, chat_id, noformat=True)

        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off", quote=True
            )

    elif len(message.text.split()) == 1:
        await welcomeformat(message, chat_id, noformat=False)


async def welcomeformat(message, chat_id, noformat=True):
    if await GetWelcomemessageOnOff(chat_id):
        WelcomeMessage = "true"
    else:
        WelcomeMessage = "false"

    if await GetCleanService(chat_id):
        CleanService = "true"
    else:
        CleanService = "false"

    if await isGetCaptcha(chat_id):
        captcha_mode, captcha_text, captcha_kick_time = await GetCaptchaSettings(
            chat_id
        )

        if captcha_mode is None:
            captcha_mode = "button"

        if captcha_text is None:
            captcha_text = "Click here to prove you're human"

        if captcha_kick_time is None:
            captcha_kick_time = "disabled"

        captcha = (
            f"The current CAPTCHA mode is: `{captcha_mode}`\n"
            f"The CAPTCHA button will say: `{captcha_text}`\n"
            f"CAPTCHA kicks are currently: `{captcha_kick_time}`\n\n"
        )
    else:
        captcha = "CAPTCHAs are disabled.\n"

    WELCOME_MESSAGE = (
        f"I am currently welcoming users: `{WelcomeMessage}`\n"
        f"I am currently deleting services: `{CleanService}`\n"
        f"{captcha}"
        "Members are currently welcomed with:"
    )

    WelcomeSentMessage = await message.reply(WELCOME_MESSAGE, quote=True)

    if await isWelcome(chat_id):
        Content, Text, DataType = await GetWelcome(chat_id)
        Text, buttons = button_markdown_parser(Text)

        reply_markup = None
        if len(buttons) > 0:
            reply_markup = InlineKeyboardMarkup(buttons)
        if noformat:
            WelcomeSentMessage = await SendWelcomeMessage(
                WelcomeSentMessage,
                None,
                Content,
                Text,
                DataType,
                reply_markup=reply_markup,
            )
        else:
            WelcomeSentMessage = await SendWelcomeMessage(
                WelcomeSentMessage,
                message.from_user,
                Content,
                Text,
                DataType,
                reply_markup=reply_markup,
            )
    else:
        if noformat:
            await WelcomeSentMessage.reply(DEFAUT_WELCOME)
        else:
            welcome_message = await Welcomefillings(
                message, DEFAUT_WELCOME, message.from_user
            )
            await WelcomeSentMessage.reply(welcome_message)
