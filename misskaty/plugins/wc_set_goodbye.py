from pyrogram import Client, enums

import misskaty.strings as strings
from misskaty import custom_filter, app
from misskaty.ultis_ex.wmilia_m.chat_status import isUserCan
from misskaty.ultis_ex.wmilia_m.get_welcome_message import GetWelcomeMessage
from misskaty.ultis_ex.wmilia_m.welcome_mongo import SetGoodBye

from Emilia.utils.decorators import *


@app.on_message(custom_filter.command(commands="setgoodbye"))
@anonadmin_checker
async def set_goodbye(client, message):
    ChatID = message.chat.id

    if (
        not str(ChatID).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)

    if not await isUserCan(message, privileges="can_change_info"):
        return

    command = message.text.split(" ")
    if not message.reply_to_message and len(command) == 1:
        return await message.reply("You need to give the goodbye message some content!")

    CONTENT, TEXT, DATATYPE = GetWelcomeMessage(message)
    await SetGoodBye(ChatID, CONTENT, TEXT, DATATYPE)
    await message.reply("The new goodbye message has been saved!", quote=True)
