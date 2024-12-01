from telegram import Update
from itertools import groupby
import math
from html import escape 
import random

from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from misskaty import collection, user_collection, application

async def remove_all_characters(update: Update, context: CallbackContext):
    if str(update.effective_user.id) != "784589736":  # Replace "6257270528" with the owner's ID
        await update.message.reply_text('Only the owner can use this command.')
        return

    try:
        # Check if the command format is correct
        args = context.args
        if len(args) != 1:
            await update.message.reply_text('Incorrect format. Please use: /remove user_id')
            return

        user_id = int(args[0])

        # Check if the user exists
        user = await user_collection.find_one({'id': user_id})
        if not user:
            await update.message.reply_text('User not found.')
            return

        # Remove all characters from the user's collection
        await user_collection.update_one({'id': user_id}, {'$set': {'characters': []}})

        await update.message.reply_text(f'All characters have been removed from user with ID {user_id}.')
    except Exception as e:
        await update.message.reply_text(f'An error occurred: {str(e)}')

application.add_handler(CommandHandler("remove", remove_all_characters))
