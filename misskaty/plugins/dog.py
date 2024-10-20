import requests
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)

from misskaty import app

close_keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="Rᴇғʀᴇsʜ", callback_data="refresh_dog")],
    ]
)


@app.on_message(filters.command(["dogs", "dog"]))
async def dog(c, m: Message):
    r = requests.get("https://random.dog/woof.json")
    if r.status_code == 200:
        data = r.json()
        dog_url = data["url"]
        if dog_url.endswith(".gif"):
            await m.reply_animation(dog_url, reply_markup=close_keyboard)
        else:
            await m.reply_photo(dog_url, reply_markup=close_keyboard)
    else:
        await m.reply_text("Failed to fetch dog picture 🐕")


@app.on_callback_query(filters.regex("refresh_dog"))
async def refresh_dog(c, m: CallbackQuery):
    r = requests.get("https://random.dog/woof.json")
    if r.status_code == 200:
        data = r.json()
        dog_url = data["url"]
        if dog_url.endswith(".gif"):
            await m.edit_message_animation(dog_url, reply_markup=close_keyboard)
        else:
            await m.edit_message_media(
                InputMediaPhoto(media=dog_url),
                reply_markup=close_keyboard,
            )
    else:
        await m.edit_message_text("Failed to refresh dog picture 🐕")
