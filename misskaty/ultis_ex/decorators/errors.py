""" WRITTEN BY @pokurt, https://github.com/pokurt"""

import traceback
from functools import wraps

from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden

from misskaty.vars import LOG_GROUP_ID
from misskaty import app, DEV_USERS


def split_limits(text):
    if len(text) < 2048:
        return [text]

    lines = text.splitlines(True)
    small_msg = ""
    result = []
    for line in lines:
        if len(small_msg) + len(line) < 2048:
            small_msg += line
        else:
            result.append(small_msg)
            small_msg = line
    else:
        result.append(small_msg)

    return result


def capture_err(func):
    @wraps(func)
    async def capture(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except ChatWriteForbidden:
            await app.leave_chat(message.chat.id)
            return
        except Exception as err:
            errors = traceback.format_exc()
            error_feedback = split_limits(
                "**ERROR** | `{}` | `{}`\n\n```{}```\n\n```{}```\n".format(
                    0 if not message.from_user else message.from_user.id,
                    0 if not message.chat else message.chat.id,
                    message.text or message.caption,
                    "".join(errors),
                ),
            )
            for x in error_feedback:
                await app.send_message(LOG_GROUP_ID, x)
            raise err

    return capture


# <============================================== IMPORTS =========================================================>
from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

#=====================================================================================================>


# <================================================ FUNCTION =======================================================>
def can_restrict(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if message.from_user.id in DEV_USERS:
            return await func(_, message)

        check = await app.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text(
                "» You're not an admin, Please stay in your limits."
            )

        admin = (
            await app.get_chat_member(message.chat.id, message.from_user.id)
        ).privileges
        if admin.can_restrict_members:
            return await func(_, message)
        else:
            return await message.reply_text(
                "`You don't have permissions to restrict users in this chat."
            )

    return non_admin


# <================================================ END =======================================================>
