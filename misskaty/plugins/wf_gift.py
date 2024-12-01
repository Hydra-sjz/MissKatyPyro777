from pyrogram import Client, filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler
from misskaty import app as bot
from telegram.ext import MessageHandler, filters
from misskaty import user_collection, application

pending_gifts = {}

async def handle_gift_command(update: Update, context: CallbackContext):
    message = update.message
    sender_id = message.from_user.id

    if not message.reply_to_message:
        await message.reply_html("<b>ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴛᴏ ɢɪғᴛ ᴀ ᴡᴀɪғᴜ!</b>")
        return

    receiver_id = message.reply_to_message.from_user.id
    receiver_username = message.reply_to_message.from_user.username
    receiver_first_name = message.reply_to_message.from_user.first_name

    if sender_id == receiver_id:
        await message.reply_html("<b>ʏᴏᴜ ᴄᴀɴ'ᴛ ɢɪғᴛ ᴀ ᴡᴀɪғᴜ ᴛᴏ ʏᴏᴜʀsᴇʟғ!</b>")
        return

    if len(message.text.split()) != 2:
        await message.reply_html("<b>ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴡᴀɪғᴜ ɪᴅ!</b>")
        return

    character_id = message.text.split()[1]

    sender = await user_collection.find_one({'id': sender_id})

    character = next((character for character in sender.get('characters', []) if isinstance(character, dict) and character.get('id') == character_id), None)

    if not character:
        await message.reply_html("<b>ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜɪs ᴡᴀɪғᴜ ɪɴ ʏᴏᴜʀ ᴄᴏʟʟᴇᴄᴛɪᴏɴ!</b>")
        return

    if sender_id in pending_gifts:
        await message.reply_html("<b>ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ʜᴀᴠᴇ ᴀ ᴘᴇɴᴅɪɴɢ ɢɪғᴛ. ᴘʟᴇᴀsᴇ ᴄᴏɴғɪʀᴍ ᴏʀ ᴄᴀɴᴄᴇʟ ɪᴛ ʙᴇғᴏʀᴇ ɪɴɪᴛɪᴀᴛɪɴɢ ᴀ ɴᴇᴡ ᴏɴᴇ.</b>")
        return

    pending_gifts[sender_id] = {
        'character': character,
        'receiver_id': receiver_id,
        'receiver_username': receiver_username,
        'receiver_first_name': receiver_first_name
    }

    caption = (
        f"<b>ᴅᴏ ʏᴏᴜ ʀᴇᴀʟʟʏ ᴡᴀɴᴛ ᴛᴏ ɢɪғᴛ ᴛʜɪs ᴡᴀɪғᴜ ᴛᴏ {receiver_first_name}?</b>\n"
        f"<b>ɴᴀᴍᴇ: {character['name']}</b>\n"
        f"<b>ɪᴅ: {character['id']}</b>\n"
        f"<b>ʀᴀʀɪᴛʏ: {character['rarity']}</b>"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("ᴄᴏɴғɪʀᴍ ✅", callback_data="confirm_gift")],
            [InlineKeyboardButton("ᴄᴀɴᴄᴇʟ ❌", callback_data="cancel_gift")]
        ]
    )

    await message.reply_text(caption, reply_markup=keyboard, parse_mode='HTML')

async def handle_callback_query(update: Update, context: CallbackContext):
    callback_query = update.callback_query
    sender_id = callback_query.from_user.id

    if sender_id not in pending_gifts:
        await callback_query.answer("No pending gift found.", show_alert=True)
        return

    gift = pending_gifts[sender_id]
    receiver_id = gift['receiver_id']

    if callback_query.data == "confirm_gift":
        sender = await user_collection.find_one({'id': sender_id})
        receiver = await user_collection.find_one({'id': receiver_id})

        sender['characters'].remove(gift['character'])
        await user_collection.update_one({'id': sender_id}, {'$set': {'characters': sender['characters']}})

        if receiver:
            await user_collection.update_one({'id': receiver_id}, {'$push': {'characters': gift['character']}})
        else:
            await user_collection.insert_one({
                'id': receiver_id,
                'username': gift['receiver_username'],
                'first_name': gift['receiver_first_name'],
                'characters': [gift['character']],
            })

        del pending_gifts[sender_id]

        await callback_query.message.edit_text(
    text=f"<b>🎁 ʏᴏᴜ ʜᴀᴠᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ɢɪғᴛᴇᴅ ʏᴏᴜʀ ᴡᴀɪғᴜ ᴛᴏ</b> {gift['receiver_first_name']}!",
    parse_mode='HTML'
)

    elif callback_query.data == "cancel_gift":
        del pending_gifts[sender_id]
        await callback_query.message.edit_text("❌️ Gifting cancelled.")

# Registering handlers with the application
application.add_handler(CommandHandler("gift", handle_gift_command))
application.add_handler(CallbackQueryHandler(handle_callback_query, pattern='^confirm_gift$|^cancel_gift$', block=False))
