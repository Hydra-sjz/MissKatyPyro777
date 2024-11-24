from pyrogram import Client, enums
from pyrogram.types import InlineKeyboardMarkup

import misskaty.strings as strings
from misskaty import custom_filter, app
from misskaty.ultis_ex.wmilia_m.button_gen import button_markdown_parser
from misskaty.ultis_ex.wmilia_m.chat_status import isUserCan
from misskaty.ultis_ex.wmilia_m.welcome_send_message import SendWelcomeMessage
from misskaty.ultis_ex.wmilia_m.welcome_mongo import (
    DEFAUT_GOODBYE,
    GetCleanService,
    GetGoobye,
    GetGoodbyemessageOnOff,
    SetGoodbyeMessageOnOff,
    isGoodbye,
)
from misskaty.ultis_ex.wmilia_m.decorators import *

GOODBYE_TRUE = ["on", "yes"]
GOODBYE_FALSE = ["off", "no"]


@app.on_message(custom_filter.command(commands="goodbye"))
@anonadmin_checker
async def Welcome(client, message):
    chat_id = message.chat.id

    if (
        not str(chat_id).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)
    if not await isUserCan(message, chat_id=chat_id, privileges="can_change_info"):
        return

    command = message.text.split(" ")
    if not (len(command) == 1):
        GetWelcomeArg = command[1]
        if GetWelcomeArg in GOODBYE_TRUE:
            await SetGoodbyeMessageOnOff(chat_id, goodbye_message=True)
            await message.reply(
                "I'll be saying goodbye to any leavers from now on!", quote=True
            )

        elif GetWelcomeArg in GOODBYE_FALSE:
            await SetGoodbyeMessageOnOff(chat_id, goodbye_message=False)
            await message.reply("I'll stay quiet when people leave.", quote=True)

        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off", quote=True
            )

    elif len(command) == 1:
        if await GetGoodbyemessageOnOff(chat_id):
            GoodByeMessage = "true"
        else:
            GoodByeMessage = "false"

        if await GetCleanService(chat_id):
            CleanService = "true"
        else:
            CleanService = "false"

        GOODBYE_MESSAGE = (
            f"I am currently saying goodbye to users: `{GoodByeMessage}`\n"
            f"I am currently deleting service messages: `{CleanService}`\n"
            "NOTE: If your group has more than 50 members, it is possible that Emilia will stop wishing users goodbye - this is a Telegram restriction.\n\n"
            "Members are currently bidden farewell with:"
        )

        GoodByeSentMessage = await message.reply(GOODBYE_MESSAGE, quote=True)

        if await isGoodbye(chat_id):
            Content, Text, DataType = await GetGoobye(chat_id)
            Text, buttons = button_markdown_parser(Text)

            reply_markup = None
            if len(buttons) > 0:
                reply_markup = InlineKeyboardMarkup(buttons)
            GoodByeSentMessage = await SendWelcomeMessage(
                GoodByeSentMessage,
                None,
                Content,
                Text,
                DataType,
                reply_markup=reply_markup,
            )
        else:
            await GoodByeSentMessage.reply(DEFAUT_GOODBYE)
