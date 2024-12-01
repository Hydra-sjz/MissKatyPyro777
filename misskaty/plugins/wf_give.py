from pyrogram import Client, filters
from misskaty import dbw as db, collection, top_global_groups_collection, group_user_totals_collection, user_collection, user_totals_collection
import asyncio
from misskaty import app
from misskaty.vars import SUDO as sudo_users

DEV_LIST = [784589736]

async def give_character(receiver_id, character_id):
    character = await collection.find_one({'id': character_id})

    if character:
        try:
            await user_collection.update_one(
                {'id': receiver_id},
                {'$push': {'characters': character}}
            )

            img_url = character['img_url']
            caption = (
                f"Successfully Given To {receiver_id}\n"
                f"Information As Follows\n"
                f" 🎏 𝙍𝙖𝙧𝙞𝙩𝙮: {character['rarity']}\n"
                f"🎐 𝘼𝙣𝙞𝙢𝙚: {character['anime']}\n"
                f"💕 𝙉𝙖𝙢𝙚: {character['name']}\n"
                f"🪅 𝙄𝘿: {character['id']}"
            )

            return img_url, caption
        except Exception as e:
            print(f"Error updating user: {e}")
            raise
    else:
        raise ValueError("Character not found.")

@app.on_message(filters.command(["give"]) & filters.reply & filters.user(DEV_LIST))
async def give_character_command(_, message):
    # Check if a message is replied to
    if not message.reply_to_message:
        await message.reply_text("You need to reply to a user's message to give a character!")
        return

    try:
        # Split the message to get the character ID
        character_id = str(message.text.split()[1])
        receiver_id = message.reply_to_message.from_user.id

        # Call the function to give the character
        result = await give_character(receiver_id, character_id)

        if result:
            # If successful, send the photo and caption
            img_url, caption = result
            await message.reply_photo(photo=img_url, caption=caption)

    # Catch specific exceptions and provide appropriate messages
    except IndexError:
        await message.reply_text("Please provide a character ID.")
    except ValueError as e:
        await message.reply_text(str(e))  # Specific error message from the function
    except Exception as e:
        print(f"Error in give_character_command: {e}")
        await message.reply_text("An error occurred while processing the command.")



async def add_all_characters_for_user(user_id):
    user = await user_collection.find_one({'id': user_id})

    if user:
        all_characters_cursor = collection.find({})
        all_characters = await all_characters_cursor.to_list(length=None)

        existing_character_ids = {character['id'] for character in user['characters']}
        new_characters = [character for character in all_characters if character['id'] not in existing_character_ids]

        if new_characters:
            await user_collection.update_one(
                {'id': user_id},
                {'$push': {'characters': {'$each': new_characters}}}
            )

            return f"Successfully added characters for user {user_id}"
        else:
            return f"No new characters to add for user {user_id}"
    else:
        return f"User with ID {user_id} not found."

@app.on_message(filters.command(["addc"]) & filters.user(DEV_LIST))
async def add_characters_command(client, message):
    user_id_to_add_characters_for = message.from_user.id
    result_message = await add_all_characters_for_user(user_id_to_add_characters_for)
    await message.reply_text(result_message)


async def kill_character(receiver_id, character_id):
    character = await collection.find_one({'id': character_id})

    if character:
        try:
            await user_collection.update_one(
                {'id': receiver_id},
                {'$pull': {'characters': {'id': character_id}}}
            )

            return f"Successfully removed character `{character_id}` from user `{receiver_id}`"
        except Exception as e:
            print(f"Error updating user: {e}")
            raise
    else:
        raise ValueError("Character not found.")

@app.on_message(filters.command(["kill"]) & filters.reply & filters.user(DEV_LIST))
async def remove_character_command(client, message):
    try:
        character_id = str(message.text.split()[1])
        receiver_id = message.reply_to_message.from_user.id

        result_message = await kill_character(receiver_id, character_id)

        await message.reply_text(result_message)
    except (IndexError, ValueError) as e:
        await message.reply_text(str(e))
    except Exception as e:
        print(f"Error in remove_character_command: {e}")
        await message.reply_text("An error occurred while processing the command.")
