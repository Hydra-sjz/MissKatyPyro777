import random 
from pyrogram import filters,Client,enums

from misskaty import app

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import ChatPermissions

from misskaty.ultis_ex.nightdb import nightdb,nightmode_on,nightmode_off,get_nightchats 




buttons = InlineKeyboardMarkup([[InlineKeyboardButton("On✅", callback_data="add_night"),InlineKeyboardButton("Off❌", callback_data="rm_night")]])         

@app.on_message(filters.command("shdmsgs") & filters.group)
async def _nivightmode(_, message):
    return await message.reply_photo(photo="https://envs.sh/99a.jpg", caption="__Turn on good morning / good night messages every night and morning 🏙️/🌃__",reply_markup=buttons)
              
     
@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(bot, query: CallbackQuery):
    data = query.data 
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id" : chat_id})
    administrators = []
    async for m in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)     
    if user_id in administrators:   
        if data == "add_night":
            if check_night:        
                await query.message.edit_caption("__this is already enabled this chat.__")
            elif not check_night :
                await nightmode_on(chat_id)
                await query.message.edit_caption("Good morning/night schedule message is enabled ✅") 
        if data == "rm_night":
            if check_night:  
                await nightmode_off(chat_id)      
                await query.message.edit_caption("Disabled ❌")
            elif not check_night:
                await query.message.edit_caption("already desabled this chat❌.") 
            
    
#good_night
async def start_nightmode() :
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for add_chat in chats:
        try:
            await bot.send_photo(
                add_chat,
                photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg",
                caption=f"__Good night 🌠🌜 and sweet dreams 😪😴!__")

        except Exception as e:
            print(f"[bold red] Unable To send message in {add_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(start_nightmode, trigger="cron", hour=7, minute=20) #hour=23, minute=59
scheduler.start()

#good_morning
async def close_nightmode():
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for rm_chat in chats:
        try:
            await bot.send_photo(
                rm_chat,
                photo="https://telegra.ph//file/14ec9c3ff42b59867040a.jpg",
                caption=f"Good morning everyone 🌞🏙️")

        except Exception as e:
            print(f"[bold red] Unable To message {rm_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(close_nightmode, trigger="cron", hour=6, minute=1)
scheduler.start()

