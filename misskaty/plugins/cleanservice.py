from pyrogram import Client

from misskaty import app
from misskaty.ultis_ex.wmilia_m.chat_status import CheckAllAdminsStuffs
from misskaty.ultis_ex.wmilia_m.welcome_mongo import GetCleanService, SetCleanService
from misskaty.ultis_ex.wmilia_m.decorators import *

CLEAN_SERVICE_TRUE = ["on", "yes"]
CLEAN_SERVICE_FALSE = ["off", "no"]


@app.on_message(filters.group & filters.command("cleanservice"))
@anonadmin_checker
async def CleanService(client, message):
    chat_id = message.chat.id

    if not (await CheckAllAdminsStuffs(message, privileges="can_delete_messages")):
        return

    command = message.text.split(" ")
    if not (len(command) == 1):
        get_clean_service = command[1]

        if get_clean_service in CLEAN_SERVICE_TRUE:
            clean_service = True
            await SetCleanService(chat_id, clean_service)
            await message.reply(
                "I'll be deleting all service messages from now on!", quote=True
            )

        elif get_clean_service in CLEAN_SERVICE_FALSE:
            clean_service = False
            await SetCleanService(chat_id, clean_service)
            await message.reply("I'll leave service messages.", quote=True)

        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off", quote=True
            )

    elif len(command) == 1:
        if await GetCleanService(chat_id):
            CleanServiceis = "I am currently deleting service messages when new members join or leave."

        else:
            CleanServiceis = "I am not currently deleting service messages when members join or leave."

        await message.reply(
            (
                f"{CleanServiceis}\n\n"
                "To change this setting, try this command again followed by one of yes/no/on/off"
            ),
            quote=True,
        )
