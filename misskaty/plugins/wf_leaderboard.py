import os
import random
import html

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from misskaty import (application,
                    user_collection, top_global_groups_collection, top_global_groups_collection, 
                    group_user_totals_collection)

from misskaty.vars import SUDO as SUDO_USERS, OWNER_ID


PHOTO_URL = ["https://telegra.ph//file/e64337bbc6cdac7e6b178.jpg", "https://telegra.ph/file/ed23556d07d33db18402d.jpg", "https://telegra.ph//file/32556c77847dff110577c.jpg", "https://telegra.ph//file/0650844fc5db4049959bc.jpg"]
  
async def global_leaderboard(update: Update, context: CallbackContext) -> None:

    cursor = top_global_groups_collection.aggregate([
        {"$project": {"group_name": 1, "count": 1}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    leaderboard_data = await cursor.to_list(length=10)

    leaderboard_message = "<b>ᴛᴏᴘ 𝟷𝟶 ɢʀᴏᴜᴘs ᴡʜᴏ ɢʀᴀʙʙᴇᴅ ᴍᴏsᴛ ᴄʜᴀʀᴀᴄᴛᴇʀs</b>\n\n"

    for i, group in enumerate(leaderboard_data, start=1):
        group_name = html.escape(group.get('group_name', 'Unknown'))

        if len(group_name) > 10:
            group_name = group_name[:15] + '...'
        count = group['count']
        leaderboard_message += f'{i}. <b>{group_name}</b> ➾ <b>{count}</b>\n'


    photo_url = random.choice(PHOTO_URL)

    await update.message.reply_photo(photo=photo_url, caption=leaderboard_message, parse_mode='HTML')

async def ctop(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id

    cursor = group_user_totals_collection.aggregate([
        {"$match": {"group_id": chat_id}},
        {"$project": {"username": 1, "first_name": 1, "character_count": "$count"}},
        {"$sort": {"character_count": -1}},
        {"$limit": 10}
    ])
    leaderboard_data = await cursor.to_list(length=10)

    leaderboard_message = "<b>ᴛᴏᴘ 𝟷𝟶 ᴜsᴇʀs ᴡʜᴏ ɢʀᴀʙʙᴇᴅ ᴄʜᴀʀᴀᴄᴛᴇʀs ᴍᴏsᴛ ᴛɪᴍᴇ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ....</b>\n\n"

    for i, user in enumerate(leaderboard_data, start=1):
        username = user.get('username', 'Unknown')
        first_name = html.escape(user.get('first_name', 'Unknown'))

        if len(first_name) > 10:
            first_name = first_name[:15] + '...'
        character_count = user['character_count']
        leaderboard_message += f'{i}. <a href="https://t.me/{username}"><b>{first_name}</b></a> ➾ <b>{character_count}</b>\n'

    photo_url = random.choice(PHOTO_URL)

    await update.message.reply_photo(photo=photo_url, caption=leaderboard_message, parse_mode='HTML')


async def leaderboard(update: Update, context: CallbackContext) -> None:
    cursor = user_collection.aggregate([
        {
            "$project": {
                "username": 1,
                "first_name": 1,
                "character_count": {
                    "$cond": {
                        "if": {"$isArray": "$characters"},
                        "then": {"$size": "$characters"},
                        "else": 0
                    }
                }
            }
        },
        {"$sort": {"character_count": -1}},
        {"$limit": 10}
    ])
    leaderboard_data = await cursor.to_list(length=10)

    leaderboard_message = "<b>ᴛᴏᴘ 𝟷𝟶 ᴜsᴇʀs ᴡɪᴛʜ ᴍᴏsᴛ ᴄʜᴀʀᴀᴄᴛᴇʀs</b>\n\n"

    for i, user in enumerate(leaderboard_data, start=1):
        username = user.get('username', 'Unknown')
        first_name = html.escape(user.get('first_name', 'Unknown'))

        if len(first_name) > 10:
            first_name = first_name[:15] + '...'
        character_count = user['character_count']
        leaderboard_message += f'{i}. <a href="https://t.me/{username}"><b>{first_name}</b></a> ➾ <b>{character_count}</b>\n'

    photo_url = random.choice(PHOTO_URL)

    await update.message.reply_photo(photo=photo_url, caption=leaderboard_message, parse_mode='HTML')





async def stats(update: Update, context: CallbackContext) -> None:

    if update.effective_user.id != 784589736:
        await update.message.reply_text("You are not authorized to use this command.")
        return


    user_count = await user_collection.count_documents({})


    group_count = await group_user_totals_collection.distinct('group_id')


    await update.message.reply_text(f'Total Users: {user_count}\nTotal groups: {len(group_count)}')




async def send_users_document(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id) not in SUDO_USERS:
        update.message.reply_text('only For Sudo users...')
        return
    cursor = user_collection.find({})
    users = []
    async for document in cursor:
        users.append(document)
    user_list = ""
    for user in users:
        user_list += f"{user['first_name']}\n"
    with open('users.txt', 'w') as f:
        f.write(user_list)
    with open('users.txt', 'rb') as f:
        await context.bot.send_document(chat_id=update.effective_chat.id, document=f)
    os.remove('users.txt')

async def send_groups_document(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id) not in SUDO_USERS:
        update.message.reply_text('Only For Sudo users...')
        return
    cursor = top_global_groups_collection.find({})
    groups = []
    async for document in cursor:
        groups.append(document)
    group_list = ""
    for group in groups:
        group_list += f"{group['group_name']}\n"
        group_list += "\n"
    with open('groups.txt', 'w') as f:
        f.write(group_list)
    with open('groups.txt', 'rb') as f:
        await context.bot.send_document(chat_id=update.effective_chat.id, document=f)
    os.remove('groups.txt')


application.add_handler(CommandHandler('wctop', ctop, block=False))
application.add_handler(CommandHandler('wfstats', stats, block=False))
application.add_handler(CommandHandler('Topgroups', global_leaderboard, block=False))

application.add_handler(CommandHandler('list', send_users_document, block=False))
application.add_handler(CommandHandler('wgroups', send_groups_document, block=False))


application.add_handler(CommandHandler('wtop', leaderboard, block=False))
