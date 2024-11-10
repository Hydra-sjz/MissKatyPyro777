import datetime

from misskaty import db

users = db.users
chats = db.chats

first_found_date = datetime.datetime.now()


async def add_user(
    user_id, username=None, chat_id=None, chat_title=None, Forwared=False
):
    UserData = await users.find_one({"user_id": user_id})

    if UserData is None:
        if Forwared:
            UsersData = {
                "user_id": user_id,
                "username": username,
                "chats": [],
                "first_found_date": first_found_date,
            }
        else:
            UsersData = {
                "user_id": user_id,
                "username": username,
                "chats": [{"_id": 1, "chat_id": chat_id, "chat_title": chat_title}],
                "first_found_date": first_found_date,
            }

        await users.insert_one(UsersData)  # usernames are empty sometimes

    else:
        if "username" not in UserData or username != UserData["username"]:
            await users.update_one(
                {"user_id": user_id}, {"$set": {"username": username}}, upsert=True
            )

        GetUserChatList = []
        if "chats" not in UserData:
            return
        UsersChats = UserData["chats"]

        if len(UsersChats) == 0:
            return

        for UserChat in UsersChats:
            try:
                GetUserChat = UserChat.get("chat_id")
            except AttributeError:
                GetUserChat = UserChat
            GetUserChatList.append(GetUserChat)

        ChatsIDs = len(GetUserChatList) + 1
        if chat_id not in GetUserChatList:
            await users.update_one(
                {"user_id": user_id},
                {
                    "$push": {
                        "chats": {
                            "_id": ChatsIDs,
                            "chat_id": chat_id,
                            "chat_title": chat_title,
                        }
                    }
                },
            )


async def add_chat(chat_id, chat_title):
    ChatData = await chats.find_one({"chat_id": chat_id})

    if ChatData is None:
        ChatData = {
            "chat_id": chat_id,
            "chat_title": chat_title,
            "first_found_date": first_found_date,
        }

        await chats.insert_one(ChatData)
    else:
        await chats.update_one(
            {"chat_id": chat_id},
            {"$set": {"chat_id": chat_id, "chat_title": chat_title}},
            upsert=True,
        )


async def GetChatName(chat_id):
    ChatData = await chats.find_one({"chat_id": chat_id})
    if ChatData:
        chat_title = ChatData["chat_title"]
        return chat_title
    else:
        return None
