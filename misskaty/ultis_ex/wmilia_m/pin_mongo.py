from misskaty import db

pin = db.pin


async def cleanlinked_db(chat_id: int, cleanlinked: bool) -> None:
    pin_data = await pin.find_one({"chat_id": chat_id})

    if pin_data is None:
        await pin.insert_one(
            {
                "chat_id": chat_id,
                "cleanlinked": cleanlinked,
                "antichannelpin": None,
            }
        )
    else:
        await pin.update_one(
            {"chat_id": chat_id}, {"$set": {"cleanlinked": cleanlinked}}, upsert=True
        )


async def get_cleanlinked(chat_id: int) -> bool:
    pin_data = await pin.find_one({"chat_id": chat_id})

    if pin_data is not None:
        return pin_data["cleanlinked"]
    else:
        return False


async def antichannelpin_db(chat_id: int, antichannelpin: bool) -> None:
    pin_data = await pin.find_one({"chat_id": chat_id})
    if pin_data is None:
        await pin.insert_one(
            {
                "chat_id": chat_id,
                "cleanlinked": False,
                "antichannelpin": antichannelpin,
            }
        )
    else:
        await pin.update_one(
            {"chat_id": chat_id},
            {"$set": {"antichannelpin": antichannelpin}},
            upsert=True,
        )


async def get_antichannelpin(chat_id: int) -> bool:
    pin_data = await pin.find_one({"chat_id": chat_id})
    if pin_data is not None:
        return pin_data["antichannelpin"]
    else:
        return False
