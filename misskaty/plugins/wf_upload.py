#FLEXdub_Official
import urllib.request
from pymongo import ReturnDocument

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from misskaty import application, collection, dbw as db 
from misskaty.vars import SUDO as sudo_users, LOG_CHANNEL as CHARA_CHANNEL_ID

SUPPORT_CHAT = "xbots_x"
WRONG_FORMAT_TEXT = """Wrong ❌️ format...  eg. /upload Img_url muzan-kibutsuji Demon-slayer 3 1

img_url character-name anime-name rarity-number event-number

Use rarity number accordingly:
rarity_map = 1 (🟢 Common), 2 (🟣 Rare), 3 (🟡 Legendary), 4 (💮 Special Edition), 5 (🔮 Premium Edition), 6 (🎗️ Supreme)

Use event number accordingly:
event_map = 1 (🏖 Summer), 2 (👘 Kimono), 3 (☃️ Winter), 4 (💞 Valentine), 5 (🎒 School), 6 (🎃 Halloween), 7 (🎮 Game), 8 (🎩 Tuxedo), 9 (👥 Duo), 10 (🧹 Made), 11 (☔ Monsoon), 12 (🐰 Bunny),  13 (🤝🏻 Group), 14 (🥻 Saree), 15 (🎄 Cristmas), 16 (💐 Groom), 17 (🩺 Nurse), 18 (💍 Wedding), 19 (🎊 Cheerleaders), 20 (⚽ Soccer), 21 (🏀 Basketball), 22 (🥂 Party), 22 (👑 Lord), 23 (None)"""

EVENT_MAPPING = {
    1: {"name": "𝒔𝒖𝒎𝒎𝒆𝒓", "sign": "🏖"},
    2: {"name": "𝑲𝒊𝒎𝒐𝒏𝒐", "sign": "👘"},
    3: {"name": "𝑾𝒊𝒏𝒕𝒆𝒓", "sign": "☃️"},
    4: {"name": "𝑽𝒂𝒍𝒆𝒏𝒕𝒊𝒏𝒆", "sign": "💞"},
    5: {"name": "𝑺𝒄𝒉𝒐𝒐𝒍", "sign": "🎒"},
    6: {"name": "𝑯𝒂𝒍𝒍𝒐𝒘𝒆𝒆𝒏", "sign": "🎃"},
    7: {"name": "𝑮𝒂𝒎𝒆", "sign": "🎮"},
    8: {"name": "𝑻𝒖𝒙𝒆𝒅𝒐", "sign": "🎩"},
    9: {"name": "𝐃𝐮𝐨", "sign": "👥"},
    10: {"name": "𝑴𝒂𝒅𝒆", "sign": "🧹"},
    11: {"name": "𝑴𝒐𝒏𝒔𝒐𝒐𝒏𝑛", "sign": "☔"},
    12: {"name": "𝑩𝒖𝒏𝒏𝒚", "sign": "🐰"},
    13: {"name": "𝐆𝐫𝐨𝐮𝐩", "sign": "🤝🏻"},
    14: {"name": "𝑺𝒂𝒓𝒆𝒆", "sign": "🥻"},
    15: {"name": "𝑪𝒓𝒊𝒔𝒕𝒎𝒂𝒔", "sign": "🎄"},
    16: {"name": "𝑮𝒓𝒐𝒐𝒎", "sign": "💐"},
    17: {"name": "𝑵𝒖𝒓𝒔𝒆", "sign": "🩺"},
    18: {"name": "𝑾𝒆𝒅𝒅𝒊𝒏𝒈", "sign": "💍"},
    19: {"name": "𝑪𝒉𝒆𝒆𝒓𝒍𝒆𝒂𝒅𝒆𝒓𝒔", "sign": "🎊"},
    20: {"name": "𝑺𝒐𝒄𝒄𝒆𝒓", "sign": "⚽"},
    21: {"name": "𝑩𝒂𝒔𝒌𝒆𝒕𝒃𝒂𝒍𝒍", "sign": "🏀"},
    22: {"name": "𝑷𝒂𝒓𝒕𝒚", "sign": "🥂"},
    23: {"name": "𝑳𝒐𝒓𝒅", "sign": "👑"},
    24: None  # Skip event
}


async def get_next_sequence_number(sequence_name):
    sequence_collection = db.sequences
    sequence_document = await sequence_collection.find_one_and_update(
        {'_id': sequence_name}, 
        {'$inc': {'sequence_value': 1}}, 
        return_document=ReturnDocument.AFTER
    )
    if not sequence_document:
        await sequence_collection.insert_one({'_id': sequence_name, 'sequence_value': 0})
        return 0
    return sequence_document['sequence_value']

