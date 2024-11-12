# DONE: Admins

import asyncio
import time
from asyncio import sleep
from datetime import datetime

from telethon import errors, types
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import MessageEntityMention, MessageEntityMentionName

import misskaty.strings as strings
from misskaty import DEV_USERS, db, tle as meow
from misskaty.ultis_ex.wmilia_m.decorators import *

cache_collection = db.admincache


def ctypeof(text):
    try:
        return int(text)
    except BaseException:
        return text


async def find_instance(items, class_or_tuple):
    for item in items:
        if isinstance(item, class_or_tuple):
            return item
    return None


async def get_user_reason(event):
    args = event.text.split(" ", maxsplit=1)

    user_input = None
    extra = None
    users = None

    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        try:
            user_input = await meow.get_entity(previous_message.sender_id)
        except errors.FloodWaitError as e:
            await sleep(e.seconds)

        extra = args[1] if len(args) >= 2 else None

    elif len(args) > 1:
        args = event.text.split(" ", maxsplit=2)
        extra = args[2] if len(args) > 2 else None
        user_input = args[1]

        if user_input.isnumeric():
            users = int(user_input)

        elif event.entities:
            for entity in event.entities:
                if isinstance(entity, MessageEntityMentionName):
                    users = entity.user_id
                if isinstance(entity, MessageEntityMention):
                    users = args[1]

        if users:
            try:
                user_input = await meow.get_entity(ctypeof(users))
            except (TypeError, ValueError):
                pass
            except errors.FloodWaitError as e:
                await sleep(e.seconds)

        else:
            return None, None
    else:
        return None, None

    return user_input, extra


async def get_extra_args(event):
    try:
        args = event.text.split(None, 1)[1].strip()
    except IndexError:
        args = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        return previous_message.text
    elif args:
        return args


async def extract_time(message, time_val):
    if any(time_val.endswith(unit) for unit in ("m", "h", "d")):
        unit = time_val[-1]
        time_num = time_val[:-1]  # type: str
        if not time_num.isdigit():
            await message.reply("Invalid time amount specified.")
            return None
        if unit == "m":
            bantime = int(time.time() + int(time_num) * 60)
        elif unit == "h":
            bantime = int(time.time() + int(time_num) * 60 * 60)
        elif unit == "d":
            bantime = int(time.time() + int(time_num) * 24 * 60 * 60)
        else:
            return
        return bantime
    else:
        return None


async def get_time(time: int):
    if time < 60:
        return f"{time} second{'s' if time != 1 else ''}"

    time_units = [("day", 86400), ("hour", 3600), ("minute", 60)]
    time_parts = []

    for unit, divisor in time_units:
        if time >= divisor:
            count = time // divisor
            time %= divisor
            time_parts.append(f"{count} {unit}{'s' if count != 1 else ''}")

    if time > 0:
        time_parts.append(f"{time} second{'s' if time != 1 else ''}")

    return " ".join(time_parts)


async def can_add_admins(event, user_id):
    try:
        p = await meow(GetParticipantRequest(event.chat_id, user_id))
    except UserNotParticipantError:
        return False

    if (
        isinstance(p.participant, types.ChannelParticipantCreator)
        or user_id in DEV_USERS
    ):
        return True

    elif isinstance(p.participant, types.ChannelParticipantAdmin):
        if not p.participant.admin_rights.add_admins:
            await event.reply(strings.CAN_PROMOTE)
            return False
        return True

    else:
        await event.reply(strings.NOT_ADMIN)
        return False


async def cb_can_add_admins(event, user_id):
    try:
        p = await meow(GetParticipantRequest(event.chat_id, user_id))
    except UserNotParticipantError:
        return False
    if (
        isinstance(p.participant, types.ChannelParticipantCreator)
        or user_id in DEV_USERS
    ):
        return True
    elif isinstance(p.participant, types.ChannelParticipantAdmin):
        if not p.participant.admin_rights.add_admins:
            await event.answer(strings.CAN_PROMOTE, alert=True)
            return False
        return True
    else:
        await event.answer(strings.NOT_ADMIN)
        return False


@exception
async def can_ban_users(event, user_id, chat_id=None):
    if chat_id is not None:
        chat_id = chat_id
    else:
        chat_id = event.chat_id
    try:
        p = await meow(GetParticipantRequest(chat_id, user_id))
    except UserNotParticipantError:
        return False
    if (
        isinstance(p.participant, types.ChannelParticipantCreator)
        or user_id in DEV_USERS
    ):
        return True
    elif isinstance(p.participant, types.ChannelParticipantAdmin):
        if not p.participant.admin_rights.ban_users:
            await event.reply(strings.CAN_BAN)
            return False
        return True
    else:
        await event.reply(strings.NOT_ADMIN)
        return False


async def cb_can_ban_users(event, user_id):
    try:
        p = await meow(GetParticipantRequest(event.chat_id, user_id))
    except UserNotParticipantError:
        return False
    if (
        isinstance(p.participant, types.ChannelParticipantCreator)
        or user_id in DEV_USERS
    ):
        return True
    elif isinstance(p.participant, types.ChannelParticipantAdmin):
        if not p.participant.admin_rights.ban_users:
            await event.answer(strings.CAN_BAN, alert=True)
            return False
        return True
    else:
        await event.answer(strings.NOT_ADMIN, alert=True)
        return False


