import datetime as ds
import time

from telethon import Button, events

import misskaty.strings as strings
from misskaty import LOGGER, db, tle as telethn
from misskaty.custom_filter import callbackquery, register
from misskaty.ultis_ex.wmilia_m.admins import get_time, is_admin
from misskaty.ultis_ex.wmilia_m.decorators import *

users_collection = db.chatlevels
first_name = db.first_name
level = db.onofflevel

ranks = [
    {"name": "Elf", "min_points": 0},
    {"name": "Oni", "min_points": 500},
    {"name": "Giant", "min_points": 1000},
    {"name": "Evil Eye", "min_points": 10000},
    {"name": "Werewolf", "min_points": 50000},
    {"name": "DragonKin", "min_points": 100000},
]

levels = 1000


async def get_rank(points):
    for rank in ranks[::-1]:
        if points >= rank["min_points"]:
            return rank["name"]
    return "Gay"


async def read_last_collection_time_today(user_id, chat_id):
    try:
        user = await users_collection.find_one({"user_id": user_id, "chat_id": chat_id})
        collection_time = user.get("last_date")
    except Exception as e:
        LOGGER.error(f"Error reading last collection time: {e}")
        collection_time = None

    return ds.datetime.fromtimestamp(collection_time) if collection_time else None


async def can_collect_coins(user_id, chat_id):
    last_collection_time = await read_last_collection_time_today(user_id, chat_id)
    if last_collection_time is None:
        return (True, True)
    current_time = ds.datetime.now()
    time_since_last_collection = current_time - last_collection_time
    return (
        time_since_last_collection.total_seconds() >= 24 * 60 * 60,
        24 * 60 * 60 - time_since_last_collection.total_seconds(),
    )


async def increase_points(user_id, chat_id, points):
    present = await first_name.find_one({"user_id": user_id})
    if not present:
        await first_name.insert_one({"user_id": user_id})

    user_data = await users_collection.find_one(
        {"user_id": user_id, "chat_id": chat_id}
    )
    update_data = {"$inc": {"points": points}}

    if user_data:
        await users_collection.update_one({"_id": user_data["_id"]}, update_data)
    else:
        await users_collection.insert_one(
            {"user_id": user_id, "chat_id": chat_id, "points": points}
        )


async def get_leaderboard(chat_id):
    meow = users_collection.find({"chat_id": chat_id})
    gae = await meow.to_list(None)
    return sorted(gae, key=lambda x: x["points"], reverse=True)[:10]


