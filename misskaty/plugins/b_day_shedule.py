import time
from asyncio import sleep
from traceback import format_exc

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.errors import UserNotParticipant

TIME_ZONE = "Asia/Kolkata"
from misskaty.vars import DATABASE_URI as BDB_URI

if BDB_URI:
    from misskaty.ultis_ex.database.bd_info import bday_cinfo, bday_info

from datetime import datetime, time
from random import choice
from pyrogram.enums import ChatMemberStatus

from misskaty.strings import birthday_wish


def give_date(date,form = "%d/%m/%Y"):
    datee = datetime.strptime(date,form).date()
    return datee

scheduler = AsyncIOScheduler()
scheduler.timezone = TIME_ZONE
scheduler_time = time(0,0,0)
async def send_wishish(JJK: Client):
    c_list = Chats.list_chats_by_id()
    blist = list(bday_info.find())
    curr = datetime.now(TIME_ZONE).date()
    cclist = list(bday_cinfo.find())
    for i in blist:
        dob = give_date(i["dob"])
        if dob.month == curr.month and dob.day == curr.day:
            for j in c_list:
                if cclist and (j in cclist):
                    return
                try:
                    agee = ""
                    if i["is_year"]:
                        agee = curr.year - dob.year
                        if str(agee).endswith("1"):
                            agee = f"{agee}st"
                        elif str(agee).endswith("2"):
                            agee = f"{agee}nd"
                        elif str(agee).endswith("3"):
                            agee = f"{agee}rd"
                        else:
                            agee = f"{agee}th"
                    U = await JJK.get_chat_member(chat_id=j,user_id=i["user_id"])
                    wish = choice(birthday_wish)
                    if U.status in [ChatMemberStatus.MEMBER,ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                        xXx = await JJK.send_message(j,f"Happy {agee} birthday {U.user.mention}🥳\n{wish}")
                        try:
                            await xXx.pin()
                        except Exception:
                            pass
                except Exception:
                    pass
