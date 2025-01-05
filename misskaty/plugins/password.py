import random
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from misskaty import app

@app.on_message(filters.command(["genpassword", 'genpw']))
async def password(bot, update):
    message = await update.reply_text(text="`Processing...`")
    
    # Define available characters for password generation
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "1234567890"
    special = "!@#$%^&*()_+"
    
    # Combine all characters
    all_characters = lowercase + uppercase + digits + special
    
    # Check if a length is provided; otherwise, use a random default choice
    if len(update.command) > 1:
        try:
            qw = update.text.split(" ", 1)[1]
            limit = int(qw)
            if limit < 4 or limit > 32:  # Ensure the length is reasonable (between 4 and 32 characters)
                raise ValueError("Password length must be between 4 and 32 characters.")
        except (ValueError, IndexError):
            await message.edit_text("Please provide a valid password length (between 4 and 32 characters).")
            return
    else:
        # Default lengths to choose from
        ST = ["5", "7", "6", "9", "10", "12", "14", "16"]
        qw = random.choice(ST)
        limit = int(qw)
    
    # Generate random password
    random_value = "".join(random.sample(all_characters, limit))
    
    # Prepare the response text
    txt = f"<b>Limit:</b> {str(limit)} \n<b>Password: <code>{random_value}</code></b>"

    # Inline buttons
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton('X BOTS', url='https://t.me/xbots_x')]
    ])
    
    # Edit the message to show the generated password
    await message.edit_text(text=txt, reply_markup=btn, parse_mode=enums.ParseMode.HTML)
