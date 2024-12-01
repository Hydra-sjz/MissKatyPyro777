from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from misskaty import app
from misskaty import sudo_users_collection, application

DEV_LIST = [6584789596]
authorized_users = [6584789596]



async def get_user_username(user_id):
    user = await app.get_chat(user_id)
    return user.username

async def add_to_sudo_users(user_id, username, sudo_title):
    await sudo_users_collection.update_one(
        {'id': user_id},
        {'$set': {'username': username, 'sudo_title': sudo_title}},
        upsert=True
    )

async def remove_from_sudo_users(user_id):
    await sudo_users_collection.delete_one({"id": user_id})

async def is_user_sudo(user_id):
    user = await sudo_users_collection.find_one({"id": user_id})
    return bool(user)

async def fetch_sudo_users():
    sudo_users = []
    async for user in sudo_users_collection.find({}):
        user_id = user.get('id')
        username = user.get('username')
        sudo_title = user.get('sudo_title')
        if user_id and username:
            sudo_users.append({"user_id": user_id, "username": username, "sudo_title": sudo_title})
    return sudo_users


async def is_user_sudo(user_id: int) -> bool:
    user = await sudo_users_collection.find_one({"id": user_id})
    return bool(user)

async def add_sudo_command(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    
    # Check if the user is authorized
    if user_id not in authorized_users:
        await update.message.reply_text("You are not authorized to use this command.")
        return

    if update.message.reply_to_message:
        replied_user_id = update.message.reply_to_message.from_user.id
        username = await get_user_username(replied_user_id)
        sudo_title = ' '.join(context.args) if context.args else "Sudo User"
        await add_to_sudo_users(replied_user_id, username, sudo_title)
        await update.message.reply_text(f"User {username} has been added as sudo with title '{sudo_title}'.")
    else:
        await update.message.reply_text("Please reply to a message to add a user as sudo.")

async def remove_sudo_command(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id

    # Check if the user is authorized
    if user_id not in authorized_users:
        await update.message.reply_text("You are not authorized to use this command.")
        return

    if update.message.reply_to_message:
        replied_user_id = update.message.reply_to_message.from_user.id
        user = await sudo_users_collection.find_one({"id": replied_user_id})
        if user:
            await remove_from_sudo_users(replied_user_id)
            username = user.get('username')
            await update.message.reply_text(f"User {username} has been removed from sudo users.")
        else:
            await update.message.reply_text("User not found in sudo users.")
    else:
        await update.message.reply_text("Please reply to a message to remove a user from sudo.")

async def sudo_list_command(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    
    # Check if the user is a sudo user
    if not await is_user_sudo(user_id):
        await update.message.reply_text("You are not authorized to view the sudo list.")
        return

    sudo_users = await fetch_sudo_users()
    if not sudo_users:
        await update.message.reply_text("No sudo users found.")
        return

    message = "Sudo Users:\n"
    for user in sudo_users:
        message += f"User ID: {user['user_id']}, Username: @{user['username']}, Title: {user['sudo_title']}\n"
    
    await update.message.reply_text(message)

# Add command handlers
application.add_handler(CommandHandler("addsudo", add_sudo_command))
application.add_handler(CommandHandler("sudoremove", remove_sudo_command))
application.add_handler(CommandHandler("sudolist", sudo_list_command))
