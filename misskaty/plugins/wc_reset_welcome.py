from pyrogram import Client, enums

import misskaty.strings as strings
from misskaty import custom_filter, app
from misskaty.ultis_ex.wmilia_m.chat_status import isUserCan
from misskaty.ultis_ex.wmilia_m.welcome_mongo import UnSetWelcome
#from Emilia.pyro.connection.connection import connection
from misskaty.ultis_ex.wmilia_m.decorators import *


@app.on_message(custom_filter.command(commands="resetwelcome"))
@anonadmin_checker
async def ResetWelcome(client, message):
    chat_id = message.chat.id

    if (
        not str(chat_id).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)

    if not await isUserCan(message, privileges="can_change_info"):
        return
    await UnSetWelcome(chat_id)
    await message.reply("The welcome message has been reset to default!", quote=True)
