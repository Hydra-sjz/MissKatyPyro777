"""
 * @author        yasir <yasiramunandar@gmail.com>
 * @date          2022-12-01 09:12:27
 * @projectName   MissKatyPyro
 * Copyright @YasirPedia All rights reserved
"""
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant, UserIsBlocked
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from misskaty import app
#from config import CHANNEL_ID


cap = """
Before entering the Group there is an honesty Rules,
please read This!

**The rules:**
──────────────────
• ⚠️ NO SPAMMING

• 🌊 NO FLOODS

• 🚯 NO PROMOTION!

•=•WARN + BAN•=•
──────────────────
🚫Never do Unwanted pm to any  <b>Admins Or Members.</b>
`if any one coming to your pm to messaging? [Block, Report] and you can report to my group
example: 
@admin his user_name/id  is coming my pm (and your type complaint)
🚫Don't send any other
Telegram, Whatsapp group channels links..
🚫No any types of promotions. 
──────────────────

have you read the Rules? 
Then Click The Approve Botton!
Thank you ❤️

**Powered by: @XBOTS_X**
"""



# Filters Approve User by bot in channel 
@app.on_chat_join_request(filters.group)
async def approve_join_chat(c, m):
    try:
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Approve Me", callback_data=f"approve_{m.chat.id}"
                    ),
                    InlineKeyboardButton(
                        text="Decline Me", callback_data=f"declined_{m.chat.id}"
                    ),
                ]
            ]
        )
        await c.send_message(
            m.from_user.id,
            f"{cap}",
            disable_web_page_preview=True,
            reply_markup=markup,
        )
    except UserIsBlocked:
        await m.decline()


@app.on_callback_query(filters.regex(r"^approve"))
async def approve_chat(c, q):
    _, chat = q.data.split("_")
    try:
        await q.message.edit(
            "🎉 Congratulations\n\n🔅 Now your Request for <b>♣️Music🎵Galaxy♣️</b> Group is Successfully Accepted✅\nNow you can request your song's in Group\n🎧 https://t.me/songdownload_group"
        )
        await c.approve_chat_join_request(chat, q.from_user.id)
    except UserAlreadyParticipant:
        await q.message.edit(
            "You are already Joined in the group, So Go here 🎧 https://t.me/songdownload_group"
        )
    except Exception as err:
        await q.message.edit(err)


@app.on_callback_query(filters.regex(r"^declined"))
async def decline_chat(c, q):
    _, chat = q.data.split("_")
    try:
        await q.message.edit(
            "Well, you were rejected Join Group. Get used to reading yahhh.."
        )
        await c.decline_chat_join_request(chat, q.from_user.id)
    except UserAlreadyParticipant:
        await q.message.edit(
            "You are already in the Music Galaxy group, so no need to press the button below."
        )
    except Exception as err:
        await q.message.edit(err)
