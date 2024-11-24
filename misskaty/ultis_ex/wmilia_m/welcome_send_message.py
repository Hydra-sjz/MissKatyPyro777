from misskaty import BOT_USERNAME, app as pgram
#from Emilia.helper.note_helper.note_misc_helper import preview_text_replace
from misskaty.ultis_ex.wmilia_m.welcome_fillings import Welcomefillings

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def SendWelcomeMessage(
    message, NewUserJson, content, text, data_type, reply_markup
):
    chat_id = message.chat.id
    text = await Welcomefillings(message, text, NewUserJson)

   # preview, text = await preview_text_replace(text)

    if "{rules}" in text:
        text = text.replace("{rules}", "")
        button = [
            [
                InlineKeyboardButton(
                    text="Rules",
                    url=f"http://t.me/{BOT_USERNAME}?start=rules_{chat_id}",
                )
            ]
        ]
        reply_markup = InlineKeyboardMarkup(button)

    SentMessage = None

    if data_type == 1:
        SentMessage = await pgram.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup,
        )

    elif data_type == 2:
        SentMessage = await pgram.send_sticker(
            chat_id=chat_id,
            sticker=content,
            reply_markup=reply_markup,
        )

    elif data_type == 3:
        SentMessage = await pgram.send_animation(
            chat_id=chat_id,
            animation=content,
            caption=text,
            reply_markup=reply_markup,
        )

    elif data_type == 4:
        SentMessage = await pgram.send_document(
            chat_id=chat_id,
            document=content,
            caption=text,
            reply_markup=reply_markup,
        )

    elif data_type == 5:
        SentMessage = await pgram.send_photo(
            chat_id=chat_id,
            photo=content,
            caption=text,
            reply_markup=reply_markup,
        )

    elif data_type == 6:
        SentMessage = await pgram.send_audio(
            chat_id=chat_id,
            audio=content,
            caption=text,
            reply_markup=reply_markup,
        )
    elif data_type == 7:
        SentMessage = await pgram.send_voice(
            chat_id=chat_id,
            voice=content,
            caption=text,
            reply_markup=reply_markup,
        )

    elif data_type == 8:
        SentMessage = await pgram.send_video(
            chat_id=chat_id,
            video=content,
            caption=text,
            reply_markup=reply_markup,
        )

    elif data_type == 9:
        SentMessage = await pgram.send_video_note(
            chat_id=chat_id,
            video_note=content,
            reply_markup=reply_markup,
        )

    return SentMessage
