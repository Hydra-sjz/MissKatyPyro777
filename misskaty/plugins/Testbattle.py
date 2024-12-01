from pyrogram import filters
from misskaty import app as bot

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

# Define a dictionary to store the battle data
battles = {}

# Define a function to start a battle
async def start_battle(update: Update, user_id: int, opponent_id: int):
    # Get the user's and opponent's beasts
    user_data = await get_user_data(user_id)
    opponent_data = await get_user_data(opponent_id)
    user_beast = user_data['beasts'][0]  # Assume the first beast is the main beast
    opponent_beast = opponent_data['beasts'][0]

    # Create a battle object
    battle = {
        'user_id': user_id,
        'opponent_id': opponent_id,
        'user_beast': user_beast,
        'opponent_beast': opponent_beast,
        'turn': 'user',  # User's turn first
        'user_hp': user_beast['power'],
        'opponent_hp': opponent_beast['power']
    }

    # Store the battle data
    battles[user_id] = battle

    # Send a message to start the battle
    await update.reply_text("Battle started! It's your turn.")
    await update.reply_text("Your beast: {} (HP: {})".format(user_beast['name'], user_beast['power']))
    await update.reply_text("Opponent's beast: {} (HP: {})".format(opponent_beast['name'], opponent_beast['power']))

    # Create inline buttons for special attacks and normal strikes
    inline_keyboard = [
        [InlineKeyboardButton("Normal Strike", callback_data="normal_strike")],
        [InlineKeyboardButton("Special Attack", callback_data="special_attack")]
    ]
    await update.reply_text("Choose your move:", reply_markup=InlineKeyboardMarkup(inline_keyboard))

# Define a function to handle inline button callbacks
async def battle_callback(update: Update, callback_query: CallbackQuery):
    user_id = update.from_user.id
    battle = battles.get(user_id)

    if battle:
        if callback_query.data == "normal_strike":
            # Calculate the damage dealt
            damage = battle['user_beast']['power'] // 2
            battle['opponent_hp'] -= damage
            await update.reply_text("You dealt {} damage to the opponent's beast!".format(damage))

        elif callback_query.data == "special_attack":
            # Calculate the damage dealt
            damage = battle['user_beast']['power'] * 2
            battle['opponent_hp'] -= damage
            await update.reply_text("You dealt {} damage to the opponent's beast!".format(damage))

        # Check if the opponent's beast is defeated
        if battle['opponent_hp'] <= 0:
            await update.reply_text("You won the battle!")
            del battles[user_id]
        else:
            # Switch turns
            battle['turn'] = 'opponent'
            await update.reply_text("It's the opponent's turn now.")

    else:
        await update.reply_text("No battle in progress.")

# Add a command to start a battle
@bot.on_message(filters.command(["battle"]))
async def battle_cmd(_: bot, update: Update):
    try:
        _, opponent_id = update.text.split()
        opponent_id = int(opponent_id)
        await start_battle(update, update.from_user.id, opponent_id)
    except ValueError:
        await update.reply_text("Invalid command format. Use `/battle <opponent_id>`.")

# Add a callback query handler for battle inline buttons
bot.add_handler(CallbackQueryHandler(battle_callback, filters.regex("normal_strike|special_attack")))
