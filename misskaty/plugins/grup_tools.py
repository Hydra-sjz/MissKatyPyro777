import os
import textwrap
import time
from datetime import datetime, timedelta
from logging import getLogger

from PIL import Image, ImageChops, ImageDraw, ImageFont
from pyrogram import Client, enums, filters
from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.errors import (
    ChatAdminRequired,
    ChatSendPhotosForbidden,
    ChatWriteForbidden,
    MessageTooLong,
    RPCError,
)
from pyrogram.types import ChatMemberUpdated, InlineKeyboardButton, InlineKeyboardMarkup

from database.greetings_db import is_welcome, toggle_welcome
from database.users_chats_db import db
from misskaty import BOT_USERNAME, app
from misskaty.core.decorator import asyncify, capture_err
from misskaty.helper import fetch, use_chat_lang
from misskaty.vars import COMMAND_HANDLER, SUPPORT_CHAT, OWNER_ID
from utils import temp

LOGGER = getLogger("MissKaty")


def circle(pfp, size=(450, 450)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp


@asyncify
def welcomepic(pic, user, chat, id, uname):
    background = Image.open("assets/WELL2.PNG")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize(
        (450, 450)
    ) 
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('assets/font.ttf', size=50)
    font2 = ImageFont.truetype('assets/font.ttf', size=90)
    draw.text((65, 250), f'NAME : {unidecode(user)}', fill=(255, 255, 255), font=font)
    draw.text((65, 340), f'ID : {id}', fill=(255, 255, 255), font=font)
    draw.text((65, 430), f"USERNAME : {uname}", fill=(255,255,255),font=font)
    pfp_position = (767, 133)  
    background.paste(pfp, pfp_position, pfp)  
    background.save(
        f"downloads/welcome#{id}.png"
    )
    return f"downloads/welcome#{id}.png"


@app.on_chat_member_updated(
    filters.group, group=6
)
@use_chat_lang()
async def member_has_joined(c: Client, member: ChatMemberUpdated, strings):
    if not (
        member.new_chat_member
        and member.new_chat_member.status not in {CMS.RESTRICTED}
        and not member.old_chat_member
    ):
        return
    if not await is_welcome(member.chat.id):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    if user.id == OWNER_ID:
        await c.send_message(
            member.chat.id,
            strings("sudo_join_msg"),
        )
        return
    elif user.is_bot:
        return  # ignore bots
    else:
        if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
            try:
                await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
            except:
                pass
        mention = f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
        joined_date = datetime.fromtimestamp(time.time()).strftime("%Y.%m.%d %H:%M:%S")
        first_name = (
            f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        )
        id = user.id
        dc = user.dc_id or "Member tanpa PP"
        try:
            pic = await app.download_media(
                user.photo.big_file_id, file_name=f"pp{user.id}.png"
            )
        except AttributeError:
            pic = "assets/profilepic.png"
        try:
            welcomeimg = await welcomepic(
                pic, user.first_name, member.chat.title, user.id, strings
            )
            temp.MELCOW[f"welcome-{member.chat.id}"] = await c.send_photo(
                member.chat.id,
                photo=welcomeimg,
                caption=strings("capt_welc").format(
                    umention=mention, uid=user.id, ttl=member.chat.title
                ),
            )
        except Exception as e:
            LOGGER.info(e)
        userspammer = ""
        # Combot API Detection
        try:
            apicombot = (
                await fetch.get(f"https://api.cas.chat/check?user_id={user.id}")
            ).json()
            if apicombot.get("ok") == "true":
                await app.ban_chat_member(
                    member.chat.id, user.id, datetime.now() + timedelta(seconds=30)
                )
                userspammer += strings("combot_msg").format(
                    umention=user.mention, uid=user.id
                )
        except Exception as err:
            LOGGER.error(f"ERROR: {err}")
        if userspammer != "":
            await c.send_message(member.chat.id, userspammer)
        try:
            os.remove(f"downloads/welcome#{user.id}.png")
            os.remove(f"downloads/pp{user.id}.png")
        except Exception:
            pass


@app.on_cmd(["set_welcome"], self_admin=True, group_only=True)
@app.adminsOnly("can_change_info")
async def welcome_toggle_handler(client, message):
    is_enabled = await toggle_welcome(message.chat.id)
    await message.reply_msg(
        f"Welcome messages are now {'enabled' if is_enabled else 'disabled'}."
    )


@app.on_message(filters.command("leave") & filters.user(OWNER_ID))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply("Give me a chat id")
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        pass
    try:
        buttons = [
            [InlineKeyboardButton("Support", url=f"https://t.me/{SUPPORT_CHAT}")]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text="<b>Hi guys, \nOwner I said I have to go! If you want to add this bot again please contact the owner of this bot.</b>",
            reply_markup=reply_markup,
        )
        await bot.leave_chat(chat)
    except Exception as e:
        await message.reply(f"Error - {e}")
        await bot.leave_chat(chat)


# Not to be used
# @app.on_message(filters.command('invite') & filters.user(OWNER_ID))
async def gen_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply("Give me a chat id")
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply("Give Me A Valid Chat ID")
    try:
        link = await bot.create_chat_invite_link(chat)
    except ChatAdminRequired:
        return await message.reply(
            "Invite Link Generation Failed, Iam Not Having Sufficient Rights"
        )
    except Exception as e:
        return await message.reply(f"Error {e}")
    await message.reply(f"Here is your Invite Link {link.invite_link}")


@app.on_message(filters.command(["adminlist"], COMMAND_HANDLER))
@capture_err
async def adminlist(_, message):
    if message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("This command is for groups only")
    try:
        msg = await message.reply_msg(f"Getting admin list in {message.chat.title}..")
        administrators = []
        async for m in app.get_chat_members(
            message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
        ):
            uname = f"@{m.user.username}" if m.user.username else ""
            administrators.append(f"{m.user.first_name} [{uname}]")

        res = "".join(f"💠 {i}\n" for i in administrators)
        return await msg.edit_msg(
            f"Admin in <b>{message.chat.title}</b> ({message.chat.id}):\n{res}"
        )
    except Exception as e:
        await message.reply(f"ERROR: {str(e)}")


@app.on_message(filters.command(["kickme"], COMMAND_HANDLER))
@capture_err
async def kickme(_, message):
    reason = None
    if len(message.text.split()) >= 2:
        reason = message.text.split(None, 1)[1]
    try:
        await message.chat.ban_member(message.from_user.id)
        txt = f"User {message.from_user.mention} kicked himself. Maybe he's frustrated 😕"
        txt += f"\n<b>Alasan</b>: {reason}" if reason else "-"
        await message.reply_text(txt)
        await message.chat.unban_member(message.from_user.id)
    except RPCError as ef:
        await message.reply_text(
            f"It seems there is an error, please report it to my owner. \nERROR: {str(ef)}"
        )
    except Exception as err:
        await message.reply(f"ERROR: {err}")


@app.on_message(filters.command("users") & filters.user(OWNER_ID))
async def list_users(_, message):
    # https://t.me/GetTGLink/4184
    msg = await message.reply("Getting List Of Users")
    users = await db.get_all_users()
    out = "Users Saved In DB Are:\n\n"
    async for user in users:
        out += f"User ID: {user.get('id')} -> {user.get('name')}"
        if user["ban_status"]["is_banned"]:
            out += "( Banned User )"
        out += "\n"
    try:
        await msg.edit_text(out)
    except MessageTooLong:
        with open("users.txt", "w+") as outfile:
            outfile.write(out)
        await message.reply_document("users.txt", caption="List Of Users")
        await msg.delete_msg()


@app.on_message(filters.command("chats") & filters.user(OWNER_ID))
async def list_chats(_, message):
    msg = await message.reply("Getting List Of chats")
    chats = await db.get_all_chats()
    out = "Chats Saved In DB Are:\n\n"
    async for chat in chats:
        out += f"Title: {chat.get('title')} ({chat.get('id')}) "
        if chat["chat_status"]["is_disabled"]:
            out += "( Disabled Chat )"
        out += "\n"
    try:
        await msg.edit_text(out)
    except MessageTooLong:
        with open("chats.txt", "w+") as outfile:
            outfile.write(out)
        await message.reply_document("chats.txt", caption="List Of Chats")
        await msg.delete_msg()
