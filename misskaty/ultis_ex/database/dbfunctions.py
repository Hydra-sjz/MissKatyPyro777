"""
MIT License

Copyright (c) 2024 TheHamkerCat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import codecs
import pickle
from string import ascii_lowercase
from typing import Dict, List, Union

from wbb import db

# SOME THINGS ARE FUCKED UP HERE, LIKE TOGGLEABLES HAVE THEIR OWN COLLECTION
# (SHOULD FIX IT WITH SOMETHING LIKE TOGGLEDB), MOST OF THE CODE IS BAD AF
# AND NEEDS TO BE REWRITTEN, BUT I WON'T, AS IT WILL TAKE
# TOO MUCH TIME AND WILL BE BAD FOR ALREADY STORED DATA


blacklist_chatdb = db.blacklistChat

rssdb = db.rss



    
 
async def blacklisted_chats() -> list:
    blacklist_chat = []
    async for chat in blacklist_chatdb.find({"chat_id": {"$lt": 0}}):
        blacklist_chat.append(chat["chat_id"])
    return blacklist_chat


async def blacklist_chat(chat_id: int) -> bool:
    if not await blacklist_chatdb.find_one({"chat_id": chat_id}):
        await blacklist_chatdb.insert_one({"chat_id": chat_id})
        return True
    return False


async def whitelist_chat(chat_id: int) -> bool:
    if await blacklist_chatdb.find_one({"chat_id": chat_id}):
        await blacklist_chatdb.delete_one({"chat_id": chat_id})
        return True
    return False


async def add_rss_feed(chat_id: int, url: str, last_title: str):
    return await rssdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"url": url, "last_title": last_title}},
        upsert=True,
    )

async def remove_rss_feed(chat_id: int):
    return await rssdb.delete_one({"chat_id": chat_id})

async def update_rss_feed(chat_id: int, last_title: str):
    return await rssdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"last_title": last_title}},
        upsert=True,
    )

async def is_rss_active(chat_id: int) -> bool:
    return await rssdb.find_one({"chat_id": chat_id})

async def get_rss_feeds() -> list:
    data = []
    async for feed in rssdb.find({"chat_id": {"$exists": 1}}):
        data.append(
            dict(
                chat_id=feed["chat_id"],
                url=feed["url"],
                last_title=feed["last_title"],
            )
        )
    return data

async def get_rss_feeds_count() -> int:
    return len([i async for i in rssdb.find({"chat_id": {"$exists": 1}})])