@exception
async def can_change_info(event, user_id, chat_id=None):
    if chat_id is not None:
        chat_id = chat_id
    else:
        chat_id = event.chat_id

    try:
        p = await meow(GetParticipantRequest(chat_id, user_id))
    except UserNotParticipantError:
        return False
    if (
        isinstance(p.participant, types.ChannelParticipantCreator)
        or user_id in DEV_USERS
    ):
        return True
    elif isinstance(p.participant, types.ChannelParticipantAdmin):
        if not p.participant.admin_rights.change_info:
            await event.reply(strings.CAN_CHANGE_INFO)
            return False
        return True
    else:
        await event.reply(strings.NOT_ADMIN)
        return False


async def cb_can_change_info(event, user_id):
    try:
        p = await meow(GetParticipantRequest(event.chat_id, user_id))
    except UserNotParticipantError:
        return False
    if (
        isinstance(p.participant, types.ChannelParticipantCreator)
        or user_id in DEV_USERS
    ):
        return True
    elif isinstance(p.participant, types.ChannelParticipantAdmin):
        if not p.participant.admin_rights.change_info:
            await event.answer(strings.CAN_CHANGE_INFO, alert=True)
            return False
        return True
    else:
        await event.answer(strings.NOT_ADMIN, alert=True)
        return False


@exception
async def is_owner(event, user_id, chat_id=None):
    if chat_id is not None:
        chat_id = chat_id
        title = await GetChat(chat_id)
    else:
        chat_id = event.chat_id
        title = event.chat.title
    try:
        p = await meow(GetParticipantRequest(chat_id, user_id))
    except UserNotParticipantError:
        return False
    if (
        isinstance(p.participant, types.ChannelParticipantCreator)
        or user_id in DEV_USERS
    ):
        return True
    else:
        await event.reply(f"You need to be the chat owner of {title} to do this.")
        return False


async def cb_is_owner(event, user_id):
    try:
        p = await meow(GetParticipantRequest(event.chat_id, user_id))
    except UserNotParticipantError:
        return False
    if (
        isinstance(p.participant, types.ChannelParticipantCreator)
        or user_id in DEV_USERS
    ):
        return True
    else:
        await event.answer(
            f"You need to be the chat owner of {event.chat.title} to do this.",
            alert=True,
        )
        return False


async def can_delete_msg(event, user_id):
    try:
        p = await meow(GetParticipantRequest(event.chat_id, user_id))
    except UserNotParticipantError:
        return False
    if (
        isinstance(p.participant, types.ChannelParticipantCreator)
        or user_id in DEV_USERS
    ):
        return True
    elif isinstance(p.participant, types.ChannelParticipantAdmin):
        if not p.participant.admin_rights.delete_messages:
            await event.reply(strings.CAN_DELETE)
            return False
        return True
    else:
        await event.reply(strings.NOT_ADMIN)
        return False


@exception
async def is_admin(event, user_id, pm_mode: bool = False):

    chat_id = event.chat_id

    if not pm_mode:
        if event.is_private:
            return True

    cached_admin_status = await get_admin_cache(event, user_id)
    if cached_admin_status is not None:
        return cached_admin_status

    try:
        p = await meow(GetParticipantRequest(chat_id, user_id))
    except UserNotParticipantError:
        return False

    is_admin = isinstance(p.participant, types.ChannelParticipantAdmin) or isinstance(
        p.participant, types.ChannelParticipantCreator
    )

    await update_admin_cache(chat_id, user_id, is_admin)

    return is_admin


async def get_admin_cache(event, user_id):
    cache_data = await cache_collection.find_one(
        {"chat_id": event.chat_id, "user_id": user_id}
    )
    if cache_data:
        return cache_data["is_admin"]
    return None


async def update_admin_cache(chat_id, user_id, is_admin):
    await cache_collection.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$set": {"is_admin": is_admin, "last_updated": datetime.now()}},
        upsert=True,
    )


async def cb_is_admin(event, user_id):
    try:
        p = await meow(GetParticipantRequest(event.chat_id, user_id))
    except UserNotParticipantError:
        return False
    if isinstance(p.participant, types.ChannelParticipantAdmin) or isinstance(
        p.participant, types.ChannelParticipantCreator
    ):
        return True
    else:
        await event.answer(strings.NOT_ADMIN, alert=True)
        return False


async def can_manage_topics(event, user_id):
    try:
        p = await meow(GetParticipantRequest(event.chat_id, user_id))
    except UserNotParticipantError:
        return False
    if (
        isinstance(p.participant, types.ChannelParticipantCreator)
        or user_id in DEV_USERS
    ):
        return True
    elif isinstance(p.participant, types.ChannelParticipantAdmin):
        if not p.participant.admin_rights.manage_topics:
            await event.reply(strings.NOT_TOPIC)
            return False
        return True
    else:
        await event.reply(strings.NOT_ADMIN)
        return False


async def update_cache_periodically():
    while True:
        cursor = cache_collection.find({})
        async for entry in cursor:
            chat_id = entry["chat_id"]
            user_id = int(entry["user_id"])

            try:
                p = await meow(GetParticipantRequest(chat_id, user_id))
                is_admin = isinstance(
                    p.participant, types.ChannelParticipantAdmin
                ) or isinstance(p.participant, types.ChannelParticipantCreator)
                await update_admin_cache(chat_id, user_id, is_admin)
            except UserNotParticipantError:
                pass
            except ValueError:
                pass
            except errors.ChatAdminRequiredError:
                pass
            except errors.ChannelPrivateError:
                pass
            except Exception as e:
                LOGGER.error("Error in admin cache periodically:", e)

        await asyncio.sleep(600)  # 10 minutes


asyncio.get_event_loop().create_task(update_cache_periodically())
