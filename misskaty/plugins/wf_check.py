import urllib.request
import os
from pymongo import ReturnDocument
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler
from misskaty import application, collection, dbw as db, user_collection
from misskaty import app as bot
from misskaty.vars import SUDO as sudo_users, LOG_CHANNEL as CHARA_CHANNEL_ID
from pyrogram import Client, filters, types as t

async def check_character(update: Update, context: CallbackContext) -> None:
    try:
        args = context.args
        if len(args) != 1:
            await update.message.reply_text('Incorrect format. Please use: /check character_id')
            return
        character_id = args[0]
        character = await collection.find_one({'id': character_id})
        if character:
            global_count = await user_collection.count_documents({'characters.id': character['id']})
            response_message = (
                f"<b>Lᴏᴏᴋ Aᴛ Tʜɪs Wᴀɪғᴜ....!!</b>\n\n"
    f"<b>{character['id']}:</b> {character['name']}\n"
    f"<b>{character['anime']}</b>\n"
    f"﹙<b>{character['rarity'][0]} 𝙍𝘼𝙍𝙄𝙏𝙔:</b> {character['rarity'][2:]})"
            )

            # The `if` and following `elif` blocks need to be indented at the same level
            if '👘' in character['name']:
                response_message += "\n\n👘𝑲𝒊𝒎𝒐𝒏𝒐👘 " 
            elif '☃️' in character['name']:
                response_message += "\n\n☃️𝑾𝒊𝒏𝒕𝒆𝒓☃️"
            elif '🐰' in character['name']:
                response_message += "\n\n🐰𝑩𝒖𝒏𝒏𝒚🐰"
            elif '🎮' in character['name']:
                response_message += "\n\n 🎮𝑮𝒂𝒎𝒆🎮 "
            elif '🎄' in character['name']:
                response_message += "\n\n🎄𝑪𝒓𝒊𝒔𝒕𝒎𝒂𝒔🎄"
            elif '🎃' in character['name']:
                response_message += "\n\n🎃𝑯𝒆𝒍𝒍𝒐𝒘𝒆𝒆𝒏🎃"
            elif '🏖️' in character['name']:
                response_message += "\n\n🏖️𝑺𝒖𝒎𝒎𝒆𝒓🏖️ "
            elif '🧹' in character['name']:
                response_message += "\n\n🧹𝑴𝒂𝒅𝒆🧹"
            elif '🥻' in character['name']:
                response_message += "\n\n🥻𝑺𝒂𝒓𝒆𝒆🥻"
            elif '☔' in character['name']: # Removed extra quote here
                response_message += "\n\n☔𝑴𝒐𝒏𝒔𝒐𝒐𝒏☔"
            elif '🎒' in character['name']:
                response_message += "\n\n🎒𝑺𝒄𝒉𝒐𝒐𝒍🎒"
            elif '🎩' in character['name']:
                response_message += "\n\n🎩𝑻𝒖𝒙𝒆𝒅𝒐🎩"
            elif '👥' in character['name']:
                response_message += "\n\n👥𝐃𝐮𝐨👥"
            elif '🤝🏻' in character['name']:
                response_message += "\n\n🤝🏻𝐆𝐫𝐨𝐮𝐩🤝🏻"
            elif '👑' in character['name']:
                response_message += "\n\n👑𝑳𝒐𝒓𝒅👑"
            elif '🩺' in character['name']:
                response_message += "\n\n🩺𝑵𝒖𝒓𝒔𝒆🩺"
            elif '💍' in character['name']:
                response_message += "\n\n💍𝑾𝒆𝒅𝒅𝒊𝒏𝒈💍"
            elif '🎊' in character['name']:
                response_message += "\n\n🎊𝑪𝒉𝒆𝒆𝒓𝒍𝒆𝒂𝒅𝒆𝒓𝒔🎊"
            elif '⚽' in character['name']:
                response_message += "\n\n⚽𝑺𝒐𝒄𝒄𝒆𝒓⚽"
            elif '🏀' in character['name']:
                response_message += "\n\n🏀𝑩𝒂𝒔𝒌𝒆𝒕𝒃𝒂𝒍𝒍🏀"
            elif '💐' in character['name']:
                response_message += "\n\n💐𝑮𝒓𝒐𝒐𝒎💐"
            elif '🥂' in character['name']:
                response_message += "\n\n🥂𝑷𝒂𝒓𝒕𝒚🥂"
            elif '💞' in character['name']:
                response_message += "\n\n💞𝑽𝒂𝒍𝒆𝒏𝒕𝒊𝒏𝒆💞"

            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("Globally Grabbed", callback_data=f"slaves_{character['id']}_{global_count}")]
            ])

            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=character['img_url'],
                caption=response_message,
                parse_mode='HTML',
                reply_markup=keyboard
            )
        else:
            await update.message.reply_text('Wrong id.')

    except Exception as e:
        await update.message.reply_text(f'Error: {str(e)}')
        
async def handle_callback_query(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data.split('_')
    if data[0] == 'slaves':
        character_id = data[1]
        global_count = data[2]
        await query.answer(f"⚡️ Globally Grabbed : {global_count}x.", show_alert=True)

CHECK_HANDLER = CommandHandler('check', check_character, block=False)
application.add_handler(CallbackQueryHandler(handle_callback_query, pattern='slaves_', block=False))
application.add_handler(CHECK_HANDLER)


from pyrogram import Client, filters
from misskaty import user_collection
from misskaty import app

OWNER_ID = 784589736  # Replace with the actual owner ID

async def get_users_by_character(character_id):
    try:
        cursor = user_collection.find(
            {'characters.id': character_id}, 
            {'_id': 0, 'id': 1, 'name': 1, 'username': 1, 'characters.$': 1}
        )
        users = await cursor.to_list(length=None)
        return users
    except Exception as e:
        print("Failed to get users by character:", e)
        return []

@app.on_message(filters.command(["ik"]) & filters.user(OWNER_ID))
async def find_users(_, message):
    if len(message.command) < 2:
        await message.reply_text("Please provide the character ID.", quote=True)
        return

    character_id = message.command[1]
    users = await get_users_by_character(character_id)

    if users:
        response = ""
        for user in users:
            user_id = user['id']
            name = user.get('first_name', 'N/A')
            username = user.get('username', 'N/A')
            character = user['characters'][0]
            character_name = character.get('name', 'N/A')
            response += f"{name} [`{user_id}`]\n\n"
        await message.reply_text(f"Users with character ID {character_id}:\n\n{response}", quote=True)
    else:
        await message.reply_text(f"No users found with character ID: {character_id}", quote=True)
