from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from misskaty import app as Bot, BOT_USERNAME, BOT_NAME
from misskaty.vars import SUDO_USERS

#============SUDO===≠===
#=================
SUDO_TEXT = """
Hi there sudo user👮‍♂️
Here is the help for DevCommand:

For Owner Bot Only.
/run [args] - Run eval CMD
/logs [int] - Check logs bot
/shell [args] - Run Exec/Terminal CMD
/download [link/reply_to_telegram_file] - Download file from Telegram
/disablechat [chat id] - Remove blacklist group
/enablechat [chat id] - Add Blacklist group
/banuser [chat id] - Ban user and block user so cannot use bot
/unbanuser [chat id] - Unban user and make their can use bot again
/gban - To Ban A User Globally.
/ungban - To remove ban user globbaly.
/restart - update and restart bot.

For Public Use
/stats - Check statistic bot
/json - Send structure message Telegram in JSON using Pyrogram Style.
"""
BUTTON_SUDO = [
    [
        InlineKeyboardButton("❮", callback_data="set_ge"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^sudo$"))
async def botCallbacks(_, CallbackQuery: CallbackQuery):
    clicker_user_id = CallbackQuery.from_user.id
    if clicker_user_id not in SUDO_USERS:
        return await CallbackQuery.answer(
            "You are not in the sudo user list.", show_alert=True)              
    await CallbackQuery.edit_message_text(
        SUDO_TEXT, reply_markup=InlineKeyboardMarkup(BUTTON_SUDO))
# =============START_CMD====================𝐺𝑜𝑗𝑜 𝑆𝑎𝑡𝑜𝑟𝑢 𝕏 | 𝐵𝑜𝑡</blockquote>
TEXT_ST = (
    "👋__Hello there {},__\n\n"
    "Welcome to the 🎈{}! This is a powerful group management bot⚡🌪️ for Telegram, I have 😌 many useful features for you, feel free to ➕add me to your group.\n\n"
    "**__Click /help to find out more about how to use me to me full potential!__**"
)
BUTTONS_ST = [
    [
        InlineKeyboardButton("➕Add Me To Your Group➕", url=f"http://t.me/{BOT_USERNAME}?startgroup=new",),
        ],[
        InlineKeyboardButton("📚 Commands ", callback_data="set_ge"),
        InlineKeyboardButton("📢 Channel", url="https://t.me/XBOTS_X"),
        ],[
        InlineKeyboardButton("📊 Status", callback_data="stats_callback"),
        InlineKeyboardButton("🪅 Stickers", url="https://t.me/stickers_collections_X"),
    ],
    [InlineKeyboardButton("❌", callback_data="close")],
]

@Bot.on_callback_query(filters.regex("^home$"))
async def st_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_ST.format(query.from_user.first_name, BOT_NAME),
        reply_markup=InlineKeyboardMarkup(BUTTONS_ST),
        disable_web_page_preview=True,
    )


# =======================f=======MAIN_HELP_CMD====================
TEXT_GE = """
Hey {} 👋
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. 
"""
BUTTONS_GE = [
    [
        InlineKeyboardButton("👮‍♂️ ɢʀᴏᴜᴘ", callback_data="group"),
        InlineKeyboardButton("➕ ᴇxᴛʀᴀ", callback_data="settings"),
    ],
    [
        InlineKeyboardButton("👥 sᴜᴅᴏ ᴜsᴇʀs", callback_data="sudo"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="home"),
        InlineKeyboardButton("❌", callback_data="close"),
    ],
]
@Bot.on_callback_query(filters.regex("^set_ge$"))
async def help_cb_handlerj1(bot, query):
    await query.message.edit(
        text=TEXT_GE.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_GE),
        disable_web_page_preview=True,
    )
@Bot.on_message(filters.command("help2") & filters.private)
async def hp_hagndlery(bot, message):
    await message.reply_text(
        text=TEXT_GE.format(message.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_GE),
        quote=True,
    )
#================GROUP_CMD=================
TEXT_GP = """
Hey 👋{}, Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Send command /privacy if you want know data collected by this bot.
General command are:
 - /start: Start the bot
 - /help: Give this message
"""
BUTTONS_GP = [
    [
        InlineKeyboardButton("Admin", callback_data="admi"),
        InlineKeyboardButton("Afk", callback_data="afk"),
    ],
    [
        InlineKeyboardButton("Bans", callback_data="ban"),
        InlineKeyboardButton("Warns", callback_data="war"),
    ],
    [
        InlineKeyboardButton("Purges", callback_data="prg"),
        InlineKeyboardButton("Ghost", callback_data="gst"),
    ],
    [
        InlineKeyboardButton("Reports", callback_data="rpt"),
        InlineKeyboardButton("Mention all", callback_data="mall"),
        
    ],
    [
        InlineKeyboardButton("Auto Approve", callback_data="aap"),
        InlineKeyboardButton("Blacklist", callback_data="bal"),
        
    ],
    [
        InlineKeyboardButton("Federation", callback_data="fed"),
        InlineKeyboardButton("Filters", callback_data="flt"),
        
    ],
    [
        InlineKeyboardButton("Locks", callback_data="lok"),
        InlineKeyboardButton("Notes", callback_data="not"),
        
    ],
    [
        InlineKeyboardButton("Night Mod", callback_data="nm"),
        InlineKeyboardButton("SangMata", callback_data="sm"),
    ],
    [
        InlineKeyboardButton("Pin", callback_data="pn"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="set_ge"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("🏠", callback_data="home"),
    ],
]
@Bot.on_callback_query(filters.regex("^group$"))
async def abvigjdv(bot, query):
    await query.message.edit(
        text=TEXT_GP.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_GP),
        disable_web_page_preview=True,
)
    
text_admi = """
**Here is the help for Admin**

Make it easy to promote and demote users with the admin module!

Admin commands:
- /adminlist: List the admins in the current chat.
- /promote <reply/username/mention/userid>: Promote a user.
- /demote <reply/username/mention/userid>: Demote a user.
- /fullpromote Promote A Member With All Rights.

**To Admins.**
/set_chat_title - Change The Name Of A Group/Channel.
/set_chat_photo - Change The PFP Of A Group/Channel.
/set_user_title - Change The Administrator Title Of An Admin.

Sometimes, you promote or demote an admin manually, and gojo doesn't realise it immediately.
This is because to avoid spamming telegram servers, admin status is cached locally.
"""
buttons_admi = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^admi$"))
async def abvijdv(bot, query):
    await query.message.edit(
        text=text_admi,
        reply_markup=InlineKeyboardMarkup(buttons_admi),
        disable_web_page_preview=True,
    )
    
text_afk = """
**Here is the help for AFK:**

/afk [Reason > Optional] - Tell others that you are AFK (Away From Keyboard), so that your boyfriend or girlfriend won't look for you 💔.
/afk [reply to media] - AFK with media.
/afkdel - Enable auto delete AFK message in group (Only for group admin). Default is Enable.

Just type something in group to remove AFK Status.
"""
buttons_afk = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^afk$"))
async def abviv(bot, query):
    await query.message.edit(
        text=text_afk,
        reply_markup=InlineKeyboardMarkup(buttons_afk),
        disable_web_page_preview=True,
    )

text_ban = """
**Here is the help for Bans**

Some people need to be publicly banned; spammers, annoyances, or just trolls.
This module allows you to do that easily, by exposing some common actions, so everyone will see!

User commands:
- /kickme: Users that use this, kick themselves.

**Admin commands:**
**Ban**
/ban - Ban A User From A Group
/dban - Delete the replied message banning its sender
/tban - Ban A User For Specific Time
/unban - Unban A User
/listban - Ban a user from groups listed in a message
/listunban - Unban a user from groups listed in a message

**Mute:**
/mute: Mute a user.
/tmute: Temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
/unmute: Unmute a user.

**Kick**
/kick: Kick a user.
/dkick - Delete the replied message kicking its sender

**Examples:**
- Mute a user for two hours.
-> /tmute @username 2h
"""
buttons_ban = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^ban$"))
async def abanv(bot, query):
    await query.message.edit(
        text=text_ban,
        reply_markup=InlineKeyboardMarkup(buttons_ban),
        disable_web_page_preview=True,
    )

text_war = """
**Here is the help for Warnings**

Keep your members in check with warnings; stop them getting out of control!

/warn <reason>: - Warn A User
/dwarn <reason>: - Delete the replied message warning its sender
/rmwarns - Remove All Warning of A User
/warns - Show Warning Of A User.
"""
buttons_war = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^war$"))
async def abvivwar(bot, query):
    await query.message.edit(
        text=text_war,
        reply_markup=InlineKeyboardMarkup(buttons_war),
        disable_web_page_preview=True,
    )

text_prg = """
**Here is the help for Purges**

Need to delete lots of messages? That's what purges are for!

/purge - Delete all messages from the replied to message, to the current message.
/purge [n] - Purge "n" number of messages from replied message
/del - Delete Replied Message

**Examples:**
- Delete all messages from the replied to message, until now.
---> /purge
"""
buttons_prg = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^prg$"))
async def abvprviv(bot, query):
    await query.message.edit(
        text=text_prg,
        reply_markup=InlineKeyboardMarkup(buttons_prg),
        disable_web_page_preview=True,
    )

text_gst = """
**Here is the help for Ghost**

/instatus - View member status in group
/ban_ghosts Remove deleted Ghosts accounts from group 

note:
- ᴜsᴇ ᴅɪʀᴇᴄᴛʟʏ ɪɴ ᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍᴇ ғᴏʀ ʙᴇsᴛ ᴇғғᴇᴄᴛ. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.
"""
buttons_gst = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^gst$"))
async def abvgstiv(bot, query):
    await query.message.edit(
        text=text_gst,
        reply_markup=InlineKeyboardMarkup(buttons_gst),
        disable_web_page_preview=True,
    )

text_rpt = """
**Here is the help for Reports**

We're all busy people who don't have time to monitor our groups 24/7. But how do you react if someone in your group is spamming?

Presenting reports; if someone in your group thinks someone needs reporting, they now have an easy way to call all admins.

/report | @admins | @admin - Report A Message To Admins.
- /report: Reply to a message to report it for admins to review.
- admin: Same as /report

Note that the report commands do not work when admins use them; or when used to report an admin. Rose assumes that admins don't need to report, or be reported!
"""
buttons_rpt = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^rpt$"))
async def abvivrpt(bot, query):
    await query.message.edit(
        text=text_rpt,
        reply_markup=InlineKeyboardMarkup(buttons_rpt),
        disable_web_page_preview=True,
    )

text_mal = """
**Here is the help for Mention all**

/mentionall - Mention all members in a groups in one click.
"""
buttons_mal = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^mall$"))
async def abvmaggliv(bot, query):
    await query.message.edit(
        text=text_mal,
        reply_markup=InlineKeyboardMarkup(buttons_mal),
        disable_web_page_preview=True,
    )

text_aap = """
**Here is the help for Autoapprove:**

- /autoapprove just type in group.

This module helps to automatically accept chat join request send by a user through invitation link of your group
"""
buttons_aap = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^aap$"))
async def aaapbviv(bot, query):
    await query.message.edit(
        text=text_aap,
        reply_markup=InlineKeyboardMarkup(buttons_aap),
        disable_web_page_preview=True,
    )

text_bal = """
**Here is the help for Blacklist:**

Want to stop people asking stupid questions? or ban anyone saying censored words? Blocklists is the module for you!
From blocking rude words, filenames/extensions, to specific emoji, everything is possible.

/blacklisted - Get All The Blacklisted Words In The Chat.
/blacklist [WORD|SENTENCE] - Blacklist A Word Or A Sentence.
/whitelist [WORD|SENTENCE] - Whitelist A Word Or A Sentence.
"""
buttons_bal = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^bal$"))
async def abvbaliv(bot, query):
    await query.message.edit(
        text=text_bal,
        reply_markup=InlineKeyboardMarkup(buttons_bal),
        disable_web_page_preview=True,
    )

#============FEDERATION==============
text_fed = """
**Here is the help for Federation:**

Everything is fun, until a spammer starts entering your group, and you have to block it. Then you need to start banning more, and more, and it hurts.
But then you have many groups, and you don't want this spammer to be in one of your groups - how can you deal? Do you have to manually block it, in all your groups?

No longer! With Federation, you can make a ban in one chat overlap with all other chats.

You can even designate federation admins, so your trusted admin can ban all the spammers from chats you want to protect.
"""
buttons_fed = [
    [
        InlineKeyboardButton("👮‍♂️Fed Owner Commands", callback_data="fdo"),
        InlineKeyboardButton("👷‍♀️Fed Admin Commands", callback_data="fdm"),
        ],
        [
        InlineKeyboardButton("🧒User Commands", callback_data="fdu"),
        ],
        [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]
@Bot.on_callback_query(filters.regex("^fed$"))
async def abfdviv(bot, query):
    await query.message.edit(
        text=text_fed,
        reply_markup=InlineKeyboardMarkup(buttons_fed),
        disable_web_page_preview=True,
    )
text_fdo = """
👑 **Fed Owner Only:**

These are the list of available fed owner commands. To run these, you have to own the current federation. 

**Owner Commands:**
 • /newfed <fed_name>: Creates a Federation, One allowed per user
 • /renamefed <fed_id> <new_fed_name>: Renames the fed id to a new name
 • /delfed <fed_id>: Delete a Federation, and any information related to it. Will not cancel blocked users
 • /myfeds: To list the federations that you have created
 • /fedtransfer <new_owner> <fed_id>:To transfer fed ownership to another person
 • /fpromote <user>: Assigns the user as a federation admin. Enables all commands for the user under Fed Admins
 • /fdemote <user>: Drops the User from the admin Federation to a normal User
 • /setfedlog <fed_id>: Sets the group as a fed log report base for the federation
 • /unsetfedlog <fed_id>: Removed the group as a fed log report base for the federation
 • /fbroadcast : Broadcasts a messages to all groups that have joined your fed
"""
buttons_fdo = [
    [
        InlineKeyboardButton("⬅️", callback_data="fed"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^fdo$"))
async def afdobviv(bot, query):
    await query.message.edit(
        text=text_fdo,
        reply_markup=InlineKeyboardMarkup(buttons_fdo),
        disable_web_page_preview=True,
    )

text_fdm = """
🔱 **Fed Admins:**

The following is the list of all fed admin commands. To run these, you have to be a federation admin in the current federation.

 • /fban <user> <reason>: Fed bans a user
 • /sfban: Fban a user without sending notification to chats
 • /unfban <user> <reason>: Removes a user from a fed ban
 • /sunfban: Unfban a user without sending a notification
 • /fedadmins: Show Federation admin
 • /fedchats <FedID>: Get all the chats that are connected in the Federation
 • /fbroadcast : Broadcasts a messages to all groups that have joined your fed
"""
buttons_fdm = [
    [
        InlineKeyboardButton("⬅️", callback_data="fed"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^fdm$"))
async def abvifdmv(bot, query):
    await query.message.edit(
        text=text_fdm,
        reply_markup=InlineKeyboardMarkup(buttons_fdm),
        disable_web_page_preview=True,
    )

text_fdu = """
**User Commands:**

These commands do not require you to be admin of a federation. These commands are for general commands, such as looking up information on a fed, or checking a user's fbans.

• /fedinfo <FedID>: Information about a federation.
• /fedadmins <FedID>: List the admins in a federation.
• /joinfed <FedID>: Join the current chat to a federation. A chat can only join one federation. Chat owners only.
• /leavefed: Leave the current federation. Only chat owners can do this.
• /fedstat <FedID>: Gives information about your ban in a federation.
• /fedstat <user ID> <FedID>: Gives information about a user's ban in a federation.
• /chatfed: Information about the federation the current chat is in.
"""
buttons_fdu = [
    [
        InlineKeyboardButton("⬅️", callback_data="fed"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^fdu$"))
async def ajbvfduiv(bot, query):
    await query.message.edit(
        text=text_fdu,
        reply_markup=InlineKeyboardMarkup(buttons_fdu),
        disable_web_page_preview=True,
    )

text_flt = """
**Here is the help for Filters:**

Make your chat more lively with filters; The bot will reply to certain words!

Filters are case insensitive; every time someone says your trigger words, Rose will reply something else! can be used to create your own commands, if desired.

/filters To Get All The Filters In The Chat.
/filter [FILTER_NAME] or /addfilter [FILTER_NAME] To Save A Filter(reply to a message).

Supported filter types are Text, Animation, Photo, Document, Video, video notes, Audio, Voice.

To use more words in a filter use.
/filter Hey_there or /addfilter Hey_there To filter "Hey there".
/stop [FILTER_NAME] or /stopfilter [FILTER_NAME] To Stop A Filter.
/stopall To delete all the filters in a chat (permanently).

You can use markdown or html to save text too.
"""
buttons_flt = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^flt$"))
async def afilbviv(bot, query):
    await query.message.edit(
        text=text_flt,
        reply_markup=InlineKeyboardMarkup(buttons_flt),
        disable_web_page_preview=True,
    )

text_lok = """
**Here is the help for Locks:**

Do stickers annoy you? or want to avoid people sharing links? or pictures? You're in the right place!

The locks module allows you to lock away some common items in the Telegram world; the bot will automatically delete them!

- /lock | /unlock | /locks [No Parameters Required]

Parameters:
    messages | sticker | gif | media | games | polls

    inline  | url | group_info | user_add | pin | photo

    voice | video | audio | docs | plain

You can only pass the "all" parameter with /lock, not with /unlock

Example:
    /lock all
"""
buttons_lok = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^lok$"))
async def lokkabviv(bot, query):
    await query.message.edit(
        text=text_lok,
        reply_markup=InlineKeyboardMarkup(buttons_lok),
        disable_web_page_preview=True,
    )

text_not = """
**Here is the help for Notes:**

Save data for future users with notes!
Notes are great to save random tidbits of information; a phone number, a nice gif, a funny picture - anything!

/notes To Get All The Notes In The Chat.

/save [NOTE_NAME] or /addnote [NOTE_NAME] To Save A Note.

Supported note types are Text, Animation, Photo, Document, Video, video notes, Audio, Voice.

To change caption of any files use.
/save [NOTE_NAME] or /addnote [NOTE_NAME] [NEW_CAPTION].

#NOTE_NAME To Get A Note.

/delete [NOTE_NAME] or delnote [NOTE_NAME] To Delete A Note.
/deleteall To delete all the notes in a chat (permanently).
"""
buttons_not = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^not$"))
async def notabviv(bot, query):
    await query.message.edit(
        text=text_not,
        reply_markup=InlineKeyboardMarkup(buttons_not),
        disable_web_page_preview=True,
    )

text_nm = """
**Here is the help for NightMode:**

Enable or disable nightmode (locks the chat at specified intervals everyday)
Flags:
'-s': "Specify starting time in 24hr format."
'-e': "Specify duration in hours / minute"
'-d': "Disable nightmode for chat."

Examples:
/nightmode -s=23:53 -e=6h
/nightmode -s=23:50 -e=120m
/nightmode -d
"""
buttons_nm = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^nm$"))
async def abvnmmiv(bot, query):
    await query.message.edit(
        text=text_nm,
        reply_markup=InlineKeyboardMarkup(buttons_nm),
        disable_web_page_preview=True,
    )

text_sm = """
**Here is the help for SangMata:**

This feature inspired from SangMata Bot. I'm created simple detection to check user data include username, first_name, and last_name.
/sangmata_set [on/off] - Enable/disable sangmata in groups.
"""
buttons_sm = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^sm$"))
async def abvivmfg(bot, query):
    await query.message.edit(
        text=text_sm,
        reply_markup=InlineKeyboardMarkup(buttons_sm),
        disable_web_page_preview=True,
    )

text_pn = """
**Here is the help for Pin**

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

Admin commands:
- /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
- /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.
- /unpinall: Unpins all pinned messages.
"""

buttons_pn = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^pn$"))
async def abvivpn(bot, query):
    await query.message.edit(
        text=text_pn,
        reply_markup=InlineKeyboardMarkup(buttons_pn),
        disable_web_page_preview=True,
    )


#===================

TEXT_HP = """
Hey 👋 {}, Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Send command /privacy if you want know data collected by this bot.
Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP = [
    [
        InlineKeyboardButton("Acᴛɪᴠᴇ", callback_data="act"),
        InlineKeyboardButton("Adᴍɪɴ", callback_data="adm"),
        InlineKeyboardButton("Auᴛʜ", callback_data="aut"),
    ],
    [
        InlineKeyboardButton("Aᴅᴠɪᴄᴇ", callback_data="adv"),
        InlineKeyboardButton("Aᴘᴘʀᴏᴠᴇ", callback_data="apr"),
        InlineKeyboardButton("B-ʟɪsᴛ", callback_data="blt"),
    ],
    [
        InlineKeyboardButton("Boᴛ", callback_data="bt"),
        InlineKeyboardButton("Bᴀɴ", callback_data="bn"),
        InlineKeyboardButton("Bᴏᴛs", callback_data="bts"),
    ],
    [
        InlineKeyboardButton("Bᴏᴛsᴄʜᴋ", callback_data="bsk"),
        InlineKeyboardButton("Cʜᴀᴛ Ai", callback_data="ai"),
        InlineKeyboardButton("Deᴠ", callback_data="dv"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings5"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("🏠", callback_data="home"),
        InlineKeyboardButton("❯", callback_data="settings2"),
    ],
] 

@Bot.on_callback_query(filters.regex("^settings$"))
async def help_cb_handler1(bot, query):
    await query.message.edit(
        text=TEXT_HP.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP),
        disable_web_page_preview=True,
    )


TEXT_HP2 = """
Hey 👋 {}, Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP2 = [
    [
        InlineKeyboardButton("Filters", callback_data="flt"),
        InlineKeyboardButton("Fɪɢʟᴇᴛ", callback_data="fgl"),
        InlineKeyboardButton("Fᴀᴋᴇ", callback_data="fk"),
    ],
    [
        InlineKeyboardButton("Fᴏɴᴛ", callback_data="fon"),
        InlineKeyboardButton("Fᴜɴ", callback_data="fn"),
        InlineKeyboardButton("G-ᴄᴀsᴛ", callback_data="gt"),
    ],
    [
        InlineKeyboardButton("Gʀᴏᴜᴘ Lɪɴᴋ", callback_data="gl"),
        InlineKeyboardButton("Gᴀʟɪ", callback_data="gli"),
        InlineKeyboardButton("sᴇᴀʀᴄʜ", callback_data="src"),
    ],
    [
        InlineKeyboardButton("Gᴏᴏᴅʙʏᴇ", callback_data="gdy"),
        InlineKeyboardButton("Hɪsᴛᴏʀʏ", callback_data="hsr"),
        InlineKeyboardButton("Hᴀsʜᴛᴀɢ", callback_data="htg"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("🏠", callback_data="home"),
        InlineKeyboardButton("❯", callback_data="settings3"),
    ],
]


@Bot.on_callback_query(filters.regex("^settings2$"))
async def help_cb_handler2(bot, query):
    await query.message.edit(
        text=TEXT_HP2.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP2),
        disable_web_page_preview=True,
    )


TEXT_HP3 = """
Hey 👋 {}, Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP3 = [
    [
        InlineKeyboardButton("Hᴜɢ", callback_data="hg"),
        InlineKeyboardButton("Lᴏᴠᴇ", callback_data="lv"),
        InlineKeyboardButton("Mᴀᴛʜ", callback_data="mt"),
    ],
    [
        InlineKeyboardButton("Mᴏɴɢᴏᴅʙ", callback_data="mog"),
        InlineKeyboardButton("Nᴏᴛᴇs", callback_data="not"),
        InlineKeyboardButton("Pᴀᴜsᴇ", callback_data="ps"),
    ],
    [
        InlineKeyboardButton("Plᴀʏ", callback_data="ply"),
        InlineKeyboardButton("SᴀɴɢMᴀᴛᴀ", callback_data="sg"),
        InlineKeyboardButton("Pʏᴘɪ", callback_data="pyp"),
    ],
    [
        InlineKeyboardButton("Pʟᴀʏʟɪsᴛ", callback_data="pay"),
        InlineKeyboardButton("Qʀɢᴇɴ", callback_data="qr"),
        InlineKeyboardButton("Deᴠ", callback_data="dv"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings2"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("🏠", callback_data="home"),
        InlineKeyboardButton("❯", callback_data="settings4"),
    ],
]


@Bot.on_callback_query(filters.regex("^settings3$"))
async def help_cb_handler3(bot, query):
    await query.message.edit(
        text=TEXT_HP3.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP3),
        disable_web_page_preview=True,
    )


TEXT_HP4 = """
Hey 👋 {}, Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP4 = [
    [
        InlineKeyboardButton("Qᴜᴏᴛᴇ", callback_data="quo"),
        InlineKeyboardButton("Rᴀᴅɪᴏ", callback_data="rd"),
        InlineKeyboardButton("Resume", callback_data="rsm"),
    ],
    [
        InlineKeyboardButton("Rᴇᴘᴏ", callback_data="rep"),
        InlineKeyboardButton("Speed", callback_data="spd"),
        InlineKeyboardButton("Tag", callback_data="tag"),
    ],
    [
        InlineKeyboardButton("Sʟᴀᴘ", callback_data="sl"),
        InlineKeyboardButton("Sᴛɪᴄᴋᴇʀ", callback_data="stk"),
        InlineKeyboardButton("Tʀᴜᴛʜ", callback_data="trt"),
    ],
    [
        InlineKeyboardButton("Tᴀɢᴀʟʟ", callback_data="tgl"),
        InlineKeyboardButton("Tᴇʟᴇɢʀᴀᴘʜ", callback_data="tgr"),
        InlineKeyboardButton("Tᴛs", callback_data="tt"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings3"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("🏠", callback_data="home"),
        InlineKeyboardButton("❯", callback_data="setting5"),
    ],
]


@Bot.on_callback_query(filters.regex("^settings4$"))
async def help_cb_handler4(bot, query):
    await query.message.edit(
        text=TEXT_HP4.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP4),
        disable_web_page_preview=True,
    )


TEXT_HP5 = """
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ. Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ  ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ.

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /
"""
BUTTONS_HP5 = [
    [
        InlineKeyboardButton("Usᴇʀ Iɴғᴏ", callback_data="ui"),
        InlineKeyboardButton("Usᴇʀɪᴅ", callback_data="ud"),
        InlineKeyboardButton("Wʀɪᴛᴇ", callback_data="wr"),
    ],
    [
        InlineKeyboardButton("Wʜᴏɪs", callback_data="wh"),
        InlineKeyboardButton("Wᴀʟʟ", callback_data="wl"),
        InlineKeyboardButton("Wᴇʙᴅʟ", callback_data="wd"),
    ],
    [
        InlineKeyboardButton("Yᴛʜᴜᴍʙ", callback_data="yh"),
        InlineKeyboardButton("Zᴏᴍʙɪᴇs", callback_data="zm"),
        InlineKeyboardButton("...", callback_data=""),
    ],
    [
        InlineKeyboardButton("...", callback_data="f"),
        InlineKeyboardButton("...", callback_data="d"),
        InlineKeyboardButton("...", callback_data="d"),
    ],
    [
        InlineKeyboardButton("❮", callback_data="settings4"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("🏠", callback_data="home"),
        InlineKeyboardButton("❯", callback_data="settings"),
    ],
]


@Bot.on_callback_query(filters.regex("^settings5$"))
async def help_cb_handler5(bot, query):
    await query.message.edit(
        text=TEXT_HP5.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP5),
        disable_web_page_preview=True,
    )


# =============================EXTRA_CMD================================
# =============================EXTRA_CMD================================

text_act = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Acᴛɪᴠᴇ:

々 /ac - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ ʙᴏᴛ.

々 /activevoice - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴀɴᴅ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴏɴ ʙᴏᴛ.

々 /activevideo - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴏɴ ʙᴏᴛ.

々 /stats - Cʜᴇᴄᴋ Bᴏᴛs Sᴛᴀᴛs
"""
buttons_act = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^act$"))
async def abot_cb_handler6(bot, query):
    await query.message.edit(
        text=text_act,
        reply_markup=InlineKeyboardMarkup(buttons_act),
        disable_web_page_preview=True,
    )


text_adm = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Adᴍɪɴ:
c sᴛᴀɴᴅs ғᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ.

々 /pause ᴏʀ /cpause - Pᴀᴜsᴇ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /resume ᴏʀ /cresume - Rᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ ᴍᴜsɪᴄ.
々 /mute ᴏʀ /cmute - Mᴜᴛᴇ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /unmute ᴏʀ /cunmute - Uɴᴍᴜᴛᴇ ᴛʜᴇ ᴍᴜᴛᴇᴅ ᴍᴜsɪᴄ.
々 /skip ᴏʀ /cskip - Sᴋɪᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /stop ᴏʀ /cstop - Sᴛᴏᴘ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
々 /shuffle ᴏʀ /cshuffle - Rᴀɴᴅᴏᴍʟʏ sʜᴜғғʟᴇs ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴘʟᴀʏʟɪsᴛ.
々 /seek ᴏʀ /cseek - Fᴏʀᴡᴀʀᴅ Sᴇᴇᴋ ᴛʜᴇ ᴍᴜsɪᴄ ᴛᴏ ʏᴏᴜʀ ᴅᴜʀᴀᴛɪᴏɴ.
々 /seekback ᴏʀ /cseekback - Bᴀᴄᴋᴡᴀʀᴅ Sᴇᴇᴋ ᴛʜᴇ ᴍᴜsɪᴄ ᴛᴏ ʏᴏᴜʀ ᴅᴜʀᴀᴛɪᴏɴ.
々 /reboot - Rᴇʙᴏᴏᴛ ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ.

々 /skip ᴏʀ /cskip [Nᴜᴍʙᴇʀ (ᴇxᴀᴍᴘʟᴇ: 𝟹)] - Sᴋɪᴘs ᴍᴜsɪᴄ ᴛᴏ ᴀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ǫᴜᴇᴜᴇᴅ ɴᴜᴍʙᴇʀ. Exᴀᴍᴘʟᴇ: /skip 𝟹 ᴡɪʟʟ sᴋɪᴘ ᴍᴜsɪᴄ ᴛᴏ ᴛʜɪʀᴅ ǫᴜᴇᴜᴇᴅ ᴍᴜsɪᴄ ᴀɴᴅ ᴡɪʟʟ ɪɢɴᴏʀᴇ 𝟷 ᴀɴᴅ 𝟸 ᴍᴜsɪᴄ ɪɴ ǫᴜᴇᴜᴇ.
々 /loop ᴏʀ /cloop [ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ] ᴏʀ [Nᴜᴍʙᴇʀs ʙᴇᴛᴡᴇᴇɴ 𝟷-𝟷𝟶] - Wʜᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ, ʙᴏᴛ ʟᴏᴏᴘs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ ᴛᴏ 𝟷-𝟷𝟶 ᴛɪᴍᴇs ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. Dᴇғᴀᴜʟᴛ ᴛᴏ 𝟷𝟶 ᴛɪᴍᴇs.
"""
buttons_adm = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^adm$"))
async def abot_cb_handler7(bot, query):
    await query.message.edit(
        text=text_adm,
        reply_markup=InlineKeyboardMarkup(buttons_adm),
        disable_web_page_preview=True,
    )


text_aut = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Auᴛʜ:

Aᴜᴛʜ Usᴇʀs ᴄᴀɴ ᴜsᴇ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.

々 /auth [Usᴇʀɴᴀᴍᴇ] - Aᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.

々 /unauth [Usᴇʀɴᴀᴍᴇ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.

々 /authusers - Cʜᴇᴄᴋ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
"""
buttons_aut = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^aut$"))
async def abot_cb_handler8(bot, query):
    await query.message.edit(
        text=text_aut,
        reply_markup=InlineKeyboardMarkup(buttons_aut),
        disable_web_page_preview=True,
    )


text_adv = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Aᴅᴠɪᴄᴇ:

々 /advice - Gᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ
々 /astronomical - ᴛᴏ ɢᴇᴛ ᴛᴏᴅᴀʏ's ᴀsᴛʀᴏɴᴏᴍɪᴄᴀʟ  ғᴀᴄᴛ
"""
buttons_adv = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^adv$"))
async def abot_cb_handler9(bot, query):
    await query.message.edit(
        text=text_adv,
        reply_markup=InlineKeyboardMarkup(buttons_adv),
        disable_web_page_preview=True,
    )


text_apr = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Aᴘᴘʀᴏᴠᴇ:

Tʜɪs ᴍᴏᴅᴜʟᴇ ʜᴇʟᴘs ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴄᴄᴇᴘᴛ ᴄʜᴀᴛ ɪᴏɪɴ ʀᴇǫᴜᴇsᴛ sᴇɴᴅ ʙʏ ᴀ ᴜsᴇʀ ᴛʜʀᴏᴜɢʜ ɪɴᴠɪᴛᴀᴛɪᴏɴ ʟɪɴᴋ ᴏғ ʏᴏᴜʀ ɢʀᴏᴜᴘ

Mᴏᴅᴇs:
ᴡʜᴇɴ ʏᴏᴜ sᴇɴᴅ /autoapprove ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʏᴏᴜ sᴇᴇ ᴛᴜʀɴ ᴏɴ ʙᴜᴛᴛᴏɴ ɪғ ᴀᴜᴛᴛᴏᴘʀᴏᴠᴇ ɴᴏᴛ ᴇɴᴀʙʟᴇᴅ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ ɪғ ᴀʟʀᴇᴅʏ ᴛᴜʀɴᴇᴅ ᴏɴ ʏᴏᴜ ᴡɪʟʟ sᴇ ᴛᴡᴏ ᴍᴏᴅᴇs ᴛʜᴀᴛ's ᴀʀᴇ ʙᴇʟᴏᴡ ᴀɴᴅ ʜɪs ᴜsᴀsɢᴇ


々 Automatic - ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴄᴄᴇᴘᴛs ᴄʜᴀᴛ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ.

々 Manual - ᴀ ᴍᴇssᴀɢᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ ʙʏ ᴛᴀɢɢɪɴɢ ᴛʜᴇ ᴀᴅᴍɪɴs. ᴛʜᴇ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴄᴄᴇᴘᴛ ᴏʀ ᴅᴇᴄʟɪɴᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛs.

々 /clearpending ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴘᴇɴᴅɪɴɢ ᴜsᴇʀ ɪᴅ ғʀᴏᴍ ᴅʙ. ᴛʜɪs ᴡɪʟʟ ᴀʟʟᴏᴡ ᴛʜᴇ ᴜsᴇʀ ᴛᴏ sᴇɴᴅ ʀᴇǫᴜᴇsᴛ ᴀɢᴀɪɴ.
"""
buttons_apr = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^apr$"))
async def abot_cb_handler10(bot, query):
    await query.message.edit(
        text=text_apr,
        reply_markup=InlineKeyboardMarkup(buttons_apr),
        disable_web_page_preview=True,
    )


text_blt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ B-ʟɪsᴛ:

々 /blacklistchat [ᴄʜᴀᴛ ɪᴅ] - Bʟᴀᴄᴋʟɪsᴛ ᴀɴʏ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ Mᴜsɪᴄ Bᴏᴛ
々 /whitelistchat [ᴄʜᴀᴛ ɪᴅ] - Wʜɪᴛᴇʟɪsᴛ ᴀɴʏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ Mᴜsɪᴄ Bᴏᴛ
々 /blacklistedchat - Cʜᴇᴄᴋ ᴀʟʟ ʙʟᴏᴄᴋᴇᴅ ᴄʜᴀᴛs.

々 /block [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Pʀᴇᴠᴇɴᴛs ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴜsɪɴɢ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs.
々 /unblock [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ Bᴏᴛ's Bʟᴏᴄᴋᴇᴅ Lɪsᴛ.
々 /blockedusers - Cʜᴇᴄᴋ ʙʟᴏᴄᴋᴇᴅ Usᴇʀs Lɪsᴛs

ⓘ /gban [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Gʙᴀɴ ᴀ ᴜsᴇʀ ғʀᴏᴍ ʙᴏᴛ's sᴇʀᴠᴇᴅ ᴄʜᴀᴛ ᴀɴᴅ sᴛᴏᴘ ʜɪᴍ ғʀᴏᴍ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ.
ⓘ /ungban [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ Bᴏᴛ's ɢʙᴀɴɴᴇᴅ Lɪsᴛ ᴀɴᴅ ᴀʟʟᴏᴡ ʜɪᴍ ғᴏʀ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ
ⓘ /gbannedusers - Cʜᴇᴄᴋ Gʙᴀɴɴᴇᴅ Usᴇʀs Lɪsᴛs
"""
buttons_blt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^blt$"))
async def abot_cb_handlerh(bot, query):
    await query.message.edit(
        text=text_blt,
        reply_markup=InlineKeyboardMarkup(buttons_blt),
        disable_web_page_preview=True,
    )


text_bt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Boᴛ:

々 c sᴛᴀɴᴅs ғᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ.

々 /stats - Gᴇᴛ Tᴏᴘ 𝟷𝟶 Tʀᴀᴄᴋs Gʟᴏʙᴀʟ Sᴛᴀᴛs, Tᴏᴘ 𝟷𝟶 Usᴇʀs ᴏғ ʙᴏᴛ, Tᴏᴘ 𝟷𝟶 Cʜᴀᴛs ᴏɴ ʙᴏᴛ, Tᴏᴘ 𝟷𝟶 Pʟᴀʏᴇᴅ ɪɴ ᴀ ᴄʜᴀᴛ ᴇᴛᴄ ᴇᴛᴄ.

々 /sudolist - Cʜᴇᴄᴋ Sᴜᴅᴏ Usᴇʀs ᴏғ Bᴏᴛ

々 /lyrics [Mᴜsɪᴄ Nᴀᴍᴇ] - Sᴇᴀʀᴄʜᴇs Lʏʀɪᴄs ғᴏʀ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ Mᴜsɪᴄ ᴏɴ ᴡᴇʙ.

々 /player - Gᴇᴛ ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ Pʟᴀʏɪɴɢ Pᴀɴᴇʟ.

々 /queue ᴏʀ /cqueue - Cʜᴇᴄᴋ Qᴜᴇᴜᴇ Lɪsᴛ ᴏғ Mᴜsɪᴄ.

    ⚡️Pʀɪᴠᴀᴛᴇ Bᴏᴛ:  
ⓘ /authorize [CHAT_ID] - Aʟʟᴏᴡ ᴀ ᴄʜᴀᴛ ғᴏʀ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ.

ⓘ /unauthorize[CHAT_ID] - Dɪsᴀʟʟᴏᴡ ᴀ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ.

ⓘ /authorized - Cʜᴇᴄᴋ ᴀʟʟ ᴀʟʟᴏᴡᴇᴅ ᴄʜᴀᴛs ᴏғ ʏᴏᴜʀ ʙᴏᴛ.
"""
buttons_bt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^bt$"))
async def abot_cb_handlersv(bot, query):
    await query.message.edit(
        text=text_bt,
        reply_markup=InlineKeyboardMarkup(buttons_bt),
        disable_web_page_preview=True,
    )


text_bn = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Bᴀɴ:

/ban - Ban A User
/banall - Ban All Users
/sban - Delete all messages of user that sended in group and ban the user
/tban - Ban A User For Specific Time
/unban - Unban A User
/warn - Warn A User
/swarn - Delete all the message sended in group and warn the user
/rmwarns - Remove All Warning of A User
/warns - Show Warning Of A User
/kick - Kick A User
/skick - Delete the replied message kicking its sender
/purge - Purge Messages
/purge [n] - Purge "n" number of messages from replied message
/del - Delete Replied Message
/promote - Promote A Member
/fullpromote - Promote A Member With All Rights
/demote - Demote A Member
/pin - Pin A Message
/unpin - unpin a message
/unpinall - unpinall messages
/mute - Mute A User
/tmute - Mute A User For Specific Time
/unmute - Unmute A User
/zombies - Ban Deleted Accounts
/report | @admins | @admin - Report A Message To Admins.
"""
buttons_bn = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^bn$"))
async def abot_cb_handlufer(bot, query):
    await query.message.edit(
        text=text_bn,
        reply_markup=InlineKeyboardMarkup(buttons_bn),
        disable_web_page_preview=True,
    )


text_bts = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Bᴏᴛs:

ʙᴏᴛs

々 /bots - ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ʙᴏᴛs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
"""
buttons_bts = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^bts$"))
async def abot_cb_handlgguer(bot, query):
    await query.message.edit(
        text=text_bts,
        reply_markup=InlineKeyboardMarkup(buttons_bts),
        disable_web_page_preview=True,
    )


text_bsk = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Bᴏᴛsᴄʜᴋ:

Dᴇsᴄʀɪᴘᴛɪᴏɴ:
Cʜᴇᴄᴋs ᴛʜᴇ ᴏɴɪɴᴇ sᴛᴀᴛᴜs ᴏғ ᴀ sᴘᴇᴄɪғɪᴇᴅ ʙᴏᴛ ʙʏ sᴇɴᴅɪɴɢ ɪᴛ ᴀ /start ᴍᴇssᴀɢᴇ.

Usᴀɢᴇ:
/botschk Bᴏᴛ_Usᴇʀɴᴀᴍᴇ

Dᴇᴛᴀɪs:
々 Sᴇɴᴅs /start ᴛᴏ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ʙᴏᴛ ᴀɴᴅ ᴄʜᴇᴄᴋs ɪғ ɪᴛ ʀᴇsᴘᴏɴᴅs.
々 Dɪsᴘᴀʏs ᴛʜᴇ ʙᴏᴛ's sᴛᴀᴛᴜs ᴀs ᴇɪᴛʜᴇʀ ᴏɴɪɴᴇ ᴏʀ ᴏғғɪɴᴇ.

Exᴀᴍᴘᴇs:
々 /botschk @YᴏᴜʀBᴏᴛUsᴇʀɴᴀᴍᴇ: Cʜᴇᴄᴋs ɪғ @YᴏᴜʀBᴏᴛUsᴇʀɴᴀᴍᴇ ɪs ᴏɴɪɴᴇ ᴏʀ ᴏғғɪɴᴇ.

Nᴏᴛᴇs:
々 Tʜᴇ ʙᴏᴛ ᴜsᴇʀɴᴀᴍᴇ ᴍᴜsᴛ ʙᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴀs ᴀɴ ᴀʀɢᴜᴍᴇɴᴛ.
々 Tʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴡɪ ᴅɪsᴘᴀʏ ᴀɴ ᴇʀʀᴏʀ ᴍᴇssᴀɢᴇ ɪғ ᴛʜᴇ ᴜsᴇʀɴᴀᴍᴇ ɪs ɪɴᴄᴏʀʀᴇᴄᴛ ᴏʀ ɪғ ᴛʜᴇʀᴇ ᴀʀᴇ ɪᴍɪᴛᴀᴛɪᴏɴs.

Oᴜᴛᴘᴜᴛ:
々 Dɪsᴘᴀʏs ᴛʜᴇ ʙᴏᴛ's ᴍᴇɴᴛɪᴏɴ ᴀɴᴅ ɪᴛs ᴏɴɪɴᴇ sᴛᴀᴛᴜs.
々 Sʜᴏᴡs ᴛʜᴇ ᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴛɪᴍᴇ.
"""
buttons_bsk = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^bsk$"))
async def abot_cb_hangidler(bot, query):
    await query.message.edit(
        text=text_bsk,
        reply_markup=InlineKeyboardMarkup(buttons_bsk),
        disable_web_page_preview=True,
    )


text_ai = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Cʜᴀᴛ Ai:

々 /advice - ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ ʙʏ ʙᴏᴛ
々 /ai [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ᴄʜᴀᴛɢᴘᴛ's ᴀɪ
々 /gemini [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ɢᴇᴍɪɴɪ ᴀɪ
々 /bard [ǫᴜᴇʀʏ] -ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ʙᴀʀᴅ ᴀɪ
"""
buttons_ai = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^ai$"))
async def abot_cb_ughandler(bot, query):
    await query.message.edit(
        text=text_ai,
        reply_markup=InlineKeyboardMarkup(buttons_ai),
        disable_web_page_preview=True,
    )


text_dv = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Deᴠ:

🔰Aᴅᴅ Aɴᴅ Rᴇᴍᴏᴠᴇ Sᴜᴅᴏ Usᴇʀ's:
々 /addsudo [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ]
々 /delsudo [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ]

🤖Bᴏᴛ Cᴏᴍᴍᴀɴᴅs:
ⓘ /restart - Rᴇsᴛᴀʀᴛ ʏᴏᴜʀ Bᴏᴛ. 
ⓘ /update , /gitpull - Uᴘᴅᴀᴛᴇ Bᴏᴛ.
ⓘ /speedtest - Cʜᴇᴄᴋ sᴇʀᴠᴇʀ sᴘᴇᴇᴅs
ⓘ /maintenance [ᴇɴᴀʙʟᴇ / ᴅɪsᴀʙʟᴇ]
ⓘ /logger [ᴇɴᴀʙʟᴇ / ᴅɪsᴀʙʟᴇ] - Bᴏᴛ ʟᴏɢs ᴛʜᴇ sᴇᴀʀᴄʜᴇᴅ ǫᴜᴇʀɪᴇs ɪɴ ʟᴏɢɢᴇʀ ɢʀᴏᴜᴘ.
ⓘ /get_log [Nᴜᴍʙᴇʀ ᴏғ Lɪɴᴇs] - Gᴇᴛ ʟᴏɢ ᴏғ ʏᴏᴜʀ ʙᴏᴛ ғʀᴏᴍ ʜᴇʀᴏᴋᴜ ᴏʀ ᴠᴘs. Wᴏʀᴋs ғᴏʀ ʙᴏᴛʜ.
ⓘ /autoend [ᴇɴᴀʙʟᴇ|ᴅɪsᴀʙʟᴇ] - Eɴᴀʙʟᴇ Aᴜᴛᴏ sᴛʀᴇᴀᴍ ᴇɴᴅ ᴀғᴛᴇʀ 𝟹 ᴍɪɴs ɪғ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ.
"""
buttons_dv = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^dv$"))
async def abot_cb_handpcler(bot, query):
    await query.message.edit(
        text=text_dv,
        reply_markup=InlineKeyboardMarkup(buttons_dv),
        disable_web_page_preview=True,
    )


text_flt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Filters:

々 /filters To Get All The Filters In The Chat.
々 /filter [FILTER_NAME] To Save A Filter(reply to a message).

Supported filter types are Text, Animation, Photo, Document, Video, video notes, Audio, Voice.

To use more words in a filter use.
々 /filter Hey_there To filter "Hey there".

々 /stop [FILTER_NAME] To Stop A Filter.
々 /stopall To delete all the filters in a chat (permanently).

You can use markdown or html to save text too.

Checkout /markdownhelp to know more about formattings and other syntax.
"""
buttons_flt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^flt$"))
async def abot_cb_handlehcr(bot, query):
    await query.message.edit(
        text=text_flt,
        reply_markup=InlineKeyboardMarkup(buttons_flt),
        disable_web_page_preview=True,
    )


text_fgl = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Fɪɢʟᴇᴛ:

々 /figlet  - ᴄʀᴇᴀᴛᴇs ᴀ ғɪɢʟᴇᴛ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
"""
buttons_fgl = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^fgl$"))
async def abot_cb_handhjler(bot, query):
    await query.message.edit(
        text=text_fgl,
        reply_markup=InlineKeyboardMarkup(buttons_fgl),
        disable_web_page_preview=True,
    )


text_fk = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Fᴀᴋᴇ:

々 /fake [ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ ] - ᴛᴏ ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴅʀᴇss
"""
buttons_fk = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^fk$"))
async def abot_cb_handbiler(bot, query):
    await query.message.edit(
        text=text_fk,
        reply_markup=InlineKeyboardMarkup(buttons_fk),
        disable_web_page_preview=True,
    )


text_fon = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Fᴏɴᴛ:

々 /font [text] - ᴄᴏɴᴠᴇʀᴛs sɪᴍᴩʟᴇ ᴛᴇxᴛ ᴛᴏ ʙᴇᴀᴜᴛɪғᴜʟ ᴛᴇxᴛ ʙʏ ᴄʜᴀɴɢɪɴɢ ɪᴛ's ғᴏɴᴛ.
"""
buttons_fon = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^fon$"))
async def abot_cb_hanipdler(bot, query):
    await query.message.edit(
        text=text_fon,
        reply_markup=InlineKeyboardMarkup(buttons_fon),
        disable_web_page_preview=True,
    )


text_fn = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Fᴜɴ:

ʜᴀᴠɪɴɢ ꜰᴜɴ:
々 /dice: Rᴏʟʟs ᴀ ᴅɪᴄᴇ.
々 /ludo: Pʟᴀʏ Lᴜᴅᴏ.
々 /dart: Tʜʀᴏᴡs ᴀ ᴅᴀʀᴛ.
々 /basket ᴏʀ /basketball: Pʟᴀʏs ʙᴀsᴋᴇᴛʙᴀʟʟ.
々 /football: Pʟᴀʏs ғᴏᴏᴛʙᴀʟʟ.
々 /slot ᴏʀ /jackpot: Pʟᴀʏs ᴊᴀᴄᴋᴘᴏᴛ.
々 /bowling: Pʟᴀʏs ʙᴏᴡʟɪɴɢ.
々 /bored: Gᴇᴛs ʀᴀɴᴅᴏᴍ ᴀᴄᴛɪᴠɪᴛʏ ɪғ ʏᴏᴜ'ʀᴇ ʙᴏʀᴇᴅ.
"""
buttons_fn = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^fn$"))
async def abot_cb_handlsser(bot, query):
    await query.message.edit(
        text=text_fn,
        reply_markup=InlineKeyboardMarkup(buttons_fn),
        disable_web_page_preview=True,
    )


text_gt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ G-ᴄᴀsᴛ:

々 /broadcast [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ] » ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ᴍᴏᴅᴇs:

-pin » ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇs ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs.

-pinloud » ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴀɴᴅ sᴇɴᴅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴍᴇᴍʙᴇʀs.

-user » ʙʀᴏᴀᴅᴄᴀsᴛs ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʜᴇ ᴜsᴇʀs ᴡʜᴏ ʜᴀᴠᴇ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.

-assistant » ʙʀᴏᴀᴅᴄᴀsᴛ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴀssɪᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.

-nobot » ғᴏʀᴄᴇs ᴛʜᴇ ʙᴏᴛ ᴛᴏ ɴᴏᴛ ʙʀᴏᴀᴅᴄᴀsᴛ ᴛʜᴇ ᴍᴇssᴀɢᴇ.

ᴇxᴀᴍᴩʟᴇ: /broadcast -user -assistant -pin ᴛᴇsᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ
"""
buttons_gt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^gt$"))
async def abot_cb_handlpnner(bot, query):
    await query.message.edit(
        text=text_gt,
        reply_markup=InlineKeyboardMarkup(buttons_gt),
        disable_web_page_preview=True,
    )


text_gl = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Gʀᴏᴜᴘ Lɪɴᴋ:

々 /ɢɪᴠᴇɪɴᴋ: Gᴇᴛ ᴛʜᴇ ɪɴᴠɪᴛᴇ ɪɴᴋ ғᴏʀ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛ.
々 /ɪɴᴋ ɢʀᴏᴜᴘ_ɪᴅ: Gᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀɴᴅ ɢᴇɴᴇʀᴀᴛᴇ ᴀɴ ɪɴᴠɪᴛᴇ ɪɴᴋ ғᴏʀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ɢʀᴏᴜᴘ ID.
"""
buttons_gl = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^gl$"))
async def abot_cb_handllnver(bot, query):
    await query.message.edit(
        text=text_gl,
        reply_markup=InlineKeyboardMarkup(buttons_gl),
        disable_web_page_preview=True,
    )


text_gli = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Gᴀʟɪ:

Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʏ ғᴏʀ Pʀɪᴠᴀᴛᴇ ᴍᴇssᴀɢᴇ, Gᴏ Tᴏ Bᴏᴛ Pʀɪᴠᴀᴛᴇ Mᴇssᴀɢᴇ Aɴᴅ Tʏᴘᴇ /gai Cᴏᴍᴍᴀɴᴅ.

Fᴇᴀᴛᴜʀᴇs:
- Pʀᴏᴠɪᴅᴇs ʀᴀɴᴅᴏᴍ ᴀʙᴜsɪᴠᴇ ᴀɴɢᴜᴀɢᴇ (ɢᴀɪ) ᴡʜᴇɴ ᴜsᴇᴅ ɪɴ DMs.
- Dɪsᴘᴀʏs ᴀ ᴍᴇssᴀɢᴇ ɪɴᴅɪᴄᴀᴛɪɴɢ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʏ ғᴏʀ ᴘʀɪᴠᴀᴛᴇ ᴍᴇssᴀɢᴇs ᴡʜᴇɴ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs.

Cᴏᴍᴍᴀɴᴅ:
 /gai : Sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴀʙᴜsɪᴠᴇ ᴀɴɢᴜᴀɢᴇ (ɢᴀɪ) ᴡʜᴇɴ ᴜsᴇᴅ ɪɴ DMs.

Nᴏᴛᴇ: Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴛᴏ ᴘʀɪᴠᴀᴛᴇ ᴍᴇssᴀɢᴇs ᴏɴʏ ᴛᴏ ᴍᴀɪɴᴛᴀɪɴ ᴅᴇᴄᴏʀᴜᴍ ɪɴ ɢʀᴏᴜᴘ ᴄʜᴀᴛs.
"""
buttons_gli = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^gli$"))
async def abot_cb_handviler(bot, query):
    await query.message.edit(
        text=text_gli,
        reply_markup=InlineKeyboardMarkup(buttons_gli),
        disable_web_page_preview=True,
    )


text_src = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Gᴏᴏɢʟᴇ:
々 /google [ǫᴜᴇʀʏ] - ᴛᴏ sᴇᴀʀᴄʜ ᴏɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ɢᴇᴛ ʀᴇsᴜʟᴛs
々 /app | /apps [ᴀᴘᴘ ɴᴀᴍᴇ] - ᴛᴏ ɢᴇᴛ ᴀᴘᴘ ɪɴғᴏ ᴛʜᴀᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴘʟᴀʏsᴛᴏʀᴇ
"""
buttons_src = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^src$"))
async def abot_cb_handlevior(bot, query):
    await query.message.edit(
        text=text_src,
        reply_markup=InlineKeyboardMarkup(buttons_src),
        disable_web_page_preview=True,
    )


text_gdy = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Gᴏᴏᴅʙʏᴇ:

ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ɢᴏᴏᴅʙʏᴇ:
/setgoodbye - Rᴇᴘʟʏ ᴛʜɪs ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴄᴏɴᴛᴀɪɴɪɴɢ ᴄᴏʀʀᴇᴄᴛ
ғᴏʀᴍᴀᴛ ғᴏʀ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ, ᴄʜᴇᴄᴋ ᴇɴᴅ ᴏғ ᴛʜɪs ᴍᴇssᴀɢᴇ.
/goodbye - Tᴏ ɢᴇᴛ ʏᴏᴜʀ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ
/goodbye  [ᴏɴ, ʏ, ᴛʀᴜᴇ, ᴇɴᴀʙʟᴇ, ᴛ] - ᴛᴏ ᴛᴜʀɴ ᴏɴ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇs
/goodbye [ᴏғғ, ɴ, ғᴀʟsᴇ, ᴅɪsᴀʙʟᴇ, ғ, ɴᴏ] - ᴛᴏ ᴛᴜʀɴ ᴏғғ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇs
/delgoodbye ᴏʀ /deletegoodbye ᴛᴏ ᴅᴇʟᴛᴇ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴛᴜʀɴ ᴏғғ ɢᴏᴏᴅʙʏᴇ
SetoodBye ->

Tᴏ sᴇᴛ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ɢɪғ ᴀs ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ. Aᴅᴅ ʏᴏᴜʀ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ ᴀs ᴄᴀᴘᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴘʜᴏᴛᴏ ᴏʀ ɢɪғ. Tʜᴇ ᴄᴀᴘᴛɪᴏɴ ᴍᴜsᴇ ʙᴇ ɪɴ ᴛʜᴇ ғᴏʀᴍᴀᴛ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.
Fᴏʀ ᴛᴇxᴛ ɢᴏᴏᴅʙʏᴇ ᴍᴇssᴀɢᴇ Jᴜsᴛ sᴇɴᴅ ᴛʜᴇ ᴛᴇxᴛ. Tʜᴇɴ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ
Tʜᴇ ғᴏʀᴍᴀᴛ sʜᴏᴜʟᴅ ʙᴇ sᴏᴍᴇᴛʜɪɴɢ ʟɪᴋᴇ ʙᴇʟᴏᴡ.
Hɪ {NAME} [{ID}] Wᴇʟᴄᴏᴍᴇ ᴛᴏ {GROUPNAME}

~ Tʜɪs sᴇᴘᴀʀᴀᴛᴇʀ (~) sʜᴏᴜʟᴅ ʙᴇ ᴛʜᴇʀᴇ ʙᴇᴛᴡᴇᴇɴ ᴛᴇxᴛ ᴀɴᴅ ʙᴜᴛᴛᴏɴs, ʀᴇᴍᴏᴠᴇ ᴛʜɪs ᴄᴏᴍᴍᴇɴᴛ ᴀʟsᴏ

Button=[Dᴜᴄᴋ, ʜᴛᴛᴘs://ᴅᴜᴄᴋᴅᴜᴄᴋɢᴏ.ᴄᴏᴍ]
Button2=[Gɪᴛʜᴜʙ, ʜᴛᴛᴘs://ɢɪᴛʜᴜʙ.ᴄᴏᴍ]
NOTES ->

Cʜᴇᴄᴋᴏᴜᴛ /markdownhelp ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ғᴏʀᴍᴀᴛᴛɪɴɢs ᴀɴᴅ ᴏᴛʜᴇʀ sʏɴᴛᴀx.
"""
buttons_gdy = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^gdy$"))
async def abot_cb_handlesnr(bot, query):
    await query.message.edit(
        text=text_gdy,
        reply_markup=InlineKeyboardMarkup(buttons_gdy),
        disable_web_page_preview=True,
    )


text_hsr = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Hɪsᴛᴏʀʏ: 

1. /sg ᴏʀ /history 
Dᴇsᴄʀɪᴘᴛɪᴏɴ:
Fᴇᴛᴄʜᴇs ᴀ ʀᴀɴᴅᴏᴍ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ʜɪsᴛᴏʀʏ.

Usᴀɢᴇ:
々 /sg [ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ/ʀᴇᴘʏ]

Dᴇᴛᴀɪs:
- Fᴇᴛᴄʜᴇs ᴀ ʀᴀɴᴅᴏᴍ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇssᴀɢᴇ ʜɪsᴛᴏʀʏ ᴏғ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ᴜsᴇʀ.
- Cᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴘʀᴏᴠɪᴅɪɴɢ ᴀ ᴜsᴇʀɴᴀᴍᴇ, ᴜsᴇʀ ID, ᴏʀ ʀᴇᴘʏɪɴɢ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴜsᴇʀ.
- Aᴄᴄᴇssɪʙᴇ ᴏɴʏ ʙʏ ᴛʜᴇ ʙᴏᴛ's ᴀssɪsᴛᴀɴᴛs.

Exᴀᴍᴘᴇs:
- /sg ᴜsᴇʀɴᴀᴍᴇ
- /sg ᴜsᴇʀ_ɪᴅ
- /sg [ʀᴇᴘʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]
"""
buttons_hsr = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^hsr$"))
async def abot_cb_handihoer(bot, query):
    await query.message.edit(
        text=text_hsr,
        reply_markup=InlineKeyboardMarkup(buttons_hsr),
        disable_web_page_preview=True,
    )


text_htg = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Hᴀsʜᴛᴀɢ:

ʜᴀsʜᴛᴀɢ ɢᴇɴᴇʀᴀᴛᴏʀ:

々 /hashtag [text]: Gᴇɴᴇʀᴀᴛᴇ ʜᴀsʜᴛᴀɢs ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
"""
buttons_htg = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^htg$"))
async def abot_cb_handluvjker(bot, query):
    await query.message.edit(
        text=text_htg,
        reply_markup=InlineKeyboardMarkup(buttons_htg),
        disable_web_page_preview=True,
    )


text_hg = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Hᴜɢ:

Tʜɪs ʙᴏᴛ ʀᴇsᴘᴏɴᴅs ᴛᴏ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴄᴏᴍᴍᴀɴᴅs:
々 /hug: Sᴇɴᴅs ᴀ ʜᴜɢɢɪɴɢ ᴀɴɪᴍᴀᴛɪᴏɴ.

Cᴏᴍᴍᴀɴᴅs
々 /hug: Sᴇɴᴅs ᴀ ʜᴜɢɢɪɴɢ ᴀɴɪᴍᴀᴛɪᴏɴ. Iғ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴍᴇssᴀɢᴇ, ɪᴛ ᴍᴇɴᴛɪᴏɴs ᴛʜᴇ sᴇɴᴅᴇʀ ᴀɴᴅ ʀᴇᴄɪᴘɪᴇɴᴛ ᴏғ ᴛʜᴇ ʜᴜɢ.

Hᴏᴡ ᴛᴏ Usᴇ

- Usᴇ /hug ᴛᴏ sᴇɴᴅ ᴀ ʜᴜɢɢɪɴɢ ᴀɴɪᴍᴀᴛɪᴏɴ.
- Rᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ /ʜᴜ ᴛᴏ sᴇɴᴅ ᴀ ʜᴜɢɢɪɴɢ ᴀɴɪᴍᴀᴛɪᴏɴ ᴍᴇɴᴛɪᴏɴɪɴɢ ᴛʜᴇ sᴇɴᴅᴇʀ ᴀɴᴅ ʀᴇᴄɪᴘɪᴇɴᴛ.

Nᴏᴛᴇs

- Eɴsᴜʀᴇ ʏᴏᴜʀ ᴄʜᴀᴛ sᴇᴛᴛɪɴɢs ᴀʟʟᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴛᴏ sᴇɴᴅ ᴠɪᴅᴇᴏs/sᴛɪᴄᴋᴇʀs ᴀs ʀᴇᴘʟɪᴇs ғᴏʀ ғᴜʟʟ ғᴜɴᴄᴛɪᴏɴᴀʟɪᴛʏ.
"""
buttons_hg = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^hg$"))
async def abot_cb_hvivandler(bot, query):
    await query.message.edit(
        text=text_hg,
        reply_markup=InlineKeyboardMarkup(buttons_hg),
        disable_web_page_preview=True,
    )


text_lv = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Lᴏᴠᴇ:

ʟᴏᴠᴇ ᴄᴀʟᴄᴜʟᴀᴛᴏʀ:
々 /love [name1] [name2]: Cᴀʟᴄᴜʟᴀᴛᴇs ᴛʜᴇ ᴘᴇʀᴄᴇɴᴛᴀɢᴇ ᴏғ ʟᴏᴠᴇ ʙᴇᴛᴡᴇᴇɴ ᴛᴡᴏ ᴘᴇᴏᴘʟᴇ.
"""
buttons_lv = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^lv$"))
async def abot_cb_handlstver(bot, query):
    await query.message.edit(
        text=text_lv,
        reply_markup=InlineKeyboardMarkup(buttons_lv),
        disable_web_page_preview=True,
    )


text_mt = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mᴀᴛʜ:

1. /ᴍᴀᴛʜ [ᴇxᴘʀᴇssɪᴏɴ]
Dᴇsᴄʀɪᴘᴛɪᴏɴ:
Cᴀᴄᴜᴀᴛᴇs ᴛʜᴇ ʀᴇsᴜᴛ ᴏғ ᴀ ᴍᴀᴛʜᴇᴍᴀᴛɪᴄᴀ ᴇxᴘʀᴇssɪᴏɴ.

Usᴀɢᴇ:
/ᴍᴀᴛʜ [ᴇxᴘʀᴇssɪᴏɴ]

Dᴇᴛᴀɪs:
- Sᴜᴘᴘᴏʀᴛs ʙᴀsɪᴄ ᴀʀɪᴛʜᴍᴇᴛɪᴄ ᴏᴘᴇʀᴀᴛɪᴏɴs: ᴀᴅᴅɪᴛɪᴏɴ (+), sᴜʙᴛʀᴀᴄᴛɪᴏɴ (-), ᴍᴜᴛɪᴘɪᴄᴀᴛɪᴏɴ (*), ᴀɴᴅ ᴅɪᴠɪsɪᴏɴ (/).
- Rᴇᴛᴜʀɴs ᴛʜᴇ ʀᴇsᴜᴛ ᴏғ ᴛʜᴇ ᴇxᴘʀᴇssɪᴏɴ.
- Dɪsᴘᴀʏs "Iɴᴠᴀɪᴅ ᴇxᴘʀᴇssɪᴏɴ" ɪғ ᴛʜᴇ ᴇxᴘʀᴇssɪᴏɴ ɪs ɴᴏᴛ ᴠᴀɪᴅ.

Gᴏᴏɢᴇ Sᴇᴀʀᴄʜ Cᴏᴍᴍᴀɴᴅ Hᴇᴘ

1. /sᴘɢ [ǫᴜᴇʀʏ]
Dᴇsᴄʀɪᴘᴛɪᴏɴ:
Sᴇᴀʀᴄʜᴇs Gᴏᴏɢᴇ ᴀɴᴅ ᴅɪsᴘᴀʏs sᴇᴀʀᴄʜ ʀᴇsᴜᴛs.

Usᴀɢᴇ:
/sᴘɢ [ǫᴜᴇʀʏ]

Dᴇᴛᴀɪs:
- Sᴇᴀʀᴄʜᴇs Gᴏᴏɢᴇ ғᴏʀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ǫᴜᴇʀʏ.
- Dɪsᴘᴀʏs sᴇᴀʀᴄʜ ʀᴇsᴜᴛs ᴡɪᴛʜ ᴛɪᴛᴇs ᴀɴᴅ ɪɴᴋs.
- Sᴜᴘᴘᴏʀᴛs ᴘᴀɢɪɴᴀᴛɪᴏɴ ᴡɪᴛʜ ɴᴇxᴛ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴠɪᴇᴡ ᴍᴏʀᴇ ʀᴇsᴜᴛs.
"""
buttons_mt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^mt$"))
async def abot_cb_handvippler(bot, query):
    await query.message.edit(
        text=text_mt,
        reply_markup=InlineKeyboardMarkup(buttons_mt),
        disable_web_page_preview=True,
    )


text_mog = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mᴏɴɢᴏᴅʙ:

ᴍᴏɴɢᴏᴅʙ ᴄʜᴇᴄᴋᴇʀ:
々 /mongochk [mongo_url]: Cʜᴇᴄᴋs ᴛʜᴇ ᴠᴀʟɪᴅɪᴛʏ ᴏғ ᴀ ᴍᴏɴɢᴏᴅʙ URL ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴍᴏɴɢᴏᴅʙ ɪɴsᴛᴀɴᴄᴇ.
"""
buttons_mog = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^mog$"))
async def abot_cb_hajjvvindler(bot, query):
    await query.message.edit(
        text=text_mog,
        reply_markup=InlineKeyboardMarkup(buttons_mog),
        disable_web_page_preview=True,
    )


text_not = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Nᴏᴛᴇs:

ɴᴏᴛᴇꜱ:
々 /save [NOTE_NAME] [CONTENT]: Sᴀᴠᴇs ᴀ ɴᴏᴛᴇ ᴡɪᴛʜ ᴛʜᴇ ɢɪᴠᴇɴ ɴᴀᴍᴇ ᴀɴᴅ ᴄᴏɴᴛᴇɴᴛ.
々 /notes: Sʜᴏᴡs ᴀʟʟ sᴀᴠᴇᴅ ɴᴏᴛᴇꜱ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.
々 /get [NOTE_NAME]: Gᴇᴛs ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴏғ ᴀ sᴀᴠᴇᴅ ɴᴏᴛᴇ.
々 /delete [NOTE_NAME]: Dᴇʟᴇᴛᴇs ᴀ sᴀᴠᴇᴅ ɴᴏᴛᴇ.
々 /deleteall: Dᴇʟᴇᴛᴇs ᴀʟʟ sᴀᴠᴇᴅ ɴᴏᴛᴇꜱ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.
"""
buttons_not = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^not$"))
async def abot_cb_hanbkodler(bot, query):
    await query.message.edit(
        text=text_not,
        reply_markup=InlineKeyboardMarkup(buttons_not),
        disable_web_page_preview=True,
    )


text_ps = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Pᴀᴜsᴇ:

Pause Music

This module allows administrators to pause the music playback in the group.

Commands:
- /pause: Pause the music playback in groups.
- /cpause: Pause the music playback in channels.

Note:
- Only administrators can use these commands.
"""
buttons_ps = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^ps$"))
async def abot_cb_handguugler(bot, query):
    await query.message.edit(
        text=text_ps,
        reply_markup=InlineKeyboardMarkup(buttons_ps),
        disable_web_page_preview=True,
    )


text_ply = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Plᴀʏ:

★ ᴘʟᴀʏ , ᴠᴘʟᴀʏ , ᴄᴘʟᴀʏ - Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs
★ ᴘʟᴀʏғᴏʀᴄᴇ , ᴠᴘʟᴀʏғᴏʀᴄᴇ , ᴄᴘʟᴀʏғᴏʀᴄᴇ - FᴏʀᴄᴇPʟᴀʏ Cᴏᴍᴍᴀɴᴅs

- c sᴛᴀɴᴅs ғᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ.
- v sᴛᴀɴᴅs ғᴏʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏ.
- force sᴛᴀɴᴅs ғᴏʀ ғᴏʀᴄᴇ ᴘʟᴀʏ.

々 /play ᴏʀ /vplay ᴏʀ /cplay - Bᴏᴛ ᴡɪʟʟ sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ʏᴏᴜʀ ɢɪᴠᴇɴ ǫᴜᴇʀʏ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴏʀ Sᴛʀᴇᴀᴍ ʟɪᴠᴇ ʟɪɴᴋs ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs.

々 /playforce ᴏʀ /vplayforce ᴏʀ /cplayforce - Fᴏʀᴄᴇ Pʟᴀʏ sᴛᴏᴘs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀɴᴅ sᴛᴀʀᴛs ᴘʟᴀʏɪɴɢ ᴛʜᴇ sᴇᴀʀᴄʜᴇᴅ ᴛʀᴀᴄᴋ ɪɴsᴛᴀɴᴛʟʏ ᴡɪᴛʜᴏᴜᴛ ᴅɪsᴛᴜʀʙɪɴɢ/ᴄʟᴇᴀʀɪɴɢ ǫᴜᴇᴜᴇ.

々 /channelplay [Cʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ] ᴏʀ [Dɪsᴀʙʟᴇ] - Cᴏɴɴᴇᴄᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀ ɢʀᴏᴜᴘ ᴀɴᴅ sᴛʀᴇᴀᴍ ᴍᴜsɪᴄ ᴏɴ ᴄʜᴀɴɴᴇʟ's ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
"""
buttons_ply = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^ply$"))
async def abot_cb_haydyriindler(bot, query):
    await query.message.edit(
        text=text_ply,
        reply_markup=InlineKeyboardMarkup(buttons_ply),
        disable_web_page_preview=True,
    )


text_sg = """
Hᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ SᴀɴɢMᴀᴛᴀ:

Tʜɪs ғᴇᴀᴛᴜʀᴇ ɪɴsᴘɪʀᴇᴅ ғʀᴏᴍ SᴀɴɢMᴀᴛᴀ Bᴏᴛ. I'ᴍ ᴄʀᴇᴀᴛᴇᴅ sɪᴍᴘʟᴇ ᴅᴇᴛᴇᴄᴛɪᴏɴ ᴛᴏ ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴅᴀᴛᴀ ɪɴᴄʟᴜᴅᴇ ᴜsᴇʀɴᴀᴍᴇ, ғɪʀsᴛ_ɴᴀᴍᴇ, ᴀɴᴅ ʟᴀsᴛ_ɴᴀᴍᴇ.
々 /sangmata_set [ᴏɴ/ᴏғғ] - Eɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ sᴀɴɢᴍᴀᴛᴀ ɪɴ ɢʀᴏᴜᴘs.
"""
buttons_sg = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^sg$"))
async def abot_cb_handhigler(bot, query):
    await query.message.edit(
        text=text_sg,
        reply_markup=InlineKeyboardMarkup(buttons_sg),
        disable_web_page_preview=True,
    )


text_pyp = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Pʏᴘɪ:

ᴄᴏᴍᴍᴀɴᴅs:
々 /pypi : Get details about a specified Python package from PyPI.

**ɪɴғᴏ:**
ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴀʟʟᴏᴡs ᴜsᴇʀs ᴛᴏ ғᴇᴛᴄʜ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴘʏᴛʜᴏɴ ᴘᴀᴄᴋᴀɢᴇs ғʀᴏᴍ ᴘʏᴘɪ, ɪɴᴄʟᴜᴅɪɴɢ ᴛʜᴇ ᴘᴀᴄᴋᴀɢᴇ ɴᴀᴍᴇ, ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ, ᴅᴇsᴄʀɪᴘᴛɪᴏɴ, ᴀɴᴅ ᴘʀᴏᴊᴇᴄᴛ ᴜʀʟ.

**ɴᴏᴛᴇ:**
ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ᴘᴀᴄᴋᴀɢᴇ ɴᴀᴍᴇ ᴀғᴛᴇʀ ᴛʜᴇ /pypi ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʀᴇᴛʀɪᴇᴠᴇ ᴘᴀᴄᴋᴀɢᴇ ᴅᴇᴛᴀɪʟs.
"""
buttons_pyp = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^pyp$"))
async def abot_cb_hgugandler(bot, query):
    await query.message.edit(
        text=text_pyp,
        reply_markup=InlineKeyboardMarkup(buttons_pyp),
        disable_web_page_preview=True,
    )


text_pay = """
PʟᴀʏʟɪsᴛHᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Pʟᴀʏʟɪsᴛ:

Pʟᴀʏʟɪsᴛ Fᴇᴀᴛᴜʀᴇ Fᴏʀ ʏᴏᴜ.
々 /payist » sʜᴏᴡ ʏᴏᴜʀ ᴘʟᴀʏʟɪsᴛ
々 /addpayist » [sᴏɴɢ ɴᴀᴍᴇ , sᴏɴɢ ʟɪɴᴋ, ʏᴏᴜᴛᴜʙᴇ ᴘʟᴀʏʟɪsᴛ ʟɪɴᴋ]
々 /drpayist » ᴅᴇʟᴇᴛᴇ ᴀɴʏ sᴏɴɢ ɪɴ ʏᴏᴜʀ ᴘʟᴀʏʟɪsᴛ.
々 /deeteapayist » ᴅᴇʟᴇᴛᴇ ᴀʟʟ sᴏɴɢ ɪɴ ʏᴏᴜʀ ᴘʟᴀʏʟɪsᴛ.
々 /paypayist » ᴘʟᴀʏ ʏᴏᴜʀ ᴘʟᴀʏʟɪsᴛ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪɴ ᴀᴜᴅɪᴏ.
々 /vpaypayist  » ᴘʟᴀʏ ʏᴏᴜʀ ᴘʟᴀʏʟɪsᴛ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪɴ ᴠɪᴅᴇᴏ.
"""
buttons_pay = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^pay$"))
async def abot_cb_hanibibbdler(bot, query):
    await query.message.edit(
        text=text_pay,
        reply_markup=InlineKeyboardMarkup(buttons_pay),
        disable_web_page_preview=True,
    )


text_qr = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Qʀɢᴇɴ:

Ƭʜɪs ᴍᴏᴅᴜʟᴇ ɢᴇɴᴇʀᴀᴛᴇs Qʀ ᴄᴏᴅᴇs. Usᴇ ᴛʜᴇ /qr ᴄᴏᴍᴍᴀɴᴅ ғᴏʟʟᴏᴡᴇᴅ ʙʏ ᴛʜᴇ ᴛᴇxᴛ ᴏʀ URL ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴇɴᴄᴏᴅᴇ ɪɴᴛᴏ ᴀ Qʀ ᴄᴏᴅᴇ. Fᴏʀ ᴇxᴀᴍᴘʟᴇ, /qr https://t.me/vivekkumar07089. Tʜᴇ ʙᴏᴛ ᴡɪʟʟ ᴛʜᴇɴ ɢᴇɴᴇʀᴀᴛᴇ ᴀ Qʀ ᴄᴏᴅᴇ ғᴏʀ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ɪɴᴘᴜᴛ. Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ɪɴᴄʟᴜᴅᴇ ᴛʜᴇ ᴘʀᴏᴛᴏᴄᴏʟ (http:// ᴏʀ https://) ғᴏʀ URLs. Eɴᴊᴏʏ ᴄʀᴇᴀᴛɪɴɢ Qʀ ᴄᴏᴅᴇs ᴡɪᴛʜ ᴇᴀsᴇ!
"""
buttons_qr = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^qr$"))
async def abot_cb_habibjndler(bot, query):
    await query.message.edit(
        text=text_qr,
        reply_markup=InlineKeyboardMarkup(buttons_qr),
        disable_web_page_preview=True,
    )


text_qz = """
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Qᴜɪᴢ:

々 /quiz - ᴛᴏ ɢᴇᴛ ᴀɴ ʀᴀɴᴅᴏᴍ ǫᴜɪᴢ
"""
buttons_qz = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^qz$"))
async def abot_cb_hanbibondler(bot, query):
    await query.message.edit(
        text=text_qz,
        reply_markup=InlineKeyboardMarkup(buttons_qz),
        disable_web_page_preview=True,
    )


# =============================================================
# =============================================================


# ==============CLOSE===================
@Bot.on_callback_query(filters.regex("^close2$"))
async def close_cb(bot, callback):
    await callback.answer("❌Closed the Module❌")
    await callback.message.delete()
    await callback.message.reply_to_message.delete()
