


from misskaty import app
from pyrogram import filters
import base64
import requests


# Command to upload images and animations (GIFs) to Imgur
@app.on_message(filters.command("imgur"))
async def imgur(client, message):
    # Check if a reply exists
    msg = await message.reply_text(
      "🎉 Please patience. trying to upload..."
    )
    if message.reply_to_message and message.reply_to_message.photo:
        # Download the photo
        photo_path = await message.reply_to_message.download()
        # Read the photo file and encode as base64
        with open(photo_path, "rb") as file:
            data = file.read()
            base64_data = base64.b64encode(data)
        # Set API endpoint and headers for image upload
        url = "https://api.imgur.com/3/image"
        headers = {"Authorization": "Client-ID a10ad04550b0648"}
        # Upload image to Imgur and get URL
        response = requests.post(url, headers=headers, data={"image": base64_data})
        result = response.json()
        await msg.edit_text(result["data"]["link"])
    elif message.reply_to_message and message.reply_to_message.animation:
        # Download the animation (GIF)
        animation_path = await message.reply_to_message.download()
        # Read the animation file and encode as base64
        with open(animation_path, "rb") as file:
            data = file.read()
            base64_data = base64.b64encode(data)
        # Set API endpoint and headers for animation upload
        url = "https://api.imgur.com/3/image"
        headers = {"Authorization": "Client-ID a10ad04550b0648"}
        # Upload animation to Imgur and get URL
        response = requests.post(url, headers=headers, data={"image": base64_data})
        result = response.json()
        await msg.edit_text(result["data"]["link"])
    else:
        await msg.edit_text("Please reply to a photo or animation (GIF) to upload to Imgur.")




__mod_name__ = 'Imgur'

__help__ = """
✨ *Imgur uploader*:

/imgur:
To upload image & gif to imgur.com
"""
