import time
from datetime import datetime
from functools import wraps

from pyrogram import Client, enums, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden
from pyrogram.types import (
    CallbackQuery,
    ChatMemberUpdated,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telethon import errors

from Emilia import BOT_ID, LOGGER, db, pgram, telethn
from Emilia.helper.chat_status import anon_admin_checker
from Emilia.helper.get_data import GetChat
from Emilia.mongo.connection_mongo import GetConnectedChat
from Emilia.strings import error_messages


async def usage_string(message, func) -> None:
    await message.reply(
        f"{func.description}\n\n**Usage:**\n`{func.usage}`\n\n**Example:**\n`{func.example}`"
    )


def description(description_doc: str):
    def wrapper(func):
        func.description = description_doc
        return func

    return wrapper


def usage(usage_doc: str):
    def wrapper(func):
        func.usage = usage_doc
        return func

    return wrapper


def example(example_doc: str):
    def wrapper(func):
        func.example = example_doc
        return func

    return wrapper


def exception(func):
    async def wrapped(event, *args, **kwargs):
        try:
            return await func(event, *args, **kwargs)
        except Exception as e:
            error_message = error_messages.get(type(e), str(e))

            if (
                isinstance(e, errors.RPCError)
                and e.code == 403
                and "CHAT_SEND_DOCS_FORBIDDEN" in e.message
            ):
                error_message = "I am not allowed to send documents in this chat. Please make me an admin to do so."

            await event.reply(error_message)

    return wrapped


# log channel stuff
mongo_collection = db.logchannels


async def get_telegram_info_telethon(event):
    id_ = None
    if not event.is_private:
        try:
            id_ = event.message.id
        except AttributeError:
            id_ = "meow"

    try:
        first_name = event.sender.first_name if event.sender else None
        admin_id = event.sender_id if event.sender else None
    except AttributeError:
        first_name = None
        admin_id = None

    chat_id = event.chat_id
    if not str(chat_id).startswith("-100"):
        chat_id = await GetConnectedChat(admin_id)

    title = await GetChat(chat_id) or event.chat.title

    return (chat_id, title, first_name, admin_id, id_)


async def get_telegram_info_pyrogram(client, event):
    id_ = "connected"
    if not event.chat.type == enums.ChatType.PRIVATE:
        try:
            id_ = event.id
        except AttributeError:
            id_ = "manual"

    try:
        first_name = event.from_user.first_name if event.from_user else None
        admin_id = event.from_user.id if event.from_user else None
    except AttributeError:
        first_name = None
        admin_id = None

    chat_id = event.chat.id
    if not str(chat_id).startswith("-100"):
        chat_id = await GetConnectedChat(admin_id)

    title = await GetChat(chat_id) or event.chat.title

    return (chat_id, title, first_name, admin_id, id_)


def is_telethon_client(client):
    return client.__module__.startswith("telethon")


async def get_telegram_info(client, event):
    if is_telethon_client(client):
        return await get_telegram_info_telethon(event)
    else:
        return await get_telegram_info_pyrogram(client, event)


def logging(func):
    async def wrapper(*args, **kwargs):
        log_message = " "
        client = args[0]
        event = (
            args[0]
            if is_telethon_client(client)
            else args[1] if args[1] is not None else args[0]
        )

        chat_id, chat_title, admin_name, admin_id, message_id = await get_telegram_info(
            client, event
        )

        chat_data = await mongo_collection.find_one({"chat_id": chat_id})
        if not (chat_data and "channel_id" in chat_data):
            return await func(*args, **kwargs)
        try:

            result_tuple = await func(*args, **kwargs)
            if len(result_tuple) == 3:
                event_type, user_id, user_name = result_tuple
            else:
                event_type, user_id, user_name, adminid, adminname = result_tuple
                admin_id = adminid
                admin_name = adminname
        except Exception as e:
            LOGGER.error(e)
            return

        datetime_fmt = "%H:%M - %d-%m-%Y"

        log_message += f"**{chat_title}** `{chat_id}`\n#{event_type}\n"

        if admin_name and admin_id is not None:
            clear_admin_name = admin_name.replace("[", "").replace("]", "")
            log_message += f"\n**Admin**: [{clear_admin_name}](tg://user?id={admin_id})"

        if user_name and user_id:
            clear_user_name = user_name.replace("[", "").replace("]", "")
            log_message += f"\n**User**: [{clear_user_name}](tg://user?id={user_id})"

        if user_id:
            log_message += f"\n**User ID**: `{user_id}`"

        log_message += (
            f"\n**Event Stamp**: `{datetime.utcnow().strftime(datetime_fmt)}`"
        )

        try:
            if message_id and message_id != "connected" and message_id != "manual":
                if event.chat.username:
                    log_message += f"\n**Link**: [click here](https://t.me/{event.chat.username}/{message_id})"
                else:
                    cid = str(chat_id).replace("-100", "")
                    log_message += (
                        f"\n**Link**: [click here](https://t.me/c/{cid}/{message_id})"
                    )
            elif message_id == "connected":
                log_message += "\n**Link**: No message link for connected commands."
            elif message_id == "manual":
                log_message += "\n**Link**: No message link for manual actions."
        except AttributeError:
            pass

        await telethn.send_message(
            chat_data["channel_id"], log_message, link_preview=False
        )

    return wrapper


@Client.on_chat_member_updated(filters.group)
@logging
async def NewMemer(client: Client, message: ChatMemberUpdated):

    if message.new_chat_member and not message.old_chat_member:
        if (message.from_user and message.new_chat_member.user):
            if (message.new_chat_member.user.id != message.from_user.id):
                return (
                    "WELCOME",
                    message.new_chat_member.user.id,
                    message.new_chat_member.user.first_name,
                    message.from_user.id,
                    message.from_user.first_name,
                )

        return (
            "WELCOME",
            message.new_chat_member.user.id,
            message.new_chat_member.user.first_name,
            None,
            None,
        )

    if not message.new_chat_member and message.old_chat_member:
        return (
            "GOODBYE",
            message.old_chat_member.user.id,
            message.old_chat_member.user.first_name,
            None,
            None,
        )

    if message.old_chat_member and message.new_chat_member:
        if (
            message.old_chat_member.status == ChatMemberStatus.MEMBER
            and message.new_chat_member.status == ChatMemberStatus.ADMINISTRATOR
        ):
            admin_title = message.new_chat_member.promoted_by.first_name
            admin_id = message.new_chat_member.promoted_by.id
            if admin_id == BOT_ID:
                return
            return (
                "PROMOTE",
                message.old_chat_member.user.id,
                message.old_chat_member.user.first_name,
                admin_id,
                admin_title,
            )

        elif (
            message.old_chat_member.status == ChatMemberStatus.ADMINISTRATOR
            and message.new_chat_member.status == ChatMemberStatus.MEMBER
        ):
            admin_title = message.from_user.first_name
            admin_id = message.from_user.id
            if admin_id == BOT_ID:
                return
            return (
                "DEMOTE",
                message.old_chat_member.user.id,
                message.old_chat_member.user.first_name,
                admin_id,
                admin_title,
            )

        elif (
            message.old_chat_member.status != ChatMemberStatus.BANNED
            and message.new_chat_member.status == ChatMemberStatus.BANNED
        ):
            admin_title = message.from_user.first_name
            admin_id = message.from_user.id
            if admin_id == BOT_ID:
                return
            return (
                "BAN",
                message.old_chat_member.user.id,
                message.old_chat_member.user.first_name,
                admin_id,
                admin_title,
            )

    elif message.old_chat_member.status == ChatMemberStatus.BANNED:
        admin_title = message.from_user.first_name
        admin_id = message.from_user.id
        if admin_id == BOT_ID:
            return
        return (
            "UNBAN",
            message.old_chat_member.user.id,
            message.old_chat_member.user.first_name,
            admin_id,
            admin_title,
        )


message_history = {}


def rate_limit(messages_per_window: int, window_seconds: int):
    """
    Decorator that limits the rate at which a function can be called.

    Args:
        messages_per_window (int): The maximum number of messages allowed within the time window.
        window_seconds (int): The duration of the time window in seconds.

    Returns:
        function: The decorated function.

    Example:
        @rate_limit(40, 60)
        async def my_function(client, message):
            # Function implementation
    """

    def decorator(func):

        async def wrapper(*args, **kwargs):
            client = args[0]
            if is_telethon_client(client):
                user_id = args[0].sender_id
            else:
                user_id = (
                    args[1].from_user.id
                    if args[1] is not None
                    else args[0].from_user.id
                )

            current_time = time.time()

            if user_id not in message_history:
                message_history[user_id] = []

            message_history[user_id] = [
                t
                for t in message_history[user_id]
                if current_time - t <= window_seconds
            ]

            if len(message_history[user_id]) >= messages_per_window:
                LOGGER.error(
                    f"Rate limit exceeded for user {user_id}. Allowed {messages_per_window} updates in {window_seconds} seconds for {func.__name__}"
                )
                return

            message_history[user_id].append(current_time)
            await func(*args, **kwargs)

        return wrapper

    return decorator


# leave chat if cannot write
def leavemute(func):
    @wraps(func)
    async def capture(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except ChatWriteForbidden:
            await pgram.leave_chat(message.chat.id)
            return

    return capture


callback_registry = {}


def register_callback(func, message):
    callback_name = f"check_admin_callback_{func.__name__}_{message.id}"

    async def callback_handler(_: Client, callback_query: CallbackQuery):
        user_id = callback_query.from_user.id
        chat_id = callback_query.message.chat.id

        if await anon_admin_checker(chat_id, user_id):
            await func(_, message)
            await callback_query.message.delete()
        else:
            await callback_query.answer("You are not an admin", show_alert=True)

    pgram.on_callback_query(
        filters.create(lambda _, __, query: query.data == callback_name)
    )(callback_handler)

    return callback_name


def anonadmin_checker(func):
    @wraps(func)
    async def wrapper(client, message):
        if message.sender_chat or (
            message.sender_chat is None and message.from_user.id == 1087968824
        ):
            button = [
                [
                    InlineKeyboardButton(
                        text="Click to prove admin",
                        callback_data=register_callback(func, message),
                    )
                ]
            ]
            await message.reply(
                text="You are anonymous. Tap this button to confirm your identity.",
                reply_markup=InlineKeyboardMarkup(button),
            )

            return
        else:
            return await func(client, message)

    return wrapper
