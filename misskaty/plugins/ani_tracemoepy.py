import asyncio
import random
from traceback import format_exc as err

import tracemoepy
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
from tracemoepy.errors import ServerError

from misskaty import app as anibot, custom_filter
from misskaty.plugins.anilist import no_pic
from anilist.data_parser import check_if_adult
from anilist.db import get_collection
from anilist.helper import clog, control_user, media_to_image, rand_key

SFW_GRPS = get_collection("SFW_GROUPS")
DC = get_collection("DISABLED_CMDS")

TRACE_MOE = {}




@anibot.on_callback_query(filters.regex(pattern=r"tracech_(.*)"))
async def tracemoe_btn(client: anibot, cq: CallbackQuery):
    kek, page, dls_loc, user = cq.data.split("_")
    try:
        TRACE_MOE[dls_loc]
    except KeyError:
        return await cq.answer("Query Expired!!!\nCreate new one", show_alert=True)
    search = TRACE_MOE[dls_loc]
    result = search["result"][int(page)]
    caption = (
        f"**Title**: {result['anilist']['title']['english']}"
        + f" (`{result['anilist']['title']['native']}`)\n"
        + f"**Anilist ID:** `{result['anilist']['id']}`\n"
        + f"**Similarity**: `{(str(result['similarity']*100))[:5]}`\n"
        + f"**Episode**: `{result['episode']}`"
    )
    preview = result["video"]
    button = []
    if await check_if_adult(int(result["anilist"]["id"])) == "True" and (
        await SFW_GRPS.find_one({"id": cq.message.chat.id})
    ):
        msg = InputMediaPhoto(
            no_pic[random.randint(0, 4)],
            caption="The results seems to be 18+ and not allowed in this group",
        )
    else:
        msg = InputMediaVideo(preview, caption=caption)
        button.append(
            [
                InlineKeyboardButton(
                    "More Info",
                    url=f"https://anilist.co/anime/{result['anilist']['id']}",
                )
            ]
        )
    if int(page) == 0:
        button.append(
            [
                InlineKeyboardButton(
                    "Next", callback_data=f"tracech_{int(page)+1}_{dls_loc}_{user}"
                )
            ]
        )
    elif int(page) == (len(search["result"]) - 1):
        button.append(
            [
                InlineKeyboardButton(
                    "Back", callback_data=f"tracech_{int(page)-1}_{dls_loc}_{user}"
                )
            ]
        )
    else:
        button.append(
            [
                InlineKeyboardButton(
                    "Back", callback_data=f"tracech_{int(page)-1}_{dls_loc}_{user}"
                ),
                InlineKeyboardButton(
                    "Next", callback_data=f"tracech_{int(page)+1}_{dls_loc}_{user}"
                ),
            ]
        )
    await cq.edit_message_media(msg, reply_markup=InlineKeyboardMarkup(button))
