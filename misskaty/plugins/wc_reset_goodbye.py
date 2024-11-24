from pyrogram import Client, enums

import misskaty.strings as strings
from misskaty import custom_filter
from misskaty.ultis_ex.wmilia_m.chat_status import isUserCan
from misskaty.ultis_ex.wmilia_m.welcome_mongo import UnSetGoodbye

from misskaty.ultis_ex.wmilia_m.decorators import *


@Client.on_message(custom_filter.command(commands="resetgoodbye"))
@anonadmin_checker
async def ResetGoodbye(client, message):
    chat_id = message.chat.id

    if (
        not str(chat_id).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)

    if not await isUserCan(message, privileges="can_change_info"):
        return
    await UnSetGoodbye(chat_id)
    await message.reply("The Goodbye message has been reset to default!", quote=True)