async def upload(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id) not in sudo_users:
        await update.message.reply_text('Ask My Owner...')
        return

    try:
        args = context.args
        if len(args) != 5:
            await update.message.reply_text(WRONG_FORMAT_TEXT)
            return

        character_name = args[1].replace('-', ' ').title()
        anime = args[2].replace('-', ' ').title()

        try:
            urllib.request.urlopen(args[0])
        except:
            await update.message.reply_text('Invalid URL.')
            return

        rarity_map = {1: "🟢 Common", 2: "🟣 Rare", 3: "🟡 Legendary", 4: "💮 Special Edition", 5: "🔮 Premium Edition", 6: "🎗️ Supreme"}
        try:
            rarity = rarity_map[int(args[3])]
        except KeyError:
            await update.message.reply_text('Invalid rarity. Please use 1, 2, 3, 4, 5, or 6. and if you entered the event mapping wrong then use 13 for skip and you can also see wrong format help text to see event mapping.')
            return

        event_choice = int(args[4])
        event = EVENT_MAPPING.get(event_choice)

        id = str(await get_next_sequence_number('character_id')).zfill(2)

        character = {
            'img_url': args[0],
            'id': id,
            'name': character_name,
            'anime': anime,
            'rarity': rarity,
            'event': event  # Add the event to the character data
        }

        try:
            message = await context.bot.send_photo(
                chat_id=CHARA_CHANNEL_ID,
                photo=args[0],
                caption=f'<b>{id}:</b> {character_name}\n<b>{anime}</b>\n(<b>{rarity[0]} 𝙍𝘼𝙍𝙄𝙏𝙔: </b>{rarity[2:]})' +
                        (f'\n\n{event["sign"]} {event["name"]} {event["sign"]}' if event else '') + 
                        f'\n\n𝑨𝒅𝒅𝒆𝒅 𝑩𝒚 ➥ <a href="tg://user?id={update.effective_user.id}">{update.effective_user.first_name}</a>',
                parse_mode='HTML'
            )
            character['message_id'] = message.message_id
            await collection.insert_one(character)
            await update.message.reply_text('CHARACTER ADDED....')
        except:
            await collection.insert_one(character)
            update.effective_message.reply_text("Character Added but no Database Channel Found, Consider adding one.")

    except Exception as e:
        await update.message.reply_text(f'Character Upload Unsuccessful. Error: {str(e)}\nIf you think this is a source error, forward to: {SUPPORT_CHAT}')


async def delete(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id) not in sudo_users:
        await update.message.reply_text('Ask my Owner to use this Command...')
        return

    try:
        args = context.args
        if len(args) != 1:
            await update.message.reply_text('Incorrect format... Please use: /delete ID')
            return


        character = await collection.find_one_and_delete({'id': args[0]})

        if character:

            await context.bot.delete_message(chat_id=CHARA_CHANNEL_ID, message_id=character['message_id'])
            await update.message.reply_text('DONE')
        else:
            await update.message.reply_text('Deleted Successfully from db, but character not found In Channel')
    except Exception as e:
        await update.message.reply_text(f'{str(e)}')

