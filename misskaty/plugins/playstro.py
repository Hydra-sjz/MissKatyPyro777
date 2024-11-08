import os
import play_scraper
from pyrogram import Client, filters
from pyrogram.types import *





@Client.on_message(filters.private & filters.command("playstore"))
async def playstore(bot, update):
    text = "▶️ __Search play store apps & Games using below inline buttons__.\n\nMy music group : @Music_Galaxy_Dl"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="sᴇᴀʀᴄʜ ʜᴇʀᴇ", switch_inline_query_current_chat="!ply ")],
            [InlineKeyboardButton(text="sᴇᴀʀᴄʜ ɪɴ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀᴛ", switch_inline_query="!ply ")]
        ]
    )
    await update.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )


@Client.on_inline_query()
async def search(bot, update):
    results = play_scraper.search(update.query)
    answers = []
    for result in results:
        details = "**✒️ ᴛɪᴛʟᴇ:** `{}`".format(result["title"]) + "\n" \
        "**ᴅᴇsᴄʀɪᴘᴛɪᴏɴ:** `{}`".format(result["description"]) + "\n" \
        "**ᴀᴘᴘ ɪᴅ:** `{}`".format(result["app_id"]) + "\n" \
        "**ᴅᴇᴠᴇʟᴏᴘᴇʀ:** `{}`".format(result["developer"]) + "\n" \
        "**ᴅᴇᴠᴇʟᴏᴘᴇʀ ɪᴅ:** `{}`".format(result["developer_id"]) + "\n" \
        "**sᴄᴏʀᴇ:** `{}`".format(result["score"]) + "\n" \
        "**ᴘʀɪᴄᴇ:** `{}`".format(result["price"]) + "\n" \
        "**ғᴜʟʟ ᴘʀɪᴄᴇ:** `{}`".format(result["full_price"]) + "\n" \
        "**ғʀᴇᴇ:** `{}`".format(result["free"]) + "\n" \
        "\n" + "ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ @HTGToolBot"
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ᴘʟᴀʏ sᴛᴏʀᴇ", url="https://play.google.com"+result["url"])]]
        )
        try:
            answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description=result.get("description", None),
                    thumb_url=result.get("icon", None),
                    input_message_content=InputTextMessageContent(
                        message_text=details, disable_web_page_preview=True
                    ),
                    reply_markup=reply_markup
                )
            )
        except Exception as error:
            print(error)
    await update.answer(answers)
