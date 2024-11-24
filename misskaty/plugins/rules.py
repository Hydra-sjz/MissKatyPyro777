import html

from pyrogram import Client, enums

import misskaty.strings as strings
from misskaty import custom_filter, app, BOT_USERNAME
from misskaty.ultis_ex.wmilia_m.chat_status import isUserCan
from misskaty.ultis_ex.wmilia_m.get_data import GetChat
from misskaty.ultis_ex.wmilia_m.rules_mongo import get_private_note, set_private_rule, set_rules_db, set_rule_button, get_rules, get_rules_button
#from Emilia.pyro.connection.connection import connection
from Emilia.utils.decorators import *

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from misskaty.ultis_ex.wmilia_m.button_gen import button_markdown_parser
from misskaty.ultis_ex.wmilia_m.note_fillings import NoteFillings as rules_filler






PRIVATE_RULES_TRUE = ["yes", "on"]
PRIVATE_RULES_FALSE = ["no", "off"]

#====privt-rl
@app.on_message(custom_filter.command(commands="privaterules"))
@anonadmin_checker
async def private_rules(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title

    if (
        not str(chat_id).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)

    if not await isUserCan(message, privileges="can_change_info"):
        return

    command = message.text.split(" ")
    if not (len(command) == 1):
        args = command[1]

        if args in PRIVATE_RULES_TRUE:
            await message.reply(
                "Use of /rules will send the rules to the user's PM.", quote=True
            )
            await set_private_rule(chat_id, True)

        elif args in PRIVATE_RULES_FALSE:
            await message.reply(
                f"All /rules commands will send the rules to {html.escape(chat_title)}.",
                quote=True,
            )
            await set_private_rule(chat_id, False)

        else:
            await message.reply(
                "I only understand the following: yes/no/on/off", quote=True
            )
    else:
        if await get_private_note(chat_id):
            await message.reply("Use of /rules will send the rules to the user's PM.")
        else:
            await message.reply(
                f"All /rules commands will send the rules to {html.escape(chat_title)}."
            )

#====== Reset-rules

@app.on_message(custom_filter.command(commands=["resetrules", "clearrules"]))
@anonadmin_checker
async def reset_rules(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title

    if (
        not str(chat_id).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)

    if not await isUserCan(message, privileges="can_change_info"):
        return

    await set_rules_db(chat_id, None)
    await message.reply(
        f"Rules for {html.escape(chat_title)} were successfully cleared!"
    )

#=======Rules-button

@app.on_message(custom_filter.command(commands="resetrulesbutton"))
@anonadmin_checker
async def reset_rules(client, message):
    chat_id = message.chat.id

    if (
        not str(chat_id).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)

    if not await isUserCan(message, privileges="can_change_info"):
        return

    await set_rule_button(chat_id, "Rules")
    await message.reply("Reset the rules button name to default", quote=True)

#====Rules

@app.on_message(custom_filter.command(commands="rules"))
async def rules(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title

    if not str(chat_id).startswith("-100"):
        return await message.reply(strings.is_pvt)

    rules_text = await get_rules(chat_id)
    if rules_text is None:
        return await message.reply(
            "This chat doesn't seem to have had any rules set yet... I wouldn't take that as an invitation though.",
            quote=True,
        )

    if not (await get_private_note(chat_id)):
        rules_text, buttons = button_markdown_parser(rules_text)
        button_markdown = None
        if len(buttons) > 0:
            button_markdown = InlineKeyboardMarkup(buttons)

        rules_text = await rules_filler(message, rules_text)

        await message.reply(
            (f"The rules for `{html.escape(chat_title)}` are:\n\n" f"{rules_text}"),
            reply_markup=button_markdown,
            quote=True,
        )
    else:
        button_text = await get_rules_button(chat_id)
        button = [
            [
                InlineKeyboardButton(
                    text=button_text,
                    url=f"http://t.me/{BOT_USERNAME}?start=rules_{chat_id}",
                )
            ]
        ]

        await message.reply(
            "Click on the button to see the chat rules!",
            reply_markup=InlineKeyboardMarkup(button),
            quote=True,
        )


async def rulesRedirect(message):
    chat_id = int(message.text.split()[1].split("_")[1])
    chat_title = await GetChat(chat_id)
    rules_text = await get_rules(chat_id)

    rules_text, buttons = button_markdown_parser(rules_text)
    button_markdown = None
    if len(buttons) > 0:
        button_markdown = InlineKeyboardMarkup(buttons)

    rules_text = await rules_filler(message, rules_text)
    await message.reply(
        (f"The rules for `{html.escape(chat_title)}` are:\n\n" f"{rules_text}"),
        reply_markup=button_markdown,
        quote=True,
    )

#======set-rul-b

@app.on_message(custom_filter.command(commands="setrulesbutton"))
@anonadmin_checker
async def set_rules(client, message):
    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if (
        not str(chat_id).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)

    if not await isUserCan(message, privileges="can_change_info"):
        return

    command = message.text.split(" ")
    if len(command) == 1:
        current_rules_button = await get_rules_button(chat_id)
        return await message.reply(
            f"The rules button will be called:\n `{current_rules_button}`\n\nTo change the button name, try this command again followed by the new name",
            quote=True,
        )

    rules_button = " ".join(command[1:])

    await set_rule_button(chat_id, rules_button)
    await message.reply("Updated the rules button name!", quote=True)

#====set-ruls


@usage("/setrules [rules]")
@example("/setrules No promotion allowed.")
@description("Use this command to set rules for users in a group chat.")
@app.on_message(custom_filter.command(commands="setrules"))
@anonadmin_checker
@logging
async def set_rules(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title

    if (
        not str(chat_id).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)

    if not await isUserCan(message, privileges="can_change_info"):
        return

    command = message.text.split(" ")
    if len(command) == 1:
        await usage_string(message, set_rules)
        return

    get_rules = message.text.markdown[len(message.text.split()[0]) + 2 :]
    await set_rules_db(chat_id, get_rules)
    await message.reply(
        f"New rules for {html.escape(chat_title)} set successfully!", quote=True
    )
    return "NEW_RULES", None, None