async def update(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id) not in sudo_users:
        await update.message.reply_text('You do not have permission to use this command.')
        return

    try:
        args = context.args
        if len(args) != 3:
            await update.message.reply_text('Incorrect format. Please use: /update id field new_value')
            return

        # Get character by ID
        character = await collection.find_one({'id': args[0]})
        if not character:
            await update.message.reply_text('Character not found.')
            return

        # Check if field is valid
        valid_fields = ['img_url', 'name', 'anime', 'rarity', 'event', 'id']
        if args[1] not in valid_fields:
            await update.message.reply_text(f'Invalid field. Please use one of the following: {", ".join(valid_fields)}')
            return

        # Update field
        if args[1] in ['name', 'anime']:
            new_value = args[2].replace('-', ' ').title()
        elif args[1] == 'rarity':
            rarity_map = {1: "🟢 Common", 2: "🟣 Rare", 3: "🟡 Legendary", 4: "💮 Special Edition", 5: "🔮 Premium Edition", 6: "🎗️ Supreme"}
            try:
                new_value = rarity_map[int(args[2])]
            except KeyError:
                await update.message.reply_text('Invalid rarity. Please use 1, 2, 3, 4, 5, or 6.')
                return
        elif args[1] == 'event':
            event_map = {
                1: {"name": "𝒔𝒖𝒎𝒎𝒆𝒓", "sign": "🏖"},
                2: {"name": "𝑲𝒊𝒎𝒐𝒏𝒐", "sign": "👘"},
                3: {"name": "𝑾𝒊𝒏𝒕𝒆𝒓", "sign": "☃️"},
                4: {"name": "𝑽𝒂𝒍𝒆𝒏𝒕𝒊𝒏𝒆", "sign": "💞"},
                5: {"name": "𝑺𝒄𝒉𝒐𝒐𝒍", "sign": "🎒"},
                6: {"name": "𝑯𝒂𝒍𝒍𝒐𝒘𝒆𝒆𝒏", "sign": "🎃"},
                7: {"name": "", "sign": "🎮"},
                8: {"name": "𝑻𝒖𝒙𝒆𝒅𝒐", "sign": "🎩"},
                9: {"name": "𝐃𝐮𝐨", "sign": "👥"},
                10: {"name": "𝑴𝒂𝒅𝒆", "sign": "🧹"},
                11: {"name": "𝑴𝒐𝒏𝒔𝒐𝒐𝒏", "sign": "☔"},
                12: {"name": "𝑩𝒖𝒏𝒏𝒚", "sign": "🐰"},
                13: {"name": "𝐆𝐫𝐨𝐮𝐩", "sign": "🤝🏻"},
                14: {"name": "𝑺𝒂𝒓𝒆𝒆", "sign": "🥻"},
                15: {"name": "𝑪𝒓𝒊𝒔𝒕𝒎𝒂𝒔", "sign": "🎄"},
                16: {"name": "𝑮𝒓𝒐𝒐𝒎", "sign": "💐"},
                17: {"name": "𝑵𝒖𝒓𝒔𝒆", "sign": "🩺"},
                18: {"name": "𝑾𝒆𝒅𝒅𝒊𝒏𝒈", "sign": "💍"},
                19: {"name": "𝑪𝒉𝒆𝒆𝒓𝒍𝒆𝒂𝒅𝒆𝒓𝒔", "sign": "🎊"},
                20: {"name": "𝑺𝒐𝒄𝒄𝒆𝒓", "sign": "⚽"},
                21: {"name": "𝑩𝒂𝒔𝒌𝒆𝒕𝒃𝒂𝒍𝒍", "sign": "🏀"},
                22: {"name": "𝑷𝒂𝒓𝒕𝒚", "sign": "🥂"},
                23: {"name": "𝑳𝒐𝒓𝒅", "sign": "👑"},
                24: {"name": None, "sign": None}
            }
            try:
                new_value = event_map[int(args[2])]
            except KeyError:
                await update.message.reply_text('Invalid event. Please use a number between 1 and 13.')
                return
        else:
            new_value = args[2]

        await collection.find_one_and_update({'id': args[0]}, {'$set': {args[1]: new_value}})

        # Update the caption or image in the Telegram channel if necessary
        if args[1] == 'img_url':
            await context.bot.delete_message(chat_id=CHARA_CHANNEL_ID, message_id=character['message_id'])
            message = await context.bot.send_photo(
                chat_id=CHARA_CHANNEL_ID,
                photo=new_value,
                caption=f'<b>{character["id"]}:</b> {character["name"]}\n<b>{character["anime"]}</b>\n(<b>{character["rarity"][0]} 𝙍𝘼𝙍𝙄𝙏𝙔:</b> {character["rarity"][2:]})\n{character["event"]["sign"]}{character["event"]["name"]}{character["event"]["sign"] if character.get("event") else ""}\n\n𝑼𝒑𝒅𝒂𝒕𝒆𝒅 𝑩𝒚 ➥ <a href="tg://user?id={update.effective_user.id}">{update.effective_user.first_name}</a>',
                parse_mode='HTML'
            )
            character['message_id'] = message.message_id
            await collection.find_one_and_update({'id': args[0]}, {'$set': {'message_id': message.message_id}})
        else:
            caption = f'<b>{character["id"]}:</b> {character["name"]}\n<b>{character["anime"]}</b>\n(<b>{character["rarity"][0]} 𝙍𝘼𝙍𝙄𝙏𝙔:</b> {character["rarity"][2:]})\n'
            if character.get("event"):
                caption += f'{character["event"]["sign"]}{character["event"]["name"]}{character["event"]["sign"]}\n'
            caption += f'\n𝑼𝒑𝒅𝒂𝒕𝒆𝒅 𝑩𝒚 ➥ <a href="tg://user?id={update.effective_user.id}">{update.effective_user.first_name}</a>'

            await context.bot.edit_message_caption(
                chat_id=CHARA_CHANNEL_ID,
                message_id=character['message_id'],
                caption=caption,
                parse_mode='HTML'
            )

        await update.message.reply_text('Update done in database. It may take some time for the changes to reflect in your channel.')
    except Exception as e:
        await update.message.reply_text(f'Error occurred: {str(e)}')


UPLOAD_HANDLER = CommandHandler('upload', upload, block=False)
application.add_handler(UPLOAD_HANDLER)
DELETE_HANDLER = CommandHandler('delete', delete, block=False)
application.add_handler(DELETE_HANDLER)
UPDATE_HANDLER = CommandHandler('update', update, block=False)
application.add_handler(UPDATE_HANDLER)
