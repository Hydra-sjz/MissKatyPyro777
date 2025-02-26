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
from misskaty import app
from misskaty.ultis_ex.database.dbfunctions import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
)

chat_watcher_group = 10


@app.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message):
    if message.from_user:
        user_id = message.from_user.id
        await add_served_user(user_id)

    chat_id = message.chat.id
    blacklisted_chats_list = await blacklisted_chats()

    if not chat_id:
        return

    if chat_id in blacklisted_chats_list:
        return await app.leave_chat(chat_id)

    await add_served_chat(chat_id)
