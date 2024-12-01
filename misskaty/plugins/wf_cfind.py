import asyncio
from pyrogram import filters, Client, types as t
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from misskaty import app as bot
from misskaty import user_collection, collection

@bot.on_message(filters.command(["cfind"]))
async def cfind(_, message: t.Message):
    if len(message.command) < 2:
        return await message.reply_text("𝖯𝗅𝖾𝖺𝗌𝖾 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝗍𝗁𝖾 𝖺𝗇𝗂𝗆𝖾 𝗇𝖺𝗆𝖾✨", quote=True)

    anime_name = " ".join(message.command[1:])
    characters = await collection.find({'anime': anime_name}).to_list(length=None)

    if not characters:
        return await message.reply_text(f"𝖭𝗈 𝖼𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋𝗌 𝖿𝗈𝗎𝗇𝖽 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝖺𝗇𝗂𝗆𝖾 ❎ {anime_name}.", quote=True)

    captions = [
        f"🎏 𝖭𝖺𝗆𝖾: {char['name']}\n🪅 𝖨𝖣: {char['id']}\n🧩 𝖱𝖺𝗋𝗂𝗍𝗒: {char['rarity']}\n"
        for char in characters
    ]
    response = "\n".join(captions)
    await message.reply_text(f"🍁 𝖢𝗁𝖺𝗋𝖺𝖼𝗍𝖾𝗋𝗌 𝖿𝗋𝗈𝗆 {anime_name}:\n\n{response}", quote=True)
