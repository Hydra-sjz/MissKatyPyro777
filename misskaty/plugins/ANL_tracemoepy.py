# The following code is exact (almost i mean) copy of 
# reverse search taken from @DeletedUser420's Userge-Plugins repo
# originally authored by
# Phyco-Ninja (https://github.com/Phyco-Ninja) (@PhycoNinja13b)
# but is in current state after DeletedUser420's edits
# which made this code shorter and more efficient

import random
import asyncio
import tracemoepy
from traceback import format_exc as err
from tracemoepy.errors import ServerError
from aiohttp import ClientSession
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    InputMediaPhoto,
    InputMediaVideo,
    Message
)

from misskaty import app as anibot
from misskaty.vars import BOT_NAME, TRIGGERS as trg
from anilist.helper import (
    check_user,
    clog,
    control_user,
    media_to_image,
    rand_key,
    get_user_from_channel as gcc
)
from anilist.data_parser import check_if_adult
from anilist.db import get_collection
from misskaty.plugins.ANL_anime import no_pic

SFW_GRPS = get_collection("SFW_GROUPS")
DC = get_collection('DISABLED_CMDS')

TRACE_MOE = {}

@anibot.on_callback_query(filters.regex(pattern=r"tracech_(.*)"))
@check_user
async def tracemoe_btn(client: anibot, cq: CallbackQuery, cdata: dict):
    kek, page, dls_loc, user = cdata['data'].split("_")
    try:
        TRACE_MOE[dls_loc]
    except KeyError:
        return await cq.answer(
            "Query Expired!!!\nCreate new one", show_alert=True
        )
    search = TRACE_MOE[dls_loc]
    result = search["result"][int(page)]
    caption = (
        f"**Title**: {result['anilist']['title']['english']}"
        +f" (`{result['anilist']['title']['native']}`)\n"
        +f"**Anilist ID:** `{result['anilist']['id']}`\n"
        +f"**Similarity**: `{(str(result['similarity']*100))[:5]}`\n"
        +f"**Episode**: `{result['episode']}`"
    )
    preview = result['video']
    button = []
    if await check_if_adult(
        int(result['anilist']['id'])
    )=="True" and (
        await SFW_GRPS.find_one({"id": cq.message.chat.id})
    ):
        msg = InputMediaPhoto(
            no_pic[random.randint(0, 4)],
            caption="The results seems to be 18+ and not allowed in this group"
        )
    else:
        msg = InputMediaVideo(preview, caption=caption)
        button.append([
            InlineKeyboardButton(
                "More Info",
                url=f"https://anilist.co/anime/{result['anilist']['id']}"
            )
        ])
    if int(page)==0:
        button.append([
            InlineKeyboardButton(
                "Next", callback_data=f"tracech_{int(page)+1}_{dls_loc}_{user}"
            )
        ])
    elif int(page)==(len(search['result'])-1):
        button.append([
            InlineKeyboardButton(
                "Back", callback_data=f"tracech_{int(page)-1}_{dls_loc}_{user}"
            )
        ])
    else:
        button.append([
            InlineKeyboardButton(
                "Back",
                callback_data=f"tracech_{int(page)-1}_{dls_loc}_{user}"
                ),
            InlineKeyboardButton(
                "Next",
                callback_data=f"tracech_{int(page)+1}_{dls_loc}_{user}"
            )
        ])
    await cq.edit_message_media(msg, reply_markup=InlineKeyboardMarkup(button))


@anibot.on_message(
    filters.command(["reverse", f"reverse{BOT_NAME}"], prefixes=trg)
)
async def trace_bek_edit(client: anibot, message: Message):
    await trace_bek(client, message)
