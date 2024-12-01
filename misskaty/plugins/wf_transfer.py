from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler
from misskaty import application, user_collection

# Replace OWNER_ID with the actual owner's user ID
OWNER_ID = 784589736

async def transfer(update, context):
    try:
        # Check if the user is the owner
        user_id = update.effective_user.id
        if user_id != OWNER_ID:
            await update.message.reply_text('You are not authorized to use this command.')
            return

        # Ensure the command has the correct number of arguments
        if len(context.args) != 2:
            await update.message.reply_text('Please provide two valid user IDs for the transfer.')
            return

        sender_id = int(context.args[0])
        receiver_id = int(context.args[1])

        # Retrieve sender's and receiver's information
        sender = await user_collection.find_one({'id': sender_id})
        receiver = await user_collection.find_one({'id': receiver_id})

        # Check if both sender and receiver exist
        if not sender:
            await update.message.reply_text(f'Sender with ID {sender_id} not found.')
            return

        if not receiver:
            await update.message.reply_text(f'Receiver with ID {receiver_id} not found.')
            return

        # Store the IDs temporarily in the user_data for later use
        context.user_data['transfer'] = {'sender_id': sender_id, 'receiver_id': receiver_id}

        # Create inline keyboard buttons for confirmation
        keyboard = [
            [InlineKeyboardButton("✅ Yes, Transfer", callback_data='confirm_transfer')],
            [InlineKeyboardButton("❌ No, Cancel", callback_data='cancel_transfer')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Ask for confirmation
        await update.message.reply_text(
            f"Are you sure you want to transfer all waifus from User {sender_id} to User {receiver_id}?",
            reply_markup=reply_markup
        )

    except ValueError:
        await update.message.reply_text('Invalid User IDs provided.')

async def transfer_confirm(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'confirm_transfer':
        # Retrieve sender and receiver IDs from user_data
        transfer_data = context.user_data.get('transfer')
        if transfer_data:
            sender_id = transfer_data['sender_id']
            receiver_id = transfer_data['receiver_id']

            # Perform the transfer
            sender = await user_collection.find_one({'id': sender_id})
            receiver = await user_collection.find_one({'id': receiver_id})

            receiver_waifus = receiver.get('characters', [])
            receiver_waifus.extend(sender.get('characters', []))

            await user_collection.update_one({'id': receiver_id}, {'$set': {'characters': receiver_waifus}})
            await user_collection.update_one({'id': sender_id}, {'$set': {'characters': []}})

            await query.edit_message_text('All waifus have been successfully transferred!')
        else:
            await query.edit_message_text('Error: Transfer data not found.')

    elif query.data == 'cancel_transfer':
        # Cancel the transfer
        await query.edit_message_text('Transfer has been canceled.')

# ... (your other code for transfer and handle_transfer_confirmation) 

# Register the handlers 
application.add_handler(CommandHandler("transfer", transfer))
application.add_handler(CallbackQueryHandler(transfer_confirm, pattern='^confirm_transfer|^cancel_transfer$')) # Register with correct function name
