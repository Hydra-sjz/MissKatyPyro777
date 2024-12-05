# DONE: Github

from aiohttp import ClientSession
from pyrogram import Client

from misskaty import custom_filter
from misskaty.ultis_ex.wmilia_m.decorators import *


@usage("/github [username]")
@example("/github ArshCypherZ")
@description(
    "This will fetch information of given username from github.com and send it."
)
@Client.on_message(custom_filter.command("github", disable=True))
@exception
async def github(_, message):
    if len(message.text.split()) != 2:
        return await usage_string(message, github)
    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"
    async with ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404: Not Found")
            result = await request.json()

            url = result["html_url"]
            name = result["name"]
            company = result["company"]
            bio = result["bio"]
            created_at = result["created_at"]
            avatar_url = result["avatar_url"]
            blog = result["blog"]
            location = result["location"]
            repositories = result["public_repos"]
            followers = result["followers"]
            following = result["following"]
            caption = f"""**Github Information of {name}:**
**Username :** `{username}`
**Bio :** `{bio}`
**Profile Link :** [Here]({url})
**Company :** `{company}`
**Created On :** `{created_at}`
**Repositories :** `{repositories}`
**Blog :** `{blog}`
**Location :** `{location}`
**Followers :** `{followers}`
**Following :** `{following}`"""

    await message.reply_photo(photo=avatar_url, caption=caption)
