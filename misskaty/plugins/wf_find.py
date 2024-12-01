import asyncio
from pyrogram import filters, Client, types as t
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from misskaty import app as bot
from misskaty import user_collection, collection

@bot.on_message(filters.command(["find"]))
async def find(_, message: t.Message):
    if len(message.command) < 2:
        return await message.reply_text("🔖<b>𝖯𝗅𝖾𝖺𝗌𝖾 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝗍𝗁𝖾 𝗐𝖺𝗂𝖿𝗎 𝖨𝖣 </b>☘️", quote=True)

    waifu_id = message.command[1]
    waifu = await collection.find_one({'id': waifu_id})

    if not waifu:
        return await message.reply_text("𝖭𝗈 𝗐𝖺𝗂𝖿𝗎 𝖿𝗈𝗎𝗇𝖽 𝗐𝗂𝗍𝗁 𝗍𝗁𝖺𝗍 𝖨𝖣 ❌", quote=True)

    # Get the top 10 users with the most of this waifu in the current chat
    top_users = await user_collection.aggregate([
        {'$match': {'characters.id': waifu_id}},
        {'$unwind': '$characters'},
        {'$match': {'characters.id': waifu_id}},
        {'$group': {'_id': '$id', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ]).to_list(length=10)

    # Get the usernames of the top users
    usernames = []
    for user_info in top_users:
        user_id = user_info['_id']
        try:
            user = await bot.get_users(user_id)
            usernames.append(user.username if user.username else f"➥ {user_id}")
        except Exception as e:
            print(e)
            usernames.append(f"➥ {user_id}")

    # Construct the caption
    caption = (
        f"🧩 <b>𝖶𝖺𝗂𝖿𝗎 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇:</b>\n\n"
        f"🪭 <b>𝖭𝖺𝗆𝖾:</b> {waifu['name']}\n"

f"⚕️ <b>𝖱𝖺𝗋𝗂𝗍𝗒:</b> {waifu['rarity']}\n"
        f"⚜️ <b>𝖠𝗇𝗂𝗆𝖾:</b> {waifu['anime']}\n"
        f"🪅 <b>𝖨𝖣:</b> {waifu['id']}\n\n"
        f"✳️ <b>𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝗅𝗂𝗌𝗍 𝗈𝖿 𝗎𝗌𝖾𝗋𝗌 𝗐𝗁𝗈 𝗁𝖺𝗏𝖾 𝗍𝗁𝗂𝗌 𝖼𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋 〽️</b>:\n\n"
    )
    for i, user_info in enumerate(top_users):
        count = user_info['count']
        username = usernames[i]
        caption += f"{i + 1}. {username} x{count}\n"

    # Reply with the waifu information and top users
    await message.reply_photo(photo=waifu['img_url'], caption=caption)
