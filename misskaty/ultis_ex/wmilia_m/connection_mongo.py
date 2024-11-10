import datetime

from misskaty import db

connection = db.connection
chats = db.chats

first_found_date = datetime.datetime.now()


async def connectDB(user_id, chat_id):
    connectionData = await connection.find_one({"user_id": user_id})

    if connectionData is None:
        await connection.insert_one(
            {
                "user_id": user_id,
                "connection": True,
                "connected_chat": chat_id,
            }
        )
    else:
        await connection.update_one(
            {"user_id": user_id},
            {"$set": {"connection": True, "connected_chat": chat_id}},
            upsert=True,
        )


async def GetConnectedChat(user_id):
    connectionData = await connection.find_one({"user_id": user_id})
    if connectionData is not None:
        chat_id = connectionData["connected_chat"]
        return chat_id
    else:
        return None


async def isChatConnected(user_id) -> bool:
    connectionData = await connection.find_one({"user_id": user_id})
    if connectionData is not None:
        return connectionData["connection"]
    else:
        return False


async def disconnectChat(user_id):
    await connection.update_one({"user_id": user_id}, {"$set": {"connection": False}})


async def reconnectChat(user_id):
    await connection.update_one({"user_id": user_id}, {"$set": {"connection": True}})


async def allow_collection(chat_id, chat_title, allow_collection):
    chat_data = await chats.find_one({"chat_id": chat_id})
    if chat_data is None:

        ChatData = {
            "chat_id": chat_id,
            "chat_title": chat_title,
            "first_found_date": first_found_date,
            "allow_collection": allow_collection,
        }

        await chats.insert_one(ChatData)
    else:
        await chats.update_one(
            {"chat_id": chat_id},
            {"$set": {"allow_collection": allow_collection}},
            upsert=True,
        )


async def get_allow_connection(chat_id) -> bool:
    chat_data = await chats.find_one({"chat_id": chat_id})
    if chat_data is not None:
        if "allow_collection" in chat_data:
            return chat_data["allow_collection"]
        else:
            return False
    return False
