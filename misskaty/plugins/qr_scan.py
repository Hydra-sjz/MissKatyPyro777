import os
import cv2
import qrcode
from PIL import Image
import io
from pyrogram import Client, filters

from pyrogram.types import Message
from misskaty import app


#TEXT TO QR CODE
def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="black")

    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    return img_bytes

@app.on_message(filters.command("txt_qr"))
def qr_handler(client, message: Message):
    command_text = message.command
    if len(command_text) > 1:
        input_text = " ".join(command_text[1:])
        qr_image = generate_qr_code(input_text)
        message.reply_photo(qr_image, caption="Here's your QR Code")
    else:
        message.reply_text("Please provide the text for the QR code after the command. Example usage: /qr text")


#QR_CODE TO TEXT
@app.on_message(filters.command('qr_txt'))
async def qr(c, m):
    if " " in m.text:
        tdl = await m.reply_text("`Please wait...`")
        text = str(m.text).split(" ", 1)[1]
        qr = qrcode.QRCode(version=None,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=10, border=4)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qr.png')
        try:
            await c.send_photo(m.chat.id, 'qr.png')
        except:
            await c.send_document(m.chat.id, 'qr.png')
        os.remove('qr.png')
    elif m.reply_to_message.text:
        text = m.reply_to_message.text
        qr = qrcode.QRCode(version=None,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=10, border=4)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qr.png')
        try:
            await c.send_photo(m.chat.id, 'qr.png')
        except:
            await c.send_document(m.chat.id, 'qr.png')
        os.remove('qr.png')
    elif not m.reply_to_message:
        await m.reply(
            '**Hah! What to do with empty command?\nReply an image to scan or send text along with command to make qr.**')
    elif m.reply_to_message.photo:
        x = await m.reply_text("Processing...")
        try:
            d = cv2.QRCodeDetector()
            qr_code = await m.reply_to_message.download()
            val, p, s = d.detectAndDecode(cv2.imread(qr_code))
            await x.edit(val)
        except:
            await x.edit("Failed to get data")
        os.remove(qr_code)
    else:
        await m.reply('Unsupported!')
