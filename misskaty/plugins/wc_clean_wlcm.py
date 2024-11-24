from pyrogram import Client

from misskaty import custom_filter, app
from misskaty.ultis_ex.wmilia_m.chat_status import CheckAdmins
from misskaty.ultis_ex.wmilia_m.welcome_mongo import GetCleanWelcome, SetCleanWelcome

CLEAN_WELCOME_TRUE = ["on", "yes"]
CLEAN_WELCOME_FALSE = ["off", "no"]


@app.on_message(custom_filter.command(commands="cleanwelcome"))
async def CleanWelcome(client, message):
    chat_id = message.chat.id

    if not await CheckAdmins(message):
        return

    command = message.text.split(" ")
    if not (len(command) == 1):
        get_args = command[1]
        if get_args in CLEAN_WELCOME_TRUE:
            clean_welcome = True
            await SetCleanWelcome(chat_id, clean_welcome)
            await message.reply(
                "I'll be deleting all old welcome/goodbye messages from now on!",
                quote=True,
            )

        elif get_args in CLEAN_WELCOME_FALSE:
            clean_welcome = False
            await SetCleanWelcome(chat_id, clean_welcome)
            await message.reply("I'll leave old welcome/goodbye messages.", quote=True)

    elif len(command) == 1:
        if await GetCleanWelcome(chat_id):
            CleanMessage = (
                "I am currently deleting old welcome messages when new members join."
            )
        else:
            CleanMessage = "I am not currently deleting old welcome messages when new members join."

        await message.reply(
            (
                f"{CleanMessage}\n\n"
                "To change this setting, try this command again followed by one of yes/no/on/off"
            ),
            quote=True,
        )