async def get_user_stats(user_id, chat_id):
    user_data = await users_collection.find_one(
        {"user_id": user_id, "chat_id": chat_id}
    )
    fuser = await first_name.find_one({"user_id": user_id})
    if fuser and user_data:
        points = user_data["points"]
        first_name1 = fuser["first_name"]
        level = min(points // 10, levels)
        rank = await get_rank(points)

        return {
            "points": points,
            "first_name": first_name1,
            "level": level,
            "rank": rank,
        }
    else:
        return None


async def is_flooding(user_id, chat_id):
    user_data = await users_collection.find_one(
        {"user_id": user_id, "chat_id": chat_id}
    )
    if user_data and "last_message_time" in user_data:
        current_time = time.time()
        last_message_time = user_data["last_message_time"]
        time_difference = current_time - last_message_time
        if time_difference < 5:
            return True
    return False


@register(pattern="leaderboard")
async def _leaderboard(event):
    if not event.is_group:
        return await event.reply("Leaderboard is only for group chats.")
    if not await level.find_one({"chat_id": event.chat_id}):
        return await event.reply(
            "Levelling system is not active in this chat. To turn it on use `/level on`"
        )
    chat_id = event.chat_id
    leaderboard = await get_leaderboard(chat_id)
    lmao = ""

    if leaderboard:
        lmao += "🏆 **Leaderboard** for this chat:\n\n"
        for idx, user in enumerate(leaderboard, start=1):
            points = user["points"]
            user_id = user["user_id"]
            gay = await first_name.find_one({"user_id": user_id})

            if gay:
                if "first_name" in gay:
                    first_name1 = gay["first_name"]
                else:
                    first_name1 = "Unknown"
            else:
                first_name1 = "Unknown"

            lmao += (
                f"{idx}. [{first_name1}](tg://user?id={user_id}) --> {points} points\n"
            )
        lmao += "\nUse /register to setup your names."
    else:
        lmao += (
            "No data for this chat. Try /register to register yourself in bot first!"
        )
    await event.reply(
        lmao, buttons=Button.inline("Global Leaderboard", data="gleaderboard_")
    )


@callbackquery(pattern="gleaderboard_")
async def gleaderboard(event):
    cursor = users_collection.find().sort("points", -1).limit(10)
    sorted_players = await cursor.to_list(length=None)

    # Fetch the first_name for each user from the first_name collection
    for player in sorted_players:
        if "user_id" not in player:
            continue

        user_id = player["user_id"]
        first_name_doc = await first_name.find_one({"user_id": user_id})
        if first_name_doc:
            player["first_name"] = first_name_doc.get("first_name", "Unknown")
        else:
            player["first_name"] = "Unknown"

    gae = "🏆 **Global Leaderboard** 🏆\n\n"
    for rank, player in enumerate(sorted_players, start=1):
        name = player.get("first_name", "Unknown")
        points = player.get("points", 0)
        gae += f"{rank}. [{name}](tg://user?id={player.get('user_id', 'N/A')}) --> {points} points\n"

    await event.edit(gae)


@register(pattern="daily")
async def _daily(event):
    if not event.is_group:
        return await event.reply(
            "You can only claim your daily bonus of 100 points inside a group chat!"
        )
    if not await level.find_one({"chat_id": event.chat_id}):
        return await event.reply(
            "Levelling system is not active in this chat. To turn it on use `/level on`"
        )
    try:
        stats = await get_user_stats(event.sender_id, event.chat_id)
    except KeyError:
        stats = None
    if not stats:
        return await event.reply("Use /register to register yourself in bot first!")
    points = stats["points"]
    x, y = await can_collect_coins(event.sender_id, event.chat_id)
    if x is True:
        await users_collection.update_one(
            {"user_id": event.sender_id, "chat_id": event.chat_id},
            {"$set": {"points": points + 100}},
            upsert=True,
        )
        await users_collection.update_one(
            {"user_id": event.sender_id, "chat_id": event.chat_id},
            {"$set": {"last_date": ds.datetime.now().timestamp()}},
            upsert=True,
        )
        new_points = points + 100
        return await event.reply(
            f"Successfully claimed daily 100 points!\n**Current points**: {new_points}"
        )
    await event.reply(
        "You can claim your daily 100 points in around`{0}`".format((await get_time(y)))
    )


async def write_last_collection_time_weekly(user_id, chat_id, time):
    await users_collection.update_one(
        {"user_id": user_id, "chat_id": chat_id},
        {"$set": {"last_collection_weekly": time}},
        upsert=True,
    )


async def read_last_collection_time_weekly(user_id, chat_id):
    user = await users_collection.find_one({"user_id": user_id, "chat_id": chat_id})
    try:
        collection_time = user["last_collection_weekly"]
    except BaseException:
        collection_time = None
    if collection_time:
        return ds.datetime.fromtimestamp(collection_time)
    else:
        return None


async def can_collect(user_id, chat_id):
    last_collection_time = await read_last_collection_time_weekly(user_id, chat_id)
    if last_collection_time is None:
        return (True, True)
    current_time = ds.datetime.now()
    time_since_last_collection = current_time - last_collection_time
    return (
        time_since_last_collection.total_seconds() >= 7 * 24 * 60 * 60,
        7 * 24 * 60 * 60 - time_since_last_collection.total_seconds(),
    )


@register(pattern="weekly")
async def _daily(event):
    if not event.is_group:
        return await event.reply(
            "You can only claim your daily bonus of 500 points inside a group chat!"
        )
    if not await level.find_one({"chat_id": event.chat_id}):
        return await event.reply(
            "Levelling system is not active in this chat. To turn it on use `/level on`"
        )
    try:
        stats = await get_user_stats(event.sender_id, event.chat_id)
    except KeyError:
        stats = None
    if not stats:
        return await event.reply("Use /register to register yourself in bot first!")
    points = stats["points"]
    x, y = await can_collect(event.sender_id, event.chat_id)
    if x is True:
        await users_collection.update_one(
            {"user_id": event.sender_id, "chat_id": event.chat_id},
            {"$set": {"points": points + 500}},
            upsert=True,
        )
        await write_last_collection_time_weekly(
            event.sender_id, event.chat_id, ds.datetime.now().timestamp()
        )
        new_points = points + 500
        return await event.reply(
            f"Successfully claimed weekly 500 points!\n**Current points**: {new_points}"
        )
    await event.reply(
        "You can claim your weekly 500 points in around`{0}`".format(
            (await get_time(y))
        )
    )


@register(pattern="rank")
async def userstats(event):
    if not event.is_group:
        return await event.reply(
            "You can only see your rank inside a specific group chat."
        )
    if not await level.find_one({"chat_id": event.chat_id}):
        return await event.reply(
            "Levelling system is not active in this chat. To turn it on use `/level on`"
        )
    user_id = event.sender_id
    chat_id = event.chat_id

    try:
        stats = await get_user_stats(user_id, chat_id)
    except KeyError:
        stats = None
    "https://api.akuari.my.id/canvas/rank?avatar=https://camo.githubusercontent.com/1ad4c22d443bd0a2f7fed1eebd75f8bd2f4c7616c8e8dc31f4797135896d525b/68747470733a2f2f692e6962622e636f2f31526d524c39642f494d472d32303231313130342d3130353230392d3438382e6a7067&username=Ari&needxp=939505&bg=https://telegra.ph/file/c8b84fff99a1914b4207d.png&level=284&currxp=23284&rank=https://i.ibb.co/Wn9cvnv/FABLED.png"
    if stats:
        response = f"**{stats['first_name']}'s Stats**:\n\n**Points Gained**: {stats['points']}\n**Level**: {stats['level']}\n**Rank**: {stats['rank']}"

    else:
        response = "Use /register to register your name first."

    await event.reply(response)


@register(pattern="register")
async def register_(event):
    if not event.is_group:
        return await event.reply(
            "Please register inside a group, each group will have it's seperate rankings."
        )
    if not await level.find_one({"chat_id": event.chat_id}):
        return await event.reply(
            "Levelling system is not active in this chat. To turn it on use `/level on`"
        )

    try:
        args: str = event.text.split(None, 1)[1]
    except IndexError:
        return await event.reply(
            "Use it like: /register PussySlayer69\n**Note**: You cannot change your name once it is registered."
        )

    if len(args) > 20:
        return await event.reply("Name too long, please try a shorter one")

    present = await first_name.find_one({"user_id": event.sender_id})
    if present and "first_name" in present:
        return await event.reply(
            "You are already registered. Please use /rank to see your user stats."
        )

    meow = await first_name.find_one({"first_name": args})
    if meow:
        return await event.reply(
            f"{args} has already been used by someone else. Please try some other name!"
        )

    await first_name.update_one(
        {"user_id": event.sender_id}, {"$set": {"first_name": args}}
    )
    return await event.reply(
        f"Successfully registered as {args}!\nUse /rank to see your stats."
    )


@register(pattern="rankings")
@exception
async def userstats(event):
    if not event.is_private:
        return await event.reply("Please use this command in my private chat.")
    response = """
The ranking system consists of multiple ranks, each with a name and a minimum number of points required to unlock that rank.

Here is a breakdown of each rank and its corresponding minimum points:

1. Rank: Elf
   - Minimum Points: 0
   - Description: The starting rank of the game. All players begin at this level.

2. Rank: Oni
   - Minimum Points: 500
   - Description: Players need to accumulate at least 500 points to unlock this rank. It represents a slightly higher level of achievement compared to the starting rank.

3. Rank: Giant
   - Minimum Points: 1000
   - Description: Players must reach a minimum of 1000 points to unlock this rank. It signifies progress and advancement in the game.

4. Rank: Evil Eye
   - Minimum Points: 10000
   - Description: Once players accumulate a minimum of 10000 points, they unlock this rank. It represents a significant achievement in the game and indicates a higher level of skill or dedication.

5. Rank: Werewolf
   - Minimum Points: 50000
   - Description: Upon reaching a minimum of 50000 points, players unlock the Werewolf rank. This rank signifies substantial progress and demonstrates a notable level of mastery in the game.

6. Rank: DragonKin
   - Minimum Points: 100000
   - Description: The highest rank in the game. Players need to accumulate a minimum of 100000 points to unlock this rank. It symbolizes exceptional skill and represents an elite level within the game.

Players start as Elves and can progress through the ranks by earning points. As they accumulate the required points, they unlock higher ranks, indicating their progression and growth within the game.

As the chat level game will get popular, we will add more levels and exciting features to it. Please contribute suggestions at @SpiralTechDivision
"""
    await event.reply(response)


@telethn.on(events.NewMessage)
async def handle_message(event):
    if not event.is_group:
        return
    if not event.text:
        return
    user_id = event.sender_id
    chat_id = event.chat_id

    if user_id == 5737513498:
        return

    if event.from_id:
        if not await level.find_one({"chat_id": event.chat_id}):
            return
        if not (await is_flooding(user_id, chat_id)):
            await increase_points(user_id, chat_id, 1)
            await users_collection.update_one(
                {"user_id": user_id, "chat_id": chat_id},
                {"$set": {"last_message_time": time.time()}},
                upsert=True,
            )
            user_data = await users_collection.find_one(
                {"user_id": user_id, "chat_id": chat_id}
            )
            for rank in ranks[::-1]:
                if user_data["points"] == rank["min_points"]:
                    name = rank["name"]
                    await event.reply(
                        f"Congratulations on reaching new rank {name}\nCheck /rank to know your stats."
                    )
        else:
            pass


ON_ARG = ["on", "yes", "true", 1, "enable"]
OFF_ARG = ["off", "no", "false", 0, "disable"]


@usage("/level [on/off]")
@example("/level on")
@description(
    "Enables levelling system inside a chat. It counts user's message and calculates level of each individual upon that basis."
)
@register(pattern="level")
@logging
@exception
async def levelonoff(event):
    if not event.is_group:
        await event.reply(strings.is_pvt)
    if not await is_admin(event, event.sender_id):
        return

    check = event.text.split()
    try:
        if check[1] in ON_ARG:
            if await level.find_one({"chat_id": event.chat_id}):
                return await event.reply(
                    "Level System is already enabled in this chat."
                )
            await level.insert_one({"chat_id": event.chat_id})
            await event.reply("Level System Enabled.")
            return "LEVEL_ON", None, None
        elif check[1] in OFF_ARG:
            if not await level.find_one({"chat_id": event.chat_id}):
                return await event.reply(
                    "Level System is already disabled in this chat."
                )
            await level.delete_one({"chat_id": event.chat_id})
            await event.reply("Level System Disabled.")
            return "LEVEL_OFF", None, None
        else:
            await event.reply("Invalid Argument.")
            return
    except IndexError:
        if await level.find_one({"chat_id": event.chat_id}):
            await event.reply("Level System in enabled in this chat.")
        else:
            await event.reply("Level System in disabled in this chat.")
