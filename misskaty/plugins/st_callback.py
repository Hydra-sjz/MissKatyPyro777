from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

from misskaty import app as Bot, BOT_USERNAME, BOT_NAME, BOT_ID
from misskaty.vars import SUDO as SUDO_USERS

#============SUDO===≠===
SUDO_TEXT = """
**Sudo User CMD**👮‍♂️
Here is the help for DevCommand:

**For Owner Bot Only:**
<blockquote>/restart - update and restart bot.
/run [args] - Run eval CMD
/logs [int] - Check logs bot
/shell [args] - Run Exec/Terminal CMD
**Blacklist chat:**
/disablechat [chat id] - Remove blacklist group
/enablechat [chat id] - Add Blacklist group
/leave</blockquote>

**BanUsers:**
<blockquote>/banuser [chat id] - Ban user and block user so cannot use bot
/unbanuser [chat id] - Unban user and make their can use bot again
/gban - To Ban A User Globally.
/ungban - To remove ban user globbaly.
/copy | /forward To send message to groups.</blockquote>

**Blacklist Groups**
<blockquote>/blacklist_chat [CHAT_ID] - Blacklist a chat.
/whitelist_chat [CHAT_ID] - Whitelist a chat.
/blacklisted - Show blacklisted chats.</blockquote>

**For Public Use**
<blockquote>/stats - Check statistic bot
/json - Send structure message Telegram in JSON using Pyrogram Style.</blockquote>
"""
BUTTON_SUDO = [
    [
        InlineKeyboardButton("❮ Back ❮", callback_data="set_ge"),
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
    "[👋](https://telegra.ph/file/f04e33ed9774304630ab7.jpg)**__Hello there {},__**\n\n"
    "<blockquote>Welcome to the 🎈{}! This is a powerful group management bot⚡🌪️ for Telegram, I have 😌 many useful features for you, feel free to ➕add me to your group.</blockquote>\n\n"
    "**__Click /help to find out more about how to use me to me full potential!__**"
)
BUTTONS_ST = [
    [
        InlineKeyboardButton("➕Add Me To Your Group!", url=f"http://t.me/{BOT_USERNAME}?startgroup=new",),
        ],[
        InlineKeyboardButton("⚙️ Help", callback_data="set_ge"),
        InlineKeyboardButton("📊 Status", callback_data="stats_callback"),
        InlineKeyboardButton("🤖 About", callback_data="abt"),
        ],[
        InlineKeyboardButton("📢 Channel", url="https://t.me/XBOTS_X"),
        InlineKeyboardButton("🪅 Stickers", url="https://t.me/stickers_collections_X"),
    ],
]

@Bot.on_callback_query(filters.regex("^home$"))
async def st_cb_handler(bot, query):
    await query.message.edit(
        text=TEXT_ST.format(query.from_user.first_name, BOT_NAME),
        reply_markup=InlineKeyboardMarkup(BUTTONS_ST),
        disable_web_page_preview=True,
    )

text_abt = """
**My About ;)**
 
<blockquote>🤖 **My Name:** {}
🆔 **My ID:** {}
©️ **My Username:** @{}</blockquote>

<blockquote>📝 **Language:** Python3
• **Python version:** 3.12.11
📚 **Library:** Pyrogram
• **Pyrogram version:** 2.0.73
📡 **Hosted On:** Digital Ocean 🌊
📋 **License:** MIT</blockquote>

<blockquote>__Hey {}, my name is ⏤͟͟͞͞𝐺𝑜𝑗𝑜 𝑆𝑎𝑡𝑜𝑟𝑢 𝕏 | 𝐵𝑜𝑡𓆪.
I'm a group management bot made to help you automate your group as much as possible by welcoming users, warning bad behaviour, and banning if necessary.
Use the /privacy command to view the privacy policy, and interact with your data.__</blockquote>
"""
button_abt = [
    [
        InlineKeyboardButton("⬅️", callback_data="home")
    ]
]

@Bot.on_callback_query(filters.regex("^abt$"))
async def st_cb_handler(bot, query):
    await query.message.edit(
        text=text_abt.format(BOT_NAME, BOT_ID, BOT_USERNAME, query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(button_abt),
        disable_web_page_preview=True,
    )



# =======================f=======MAIN_HELP_CMD====================
TEXT_GE = """
Hey {} [👋](https://telegra.ph/file/cadfaa11fcc628b2ac385.jpg)
<blockquote>Click on the Buttons below for more information.</blockquote>
"""
BUTTONS_GE = [
    [
        InlineKeyboardButton("👮‍♂️ Group-CMD", callback_data="group"),
        InlineKeyboardButton("➕ Extra-CMD", callback_data="settings"),
    ],
    [
        InlineKeyboardButton("👥 Only for Sudo Users!", callback_data="sudo"),
    ],
    [
        InlineKeyboardButton("⬅️", callback_data="home")
    ],
]
@Bot.on_callback_query(filters.regex("^set_ge$"))
async def help_cb_handlerj1(bot, query):
    await query.message.edit(
        text=TEXT_GE.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_GE),
        disable_web_page_preview=True,
    )
@Bot.on_message(filters.command("help") & filters.private)
async def hp_hagndlery(bot, query):
    await query.reply_text(
        text=TEXT_GE.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_GE),
        quote=True,
    )
   
#================GROUP_CMD=================
TEXT_GP = """
**Group-CMD**
<blockquote>Hey {}, My name is ⏤͟͟͞͞𝐺𝑜𝑗𝑜 𝑆𝑎𝑡𝑜𝑟𝑢 𝕏 | 𝐵𝑜𝑡𓆪. I am a group management bot, here to help you get around and keep the order in your groups!
I have lots of handy features, such as flood control, a warning system, a note keeping system, and even predetermined replies on certain keywords.</blockquote>

**Helpful commands:**
<blockquote> - /start: Start the bot
 - /help: Give this message
 - /privacy if you want know data collected by this bot.</blockquote>

** All commands can be used with the following: / !**
"""
BUTTONS_GP = [
    [
        InlineKeyboardButton("👮Admin", callback_data="admi"),
        InlineKeyboardButton("💤Afk", callback_data="afk"),
    ],
    [
        InlineKeyboardButton("☣️Anti-Flood", callback_data="adf"),
        InlineKeyboardButton("🚧Anti-Channel", callback_data="adc"),
    ],
    [
        InlineKeyboardButton("🚪Auto-Approve", callback_data="aap"),
        InlineKeyboardButton("👾Anti-Raid", callback_data="ard"),
    ],
    [
        InlineKeyboardButton("🚯Bans", callback_data="ban"),
        InlineKeyboardButton("⚖️Blacklist", callback_data="bal"),
    ],
    [
        InlineKeyboardButton("🎂Birthday", callback_data="brt"),
        InlineKeyboardButton("🧹Clean-CMD", callback_data="ccd"),
    ],
    [
        InlineKeyboardButton("🚨Federation", callback_data="fed"),
        InlineKeyboardButton("📄Filters", callback_data="filter"),
    ],
    [
        InlineKeyboardButton("🧟Ghost", callback_data="gst"),
        InlineKeyboardButton("🔐Locks", callback_data="lok"),
    ],
    [
        InlineKeyboardButton("📣Mention-all", callback_data="mall"),
        InlineKeyboardButton("🌃Night-Mod", callback_data="nm"),
    ],
    [
        InlineKeyboardButton("📝Notes", callback_data="not"),
        InlineKeyboardButton("🚮Purges", callback_data="prg"),
    ],
    [
        InlineKeyboardButton("📌Pin", callback_data="pn"),
        InlineKeyboardButton("🗳️Reports", callback_data="rpt"),
    ],
    [
        InlineKeyboardButton("📊Ranking", callback_data="rak"),
        InlineKeyboardButton("🪬SangMata", callback_data="sm"),
    ],
    [
        InlineKeyboardButton("❗Warns", callback_data="war"),
        InlineKeyboardButton("🔦Fsub", callback_data="fsb"),
    ],
    [
        InlineKeyboardButton("⬅️", callback_data="set_ge"),
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


text_fsb = """
<blockquote>Dazai has the capability to hush members who haven't yet subscribed to your channel until they decide to hit that subscribe button.
When activated, I'll silence those who are not subscribed and provide them with an option to unmute. Once they click the button, I'll lift the mute.</blockquote>

<blockquote>Configuration Process
Exclusively for Creators
Grant me admin privileges in your group
Designate me as an admin in your channel</blockquote>

**Commands**
<blockquote>/fsub channel\_username - to initiate and customize settings for the channel.</blockquote>

**Kick things off with...**
<blockquote>/fsub - to review the current settings.
/fsub off - to deactivate the force subscription feature.</blockquote>
"""
buttons_fsb = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
    ]
]


@Bot.on_callback_query(filters.regex("^fsb$"))
async def abvifsv(bot, query):
    await query.message.edit(
        text=text_fsb,
        reply_markup=InlineKeyboardMarkup(buttons_fsb),
        disable_web_page_preview=True,
    )


text_rak = """
**Rankings**

<blockquote>Emilia now provides a more interactive and playful environment for group chats!
You can now enjoy our new chat levels module to increase your points and level up in a specific group chat. All you need to do is register yourself for unlocking new adventures!</blockquote>

**Commands:**
<blockquote>/register [your_name]: This is a one time command for users to register themselves to play chat levels.
/rank: This will show your rankings and stats.
/leaderboard: Shows current leaderboard among top players.
/daily: Use it once in every 24 hours to get a 100 points gift.
/weekly: Use it once in every 7 days to get a 500 points gift.
/rankings: To know more about chat levels.</blockquote>
"""
buttons_rak = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
    ]
]


@Bot.on_callback_query(filters.regex("^rak$"))
async def abvivrak(bot, query):
    await query.message.edit(
        text=text_rak,
        reply_markup=InlineKeyboardMarkup(buttons_rak),
        disable_web_page_preview=True,
    )

text_ard = """
**AntiRaid**

<blockquote>Some people on telegram find it entertaining to **raid** chats. During a raid, hundreds of users join a chat to spam.
The antiraid module allows you to quickly stop anyone from joining when such a raid is happening.
All new joins will be temporarily banned for the next few hours, allowing you to wait out the spam attack until the trolls stop.</blockquote>

**Admin commands:**
<blockquote>__/antiraid Toggle antiraid. All new joins will be temporarily banned for the next few hours.
/raidtime <time>: View or set the desired antiraid duration. Default 6h.
/raidactiontime <time>: View or set the time for antiraid to tempban users for. Default 1h.
/autoantiraid <number/off/no>: Set the number of joins per minute after which to enable automatic antiraid. Set to '0', 'off', or 'no' to disable.__</blockquote>
"""
buttons_ard = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
    ]
]


@Bot.on_callback_query(filters.regex("^ard$"))
async def abvrriv(bot, query):
    await query.message.edit(
        text=text_ard,
        reply_markup=InlineKeyboardMarkup(buttons_ard),
        disable_web_page_preview=True,
    )


text_ccd = """
**Clean Command**

<blockquote>/cleanblue - Enable clean Blue texts in group chats.</blockquote>
"""
buttons_ccd = [
    [
        InlineKeyboardButton("⬅️", callback_data="group")
    ]
]


@Bot.on_callback_query(filters.regex("^ccd$"))
async def abviv(bot, query):
    await query.message.edit(
        text=text_ccd,
        reply_markup=InlineKeyboardMarkup(buttons_ccd),
        disable_web_page_preview=True,
    )

text_admi = """
**Here is the help for Admin**
<blockquote>Make it easy to promote and demote users with the admin module!</blockquote>

**Admin commands:**
<blockquote>/adminlist: List the admins in the current chat.
/promote <reply/username/mention/userid>: Promote a user.
/demote <reply/username/mention/userid>: Demote a user.
/fullpromote Promote A Member With All Rights.
/groupdata To get Group Data.
/groupinfo To get Group info.
/link To get Group link.</blockquote>

**To Admins.**
<blockquote>/set_chat_title - Change The Name Of A Group/Channel.
/set_chat_photo - Change The PFP Of A Group/Channel.
/set_user_title - Change The Administrator Title Of An Admin.</blockquote>

<blockquote>Sometimes, you promote or demote an admin manually, and gojo doesn't realise it immediately.
This is because to avoid spamming telegram servers, admin status is cached locally.</blockquote>
"""
buttons_admi = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>/afk [Reason > Optional] - Tell others that you are AFK (Away From Keyboard), so that your boyfriend or girlfriend won't look for you 💔.
/afk [reply to media] - AFK with media.
/afkdel - Enable auto delete AFK message in group (Only for group admin). Default is Enable.</blockquote>

<blockquote>Just type something in group to remove AFK Status.</blockquote>
"""
buttons_afk = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>Some people need to be publicly banned; spammers, annoyances, or just trolls.
This module allows you to do that easily, by exposing some common actions, so everyone will see!</blockquote>

**User commands:**
<blockquote>/kickme: Users that use this, kick themselves.</blockquote>

**Admin commands:**
**Ban**
<blockquote>/ban - Ban A User From A Group
/dban - Delete the replied message banning its sender
/tban - Ban A User For Specific Time
/unban - Unban A User
/listban - Ban a user from groups listed in a message
/listunban - Unban a user from groups listed in a message</blockquote>

**Mute:**
<blockquote>/mute: Mute a user.
/tmute: Temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
/unmute: Unmute a user.</blockquote>

**Kick**
<blockquote>/kick: Kick a user.
/dkick - Delete the replied message kicking its sender</blockquote>
"""
buttons_ban = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>Keep your members in check with warnings; stop them getting out of control!</blockquote>

<blockquote>/warn <reason>: - Warn A User
/dwarn <reason>: - Delete the replied message warning its sender
/rmwarns - Remove All Warning of A User
/warns - Show Warning Of A User.</blockquote>

<blockquote>Keep your members in check with warnings; stop them getting out of control!
If you're looking for automated warnings, go read about the blocklist module.</blockquote>
"""
buttons_war = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>Need to delete lots of messages? That's what purges are for!</blockquote>

<blockquote>/purge - Delete all messages from the replied to message, to the current message.
/purge [n] - Purge "n" number of messages from replied message
/del - Delete Replied Message</blockquote>
<blockquote>
**Examples:**
- Delete all messages from the replied to message, until now.
---> /purge</blockquote>
"""
buttons_prg = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>/instatus - View member status in group
/ban_ghosts Remove deleted Ghosts accounts from group</blockquote>

<blockquote>note:
- ᴜsᴇ ᴅɪʀᴇᴄᴛʟʏ ɪɴ ᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍᴇ ғᴏʀ ʙᴇsᴛ ᴇғғᴇᴄᴛ. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.</blockquote>
"""
buttons_gst = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>We're all busy people who don't have time to monitor our groups 24/7. But how do you react if someone in your group is spamming?
Presenting reports; if someone in your group thinks someone needs reporting, they now have an easy way to call all admins.</blockquote>

<blockquote>/report | @admins | @admin - Report A Message To Admins.
- /report: Reply to a message to report it for admins to review.
- admin: Same as /report</blockquote>

<blockquote>Note that the report commands do not work when admins use them; or when used to report an admin. 𝐺𝑜𝑗𝑜 𝑆𝑎𝑡𝑜𝑟𝑢 𝕏 | 𝐵𝑜𝑡 assumes that admins don't need to report, or be reported!</blockquote>
"""
buttons_rpt = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>/mentionall - Mention all members in a groups in one click.</blockquote>
"""
buttons_mal = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>/autoapprove just type in group.</blockquote>

<blockquote>This module helps to automatically accept chat join request send by a user through invitation link of your group.</blockquote>
"""
buttons_aap = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>Want to stop people asking stupid questions? or ban anyone saying censored words? Blocklists is the module for you!
From blocking rude words, filenames/extensions, to specific emoji, everything is possible.</blockquote>

<blockquote>/blacklisted - Get All The Blacklisted Words In The Chat.
/blacklist [WORD|SENTENCE] - Blacklist A Word Or A Sentence.
/whitelist [WORD|SENTENCE] - Whitelist A Word Or A Sentence.</blockquote>
"""
buttons_bal = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>Everything is fun, until a spammer starts entering your group, and you have to block it. Then you need to start banning more, and more, and it hurts.
But then you have many groups, and you don't want this spammer to be in one of your groups - how can you deal? Do you have to manually block it, in all your groups?

No longer! With Federation, you can make a ban in one chat overlap with all other chats.

You can even designate federation admins, so your trusted admin can ban all the spammers from chats you want to protect.</blockquote>
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

<blockquote>These are the list of available fed owner commands. To run these, you have to own the current federation.</blockquote>

**Owner Commands:**
<blockquote>/newfed <fed_name>: Creates a Federation, One allowed per user
/renamefed <fed_id> <new_fed_name>: Renames the fed id to a new name
/delfed <fed_id>: Delete a Federation, and any information related to it. Will not cancel blocked users
/myfeds: To list the federations that you have created
/fedtransfer <new_owner> <fed_id>:To transfer fed ownership to another person
/fpromote <user>: Assigns the user as a federation admin. Enables all commands for the user under Fed Admins
/fdemote <user>: Drops the User from the admin Federation to a normal User
/setfedlog <fed_id>: Sets the group as a fed log report base for the federation
/unsetfedlog <fed_id>: Removed the group as a fed log report base for the federation
/fbroadcast : Broadcasts a messages to all groups that have joined your fed</blockquote>
"""
buttons_fdo = [
    [
        InlineKeyboardButton("⬅️", callback_data="fed"),
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

<blockquote>The following is the list of all fed admin commands. To run these, you have to be a federation admin in the current federation.</blockquote>

<blockquote>/fban <user> <reason>: Fed bans a user
/sfban: Fban a user without sending notification to chats
/unfban <user> <reason>: Removes a user from a fed ban
/sunfban: Unfban a user without sending a notification
/fedadmins: Show Federation admin
/fedchats <FedID>: Get all the chats that are connected in the Federation
/fbroadcast : Broadcasts a messages to all groups that have joined your fed</blockquote>
"""
buttons_fdm = [
    [
        InlineKeyboardButton("⬅️", callback_data="fed"),
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

<blockquote>These commands do not require you to be admin of a federation. These commands are for general commands, such as looking up information on a fed, or checking a user's fbans.</blockquote>

<blockquote>/fedinfo <FedID>: Information about a federation.
/fedadmins <FedID>: List the admins in a federation.
/joinfed <FedID>: Join the current chat to a federation. A chat can only join one federation. Chat owners only.
/leavefed: Leave the current federation. Only chat owners can do this.
/fedstat <FedID>: Gives information about your ban in a federation.
/fedstat <user ID> <FedID>: Gives information about a user's ban in a federation.
/chatfed: Information about the federation the current chat is in.</blockquote>
"""
buttons_fdu = [
    [
        InlineKeyboardButton("⬅️", callback_data="fed"),
    ]
]


@Bot.on_callback_query(filters.regex("^fdu$"))
async def ajbvfduiv(bot, query):
    await query.message.edit(
        text=text_fdu,
        reply_markup=InlineKeyboardMarkup(buttons_fdu),
        disable_web_page_preview=True,
    )

text_filt = """
**Here is the help for Filters:**

<blockquote>Make your chat more lively with filters; The bot will reply to certain words!
Filters are case insensitive; every time someone says your trigger words, Rose will reply something else! can be used to create your own commands, if desired.</blockquote>

<blockquote>/filters To Get All The Filters In The Chat.
/filter [FILTER_NAME] or /addfilter [FILTER_NAME] To Save A Filter(reply to a message).</blockquote>

<blockquote>Supported filter types are Text, Animation, Photo, Document, Video, video notes, Audio, Voice.</blockquote>

**To use more words in a filter use:**
<blockquote>/filter Hey_there or /addfilter Hey_there To filter "Hey there".
/stop [FILTER_NAME] or /stopfilter [FILTER_NAME] To Stop A Filter.
/stopall To delete all the filters in a chat (permanently).</blockquote>

**You can use markdown or html to save text too.**
"""
buttons_filt = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
    ]
]


@Bot.on_callback_query(filters.regex("^filter$"))
async def afddviv(bot, query):
    await query.message.edit(
        text=text_filt,
        reply_markup=InlineKeyboardMarkup(buttons_filt),
        disable_web_page_preview=True,
    )

text_lok = """
**Here is the help for Locks:**

<blockquote>Do stickers annoy you? or want to avoid people sharing links? or pictures? You're in the right place!
The locks module allows you to lock away some common items in the Telegram world; the bot will automatically delete them!</blockquote>

<blockquote>- /lock | /unlock | /locks [No Parameters Required]</blockquote>

**Parameters:**
<blockquote>messages | sticker | gif | media | games | polls

inline  | url | group_info | user_add | pin | photo

voice | video | audio | docs | plain

You can only pass the "all" parameter with /lock, not with /unlock</blockquote>

**Example:**
    /lock all
"""
buttons_lok = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>Save data for future users with notes!
Notes are great to save random tidbits of information; a phone number, a nice gif, a funny picture - anything!</blockquote>

<blockquote>/notes To Get All The Notes In The Chat.
/save [NOTE_NAME] or /addnote [NOTE_NAME] To Save A Note.
Supported note types are Text, Animation, Photo, Document, Video, video notes, Audio, Voice.</blockquote>

<blockquote>**To change caption of any files use.**
/save [NOTE_NAME] or /addnote [NOTE_NAME] [NEW_CAPTION].</blockquote>

<blockquote>#NOTE_NAME To Get A Note.</blockquote>

<blockquote>/delete [NOTE_NAME] or delnote [NOTE_NAME] To Delete A Note.
/deleteall To delete all the notes in a chat (permanently).</blockquote>
"""
buttons_not = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>Enable or disable nightmode (locks the chat at specified intervals everyday)</blockquote>
**Flags:**
<blockquote>'-s': "Specify starting time in 24hr format.
'-e': "Specify duration in hours / minute
'-d': "Disable nightmode for chat.</blockquote>

**Examples:**
<blockquote>/nightmode -s=23:53 -e=6h
/nightmode -s=23:50 -e=120m
/nightmode -d</blockquote>
"""
buttons_nm = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>This feature inspired from SangMata Bot. I'm created simple detection to check user data include username, first_name, and last_name.
/sangmata_set [on/off] - Enable/disable sangmata in groups.</blockquote>
"""
buttons_sm = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
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

<blockquote>All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!</blockquote>

**User commands:**
<blockquote>/pinned: Get the current pinned message.</blockquote>

**Admin commands:**
<blockquote>- /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
- /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.
- /unpinall: Unpins all the pinned message in the current chat.</blockquote>
"""

buttons_pn = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
    ]
]


@Bot.on_callback_query(filters.regex("^pn$"))
async def abvivpn(bot, query):
    await query.message.edit(
        text=text_pn,
        reply_markup=InlineKeyboardMarkup(buttons_pn),
        disable_web_page_preview=True,
    )

text_adf = """
**Antiflood**
<blockquote>You know how sometimes, people join, send 100 messages, and ruin your chat? With antiflood, that happens no more!
Antiflood allows you to take action on users that send more than x messages in a row. Actions are: ban/mute/kick/tban/tmute.</blockquote>

**Admin commands:**
<blockquote>/flood: Get the current antiflood settings
/setflood : Set the number of messages after which to take action on a user. Set to '0', 'off', or 'no' to disable.
/setfloodtimer  : Set the number of messages and time required for timed antiflood to take action on a user. Set to just 'off' or 'no' to disable.
/setfloodmode : Choose which action to take on a user who has been flooding. Possible actions: ban/mute/kick/tban/tmute
/clearflood : Whether to delete the messages that triggered the flood.</blockquote>
"""
buttons_adf = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
    ]
]


@Bot.on_callback_query(filters.regex("^adf$"))
async def abfiv(bot, query):
    await query.message.edit(
        text=text_adf,
        reply_markup=InlineKeyboardMarkup(buttons_adf),
        disable_web_page_preview=True,
    )

text_adc = """
**Anti-Channel**

<blockquote>Anti Channel Mode is a mode to prevent unwanted channel actions.</blockquote>

**Admin Commands:**
<blockquote>• /antichannelmode : Enables Anti Channel Mode to ban users who chat using channels.
• /antichannelmode : Disables Anti Channel Mode.
• /antichannelpin : Don't let telegram auto-pin linked channels. If no arguments are given, shows current setting.
• /cleanlinked : Delete messages sent by the linked channel.</blockquote>

<blockquote>Note: When using antichannel pins, make sure to use the /unpin command, instead of doing it manually. Otherwise, the old message will get re-pinned when the channel sends any messages.</blockquote>
"""
buttons_adc = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
    ]
]


@Bot.on_callback_query(filters.regex("^adc$"))
async def abcviv(bot, query):
    await query.message.edit(
        text=text_adc,
        reply_markup=InlineKeyboardMarkup(buttons_adc),
        disable_web_page_preview=True,
    )

#===================

TEXT_HP = """
**Extra-CMD**

<blockquote>Hey 👋 {}, 
Send command /privacy if you want know data collected by this bot.
All Commands can be used with: /</blockquote>
"""
BUTTONS_HP = [
    [
        InlineKeyboardButton("NSFW", callback_data="nsf"),
        InlineKeyboardButton("Ai", callback_data="ai"),
        InlineKeyboardButton("Cat & Dog", callback_data="cd"),
    ],
    [
        InlineKeyboardButton("Quotly", callback_data="q"),
        InlineKeyboardButton("Quiz", callback_data="qz"),
        InlineKeyboardButton("PyPi Search", callback_data="pyi"),
    ],
    [
        InlineKeyboardButton("Bypass", callback_data="byp"),
        InlineKeyboardButton("Couples", callback_data="cos"),
        InlineKeyboardButton("SessionGen", callback_data="sng"),
    ],
    [
        InlineKeyboardButton("Currency", callback_data="crc"),
        InlineKeyboardButton("CodeTester", callback_data="ct"),
        InlineKeyboardButton("UrbanDictionary", callback_data="bt"),
    ],
    [
        InlineKeyboardButton("Fun", callback_data="fn"),
        InlineKeyboardButton("MediaExtract", callback_data="mdx"),
        InlineKeyboardButton("MediaTool", callback_data="gen"),
    ],
    [
        InlineKeyboardButton("Inline", callback_data="ini"),
        InlineKeyboardButton("Misc", callback_data="mis"),
        InlineKeyboardButton("Ocr", callback_data="oc"),
    ],
    [
        InlineKeyboardButton("Sticker", callback_data="str"),
        InlineKeyboardButton("Paste", callback_data="pst"),
        InlineKeyboardButton("SFW", callback_data="sfwj"),
    ],
    [
        InlineKeyboardButton("WebScraper", callback_data="web"),
        InlineKeyboardButton("Karma", callback_data="kr"),
        InlineKeyboardButton("Nulis", callback_data="nui"),
    ],
    [
        InlineKeyboardButton("Extras", callback_data="ext"),
        InlineKeyboardButton("Anilist", callback_data="anil"),
        InlineKeyboardButton("Stylish-Txt", callback_data="stx"),
    ],
    [
        InlineKeyboardButton("Weather", callback_data="wtr"),
        InlineKeyboardButton("Wall", callback_data="wal"),
        InlineKeyboardButton("RM-BG", callback_data="rmb"),
    ],
    [
        InlineKeyboardButton("Chat-Bot", callback_data="ctb"),
        InlineKeyboardButton("Wiki", callback_data="wk"),
        InlineKeyboardButton("Telegraph Up", callback_data="tgf"),
    ],
    [
        InlineKeyboardButton("Web-Games", callback_data="wg"),
        InlineKeyboardButton(".", callback_data="h"),
        InlineKeyboardButton(".", callback_data="h"),
    ],
    [
        #InlineKeyboardButton("❮", callback_data="settings5"),
        InlineKeyboardButton("⬅️", callback_data="set_ge"),
        InlineKeyboardButton("❌", callback_data="close_cb"),
        InlineKeyboardButton("🏠", callback_data="home"),
        #InlineKeyboardButton("❯", callback_data="settings2"),
    ],
] 

@Bot.on_callback_query(filters.regex("^settings$"))
async def help_cb_handler1(bot, query):
    await query.message.edit(
        text=TEXT_HP.format(query.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(BUTTONS_HP),
        disable_web_page_preview=True,
    )

# =============================EXTRA_CMD================================
# =============================EXTRA_CMD================================
text_wg = """
**Web Games:**

× /webgame - To play Web Games from here, just click.
"""
buttons_wg = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^wg$"))
async def abvivg(bot, query):
    await query.message.edit(
        text=text_wg,
        reply_markup=InlineKeyboardMarkup(buttons_wg),
        disable_web_page_preview=True,
    )

text_tgf = """
**Telegraph Upload**

<blockquote>this is a Telegraph up module for images. I can upload media file on Telegra.ph. Maximum file size limit is 5Mb.</blockquote>

<blockquote>Use /timg or /telegraph to Reply to photos to make telegraph links.</blockquote>
"""
buttons_tgf = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
    ]
]


@Bot.on_callback_query(filters.regex("^tgf$"))
async def abviv(bot, query):
    await query.message.edit(
        text=text_tgf,
        reply_markup=InlineKeyboardMarkup(buttons_tgf),
        disable_web_page_preview=True,
    )

text_wk = """
**Wikipedia:**

• /wiki - wikipedia your query
"""
buttons_wk = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^wk$"))
async def abviv(bot, query):
    await query.message.edit(
        text=text_wk,
        reply_markup=InlineKeyboardMarkup(buttons_wk),
        disable_web_page_preview=True,
    )

text_ctb = """
**Chatbot**

<blockquote>Chatbot makes GoJo talk like a human.
Basically, there is chatbot inserted in Gojo, it can be used to talk in a frank way and can also be used to write essays, codes, birthday wishes, simply anything you want.</blockquote>

Commands:
<blockquote>/chatbot: Shows chatbot control panel.</blockquote>
"""
buttons_ctb = [
    [
        InlineKeyboardButton("⬅️", callback_data="group"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^ctb$"))
async def abviv(bot, query):
    await query.message.edit(
        text=text_ctb,
        reply_markup=InlineKeyboardMarkup(buttons_ctb),
        disable_web_page_preview=True,
    )

text_rmb = """
**Remove Background**

/rmbg Reply to image to remove background.
"""
buttons_rmb = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^rmb$"))
async def armbviv(bot, query):
    await query.message.edit(
        text=text_rmb,
        reply_markup=InlineKeyboardMarkup(buttons_rmb),
        disable_web_page_preview=True,
    )

text_wtr = """
**Weather**

/weather location Or city to get weather information.
"""
buttons_wtr = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]

@Bot.on_callback_query(filters.regex("^wtr$"))
async def abwwviv(bot, query):
    await query.message.edit(
        text=text_wtr,
        reply_markup=InlineKeyboardMarkup(buttons_wtr),
        disable_web_page_preview=True,
    )

text_wal = """
**Wallpapers**

/wall [wall_name] to get wallpepars.
extra c - /wallpapers 
"""
buttons_wal = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^wal$"))
async def abvivll(bot, query):
    await query.message.edit(
        text=text_wal,
        reply_markup=InlineKeyboardMarkup(buttons_wal),
        disable_web_page_preview=True,
    )

text_ext = """
<blockquote>__/meme cmd to get meme from meme api.
/mormeme cmd to get more memes.
/reddit cmd to get Random image from Reddit.
/morddit cmd to get more images from Reddit.
/unsplash cmd then your text to get images from unsplash.
/pexi cmd to get images from **Pexels**
/pexv cmd to get Videos from **Pexels**
/tor cmd to get Torrent movies links.
/repo the repository name to get GitHub repos.
/google cmd to get 10 quarys from Google.
/bingt cmd to get 10 quarys from Bing browser.
/yandex cmd to get 10 quarys from Yandex browser.
/ddg cmd to get 10 quarys from DuckDuckGo browser.
/ggimg cmd to get 10 Images from Google.
/bingimg cmd to get 10 Images from Bing.
/yandeximg cmd to get 10 Images from Yandex.
/ddgimg cmd to get 10 Images from DuckDuckGo.
/pimg cmd to get 6 images from Pinterest.</blockquote>
"""
buttons_ext = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^ext$"))
async def abviv(bot, query):
    await query.message.edit(
        text=text_ext,
        reply_markup=InlineKeyboardMarkup(buttons_ext),
        disable_web_page_preview=True,
    )

text_nsf = """
**NSFW**

<blockquote>Sometimes a lil bit of horni-stuff is fine, check this module for fine stuff!</blockquote>

**Admins Only:**
<blockquote>• /addnsfw: To Activate NSFW commands. (for groups)
• /rmnsfw: To Deactivate NSFW commands. (for groups)</blockquote>

**Following are the NSFW commands:**
<blockquote>• /nsfwwaifu
• /blowjob
• /nwaifu
• /bj
• /trap
• /nsfwneko
• /nneko
• /spank</blockquote>
"""
buttons_nsf = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^nsf$"))
async def abviv(bot, query):
    await query.message.edit(
        text=text_nsf,
        reply_markup=InlineKeyboardMarkup(buttons_nsf),
        disable_web_page_preview=True,
    )

text_sfw = """
**SFW**

This module is safe for work (for real!)

**Commands:**
<blockquote>• /neko: Sends Random SFW Neko source Images.
• /ngif: Sends Random Neko GIFs.
• /tickle: Sends Random Tickle GIFs.
• /feed: Sends Random Feeding GIFs.
• /gasm: Sends Random Orgasm Stickers.
• /avatar: Sends Random Avatar Stickers.
• /waifu: Sends Random Waifu Stickers.
• /kiss: Sends Random Kissing GIFs.
• /cuddle: Sends Random Cuddle GIFs.
• /foxgirl: Sends Random FoxGirl source Images.
• /smug: Sends Random Smug GIFs.
• /gecg: IDK
• /slap: Sends Random Slap GIFs.</blockquote>

**Some more SFW commands:**
<blockquote>• /shinobu
• /hug
• /megumin
• /bully
• /cry
• /awoo
• /woof
• /lick
• /pat
• /bonk
• /yeet
• /blush
• /smile
• /wave
• /highfive
• /handhold
• /nom
• /bite
• /glomp
• /slapgif
• /kill
• /kicks
• /happy
• /wink
• /poke
• /dance
• /cringe
• /wallpaper
• /goose</blockquote>
"""
buttons_sfw = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^sfwj$"))
async def abvsfiv(bot, query):
    await query.message.edit(
        text=text_sfw,
        reply_markup=InlineKeyboardMarkup(buttons_sfw),
        disable_web_page_preview=True,
    )

text_stx = """
**Stylish Text**

/font [your text] - just add your paragraph to make style texts.
"""
buttons_stx = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^stx$"))
async def abviv(bot, query):
    await query.message.edit(
        text=text_stx,
        reply_markup=InlineKeyboardMarkup(buttons_stx),
        disable_web_page_preview=True,
    )

text_act = """
**Quiz**

/quiz To get an random quizs
"""
buttons_act = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^qz$"))
async def abot_cb_handler6(bot, query):
    await query.message.edit(
        text=text_act,
        reply_markup=InlineKeyboardMarkup(buttons_act),
        disable_web_page_preview=True,
    )


text_adm = """
**Here is the help for Ai ChatBot Assistant:**

<blockquote>/ai - Generate text response from AI using Gemini AI By Google.
/ask | /ask2 - Generate text response from AI using OpenAI.
/gpt - Ask me anything with GPT-4o! 💡
/gemini - Dive deep into questions with Gemini-Pro! 
/llama - Experience creativity with Llama-3.1-405b! 🦙
/blackbox - Curious about BlackBoxAI-Pro? Just ask! 📦
/claude - to get ai message from 𝙲𝙻𝙾𝚄𝙳 𝚂𝙾𝙽𝙽𝙴𝚃 3.5.
/draw - drow your prompt to get photos.</blockquote>

**Ai-Gemini**
<blockquote>/askai
/aii [Reply to Image]
/aiseller
/aicook</blockquote> 
"""
buttons_adm = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^ai$"))
async def abot_cb_handler7(bot, query):
    await query.message.edit(
        text=text_adm,
        reply_markup=InlineKeyboardMarkup(buttons_adm),
        disable_web_page_preview=True,
    )


text_aut = """
**Here is the help for Birthday**

<blockquote>/remember [reply to user] [DAT] : To registers user date of birth in my database. If not replied to user then the DAT givien will be treated as yours
/nextbdays (/nbdays,/brithdays,/bdays) : Return upcoming birthdays of 10 users
/removebday (/rmbday) : To remove birthday from database (One can only remove their data from database not of others)
/settingbday (/sbday) : To configure the settings for wishing and all for the chat
/getbday (/gbday,/mybirthday,/mybday) [reply to user] : If replied to user get the replied user's birthday else returns your birthday</blockquote>

<blockquote>DAT should be in format of dd/mm/yyyy
Year is optional it is not necessary to pass it.</blockquote>
"""
buttons_aut = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^brt$"))
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
**SessionGen**

<blockquote>/genstring - Generate string session using this bot. Only support Pyrogram v2 and Telethon.</blockquote>
"""
buttons_apr = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^sng$"))
async def abot_cb_handler10(bot, query):
    await query.message.edit(
        text=text_apr,
        reply_markup=InlineKeyboardMarkup(buttons_apr),
        disable_web_page_preview=True,
    )


text_blt = """
/directurl [Link] - Bypass URL.

**Supported Link:**
<blockquote>- Pling and all aliases.
- Wetransfer
- Other link soon...</blockquote>

This feature is deprecated..
"""
buttons_blt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^byp$"))
async def abot_cb_handlerh(bot, query):
    await query.message.edit(
        text=text_blt,
        reply_markup=InlineKeyboardMarkup(buttons_blt),
        disable_web_page_preview=True,
    )


text_bt = """
**Urban Dictionary**

<blockquote>/ud [give any word] Type the word or expression you want to search.</blockquote>
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


text_bts = """
**Here is the help for WebScraper:**

<blockquote>/webss [URL] - Take A Screenshot Of A Webpage.
/melongmovie [query ] - Scrape website data from MelongMovie Web.
/lk21 [query ] - Scrape website data from LayarKaca21.
/pahe [query ] - Scrape website data from Pahe.li.
/terbit21 [query ] - Scrape website data from Terbit21.
/savefilm21 [query ] - Scrape website data from Savefilm21.
/movieku [query ] - Scrape website data from Movieku.cc
/kusonime [query ] - Scrape website data from Kusonime
/lendrive [query ] - Scrape website data from Lendrive
/klikxxi [query ] - Scrape website data from Klikxxi aka GoMov.
/samehadaku [query ] - Scrape website data from Samehadaku.
/nodrakor [query ] - Scrape website data from NoDrakor</blockquote>
"""
buttons_bts = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^web$"))
async def abot_cb_handlgguer(bot, query):
    await query.message.edit(
        text=text_bts,
        reply_markup=InlineKeyboardMarkup(buttons_bts),
        disable_web_page_preview=True,
    )


text_bsk = """
**Here is the help for Currency:**

/currency - Send structure message Telegram in JSON using Pyrogram Style.
"""
buttons_bsk = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^crc$"))
async def abot_cb_hangidler(bot, query):
    await query.message.edit(
        text=text_bsk,
        reply_markup=InlineKeyboardMarkup(buttons_bsk),
        disable_web_page_preview=True,
    )


text_ai = """
**Here is the help for CodeTester:**

<blockquote>This feature allows you to run multiple programming languages through this bot via the Glot.io api.  The following is a list of supported languages, for temporary commands only support with a "!"  like the example below.</blockquote>

**List of Supported Programming Languages:**
<blockquote>~> assembly
~> ats
~> bash
~> c
~> clojure
~> cobol
~> coffeescript
~> cpp
~> crystal
~> csharp
~> d
~> elixir
~> elm
~> erlang
~> fsharp
~> go
~> groovy
~> haskell
~> idris
~> java
~> javascript
~> julia
~> kotlin
~> lua
~> mercury
~> nim
~> nix
~> ocaml
~> perl
~> php
~> python
~> raku
~> ruby
~> rust
~> scala
~> swift
~> typescript</blockquote>

**Example:**
<blockquote>~> !python print("Hai aku Gojo x satuto")</blockquote>
"""
buttons_ai = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^ct$"))
async def abot_cb_ughandler(bot, query):
    await query.message.edit(
        text=text_ai,
        reply_markup=InlineKeyboardMarkup(buttons_ai),
        disable_web_page_preview=True,
    )


text_dv = """
**Here is the help for nulis:**

Command: /nulis [reply to msg or after cmd]
Desc: For those of you who are lazy to write.
"""
buttons_dv = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^nui$"))
async def abot_cb_handpcler(bot, query):
    await query.message.edit(
        text=text_dv,
        reply_markup=InlineKeyboardMarkup(buttons_dv),
        disable_web_page_preview=True,
    )


text_flt = """
**Here is the help for Fun:**

<blockquote>/memify [text] - Reply to sticker to give text on sticker.
/react [emoji | list of emoji] - React to any message (Sudo and Owner only)
/beri [pesan] - Giving false hope to someone hehehe
/dice - Randomly roll the dice
/tebakgambar - Play "Tebak Gambar" in any room chat
/tebaklontong - Play "Tebak Lontong" in any room chat
/tebakkata - Play "Tebak Kata" in any room chat
/tebaktebakan - Play "Tebak Tebakan" in any room chat.
/truth | /dare Teuth or Dare Game.</blockquote>
"""
buttons_flt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^fn$"))
async def abot_cb_handlehcr(bot, query):
    await query.message.edit(
        text=text_flt,
        reply_markup=InlineKeyboardMarkup(buttons_flt),
        disable_web_page_preview=True,
    )


text_fgl = """
**Here is the help for MediaExtract:**

<blockquote>/extractmedia [URL] - Extract subtitle or audio from video using link. (Not support TG File to reduce bandwith usage.)
/converttosrt [Reply to .ass or .vtt TG File] - Convert from .ass or .vtt to srt
/converttoass [Reply to .srt or .vtt TG File] - Convert from .srt or .vtt to srt</blockquote>
"""
buttons_fgl = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^mdx$"))
async def abot_cb_handhjler(bot, query):
    await query.message.edit(
        text=text_fgl,
        reply_markup=InlineKeyboardMarkup(buttons_fgl),
        disable_web_page_preview=True,
    )


text_fk = """
**Here is the help for MediaTool:**

<blockquote>/genss [reply to video] - Generate Screenshot From Video. (Support TG Media and Direct URL)
/mediainfo [link/reply to TG Video] - Get Mediainfo From File.</blockquote>
"""
buttons_fk = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^gen$"))
async def abot_cb_hangenlr(bot, query):
    await query.message.edit(
        text=text_fk,
        reply_markup=InlineKeyboardMarkup(buttons_fk),
        disable_web_page_preview=True,
    )


text_fon = """
**Here is the help for InlineFeature:**

<blockquote>To use this feature, just type bot username with following args below.
~ imdb [query] - Search movie details in IMDb.com.
~ pypi [query] - Search package from Pypi.
~ git [query] - Search in Git.
~ google [query] - Search in Google.
~ info [user id/username] - Check info about a user.</blockquote>
"""
buttons_fon = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^ini$"))
async def abot_cb_hanipdler(bot, query):
    await query.message.edit(
        text=text_fon,
        reply_markup=InlineKeyboardMarkup(buttons_fon),
        disable_web_page_preview=True,
    )


text_mis = """
**Here is the help for Misc:**

<blockquote>/carbon [text or reply to text or caption] - Make beautiful snippet code on carbon from text.
/removebg [Reply to image] - Remove background from image.
/calc - Simple math calculator using inline buttons.
/kbbi [keyword] - Search definition on KBBI (For Indonesian People)
/sof [query] - Search your problem in StackOverflow.
/google [query] - Search using Google Search.
(/tr, /trans, /translate) [lang code] - Translate text using Google Translate.
/tts - Convert Text to Voice.
/imdb [query] - Find Movie Details From IMDB.com.
/tmdb [query] - Find Movie Details From TMDB.com
/readqr [reply to photo] - Read QR Code From Photo.
/createqr [text] - Convert Text to QR Code.
/animegj [query] - Search title in myanimelist.
/info - Get info user with Pic and full description if user set profile picture.
/id - Get simple user ID.
/bots - To see how much bots on group.
/gdata | /groupinfo - To get Group datas.
/link | givelink To get group link.
/figlet - To creat finglet ex:` /figlet Gojo`</blockquote>
"""
buttons_mis = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^mis$"))
async def abot_cb_handlsser(bot, query):
    await query.message.edit(
        text=text_mis,
        reply_markup=InlineKeyboardMarkup(buttons_mis),
        disable_web_page_preview=True,
    )


text_gt = """
**Here is the help for OCR:**
<blockquote>/ocr [reply to photo] - Read Text From Image</blockquote>
"""
buttons_gt = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^oc$"))
async def abot_cb_handlpnner(bot, query):
    await query.message.edit(
        text=text_gt,
        reply_markup=InlineKeyboardMarkup(buttons_gt),
        disable_web_page_preview=True,
    )


text_gl = """
**Cat and Dog:**

<blockquote>/Cat | /dog - To get random cat and dog photos.</blockquote>
"""
buttons_gl = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^cd$"))
async def abot_cb_handllnver(bot, query):
    await query.message.edit(
        text=text_gl,
        reply_markup=InlineKeyboardMarkup(buttons_gl),
        disable_web_page_preview=True,
    )


text_gli = """
**Here is the information about Couples**

<blockquote>/couples - Get Todays Couples Of The Group In Interactive View.</blockquote>
"""
buttons_gli = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^cop$"))
async def abot_cb_handviler(bot, query):
    await query.message.edit(
        text=text_gli,
        reply_markup=InlineKeyboardMarkup(buttons_gli),
        disable_web_page_preview=True,
    )

text_gdy = """
**Here is the help for Stickers:**

<blockquote>/kang [Reply to sticker] - Add sticker to your pack.
/unkang [Reply to sticker] - Remove sticker from your pack (Only can remove sticker that added by this bot.).
/getsticker - Convert sticker to png.
/stickerid - View sticker ID.</blockquote>
"""
buttons_gdy = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^str$"))
async def abot_cb_handlesnr(bot, query):
    await query.message.edit(
        text=text_gdy,
        reply_markup=InlineKeyboardMarkup(buttons_gdy),
        disable_web_page_preview=True,
    )


text_hsr = """
**Here is the help for Karma:**

<blockquote>Give reputation to other people in group.
/karma_toggle [enable/disable] - Enable/Disable Karma.
/karma - View all karma from member group.</blockquote>
"""
buttons_hsr = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^kr$"))
async def abot_cb_handihoer(bot, query):
    await query.message.edit(
        text=text_hsr,
        reply_markup=InlineKeyboardMarkup(buttons_hsr),
        disable_web_page_preview=True,
    )


text_htg = """
**Here is the help for Paste:**

<blockquote>/paste [Text/Reply To Message] - Post text to My Pastebin.
/sbin [Text/Reply To Message] - Post text to Spacebin.
/neko [Text/Reply To Message] - Post text to Nekobin.
/tgraph [Text/Reply To Message] - Post text to Telegraph.
/imgbb [Images] - Upload image to ImgBB.
/rentry [Text/Reply To Message] - Post text to Rentry using markdown style.</blockquote>
"""
buttons_htg = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^pst$"))
async def abot_cb_handluvjker(bot, query):
    await query.message.edit(
        text=text_htg,
        reply_markup=InlineKeyboardMarkup(buttons_htg),
        disable_web_page_preview=True,
    )


text_anx = """
🥀 **AniList**
<blockquote>Since this is an anime themed bot, so anime module is a must! Tester provides you the best anime based commands including anime news and much more!</blockquote>

<blockquote>/anihelp: Get interactive and detailed help on anime commands</blockquote>

"""
buttons_anx = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^anil$"))
async def abot_cb_hvivandler(bot, query):
    await query.message.edit(
        text=text_anx,
        reply_markup=InlineKeyboardMarkup(buttons_anx),
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



text_mog = """
**Quotly**

<blockquote>I will help create a quote from a post.
Bot can work both in private messages and in groups.</blockquote>

<blockquote>/q — make a quote from the message [reply to the message]</blockquote>

/q2 Will make a quotly sticker of replied text, you can also use /q r, /q 3 and /q white to see blek megik happening.
/qrate to rate Quotly.
/qtop to get Top Quotly from group.
/qrand blah blah blah 😒

"""
buttons_mog = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^q$"))
async def abot_cb_hajjvvindler(bot, query):
    await query.message.edit(
        text=text_mog,
        reply_markup=InlineKeyboardMarkup(buttons_mog),
        disable_web_page_preview=True,
    )

text_ps = """
**PyPi**

add query after command. Ex: /pypi pyrogram
"""
buttons_ps = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^pyi$"))
async def abot_cb_handguugler(bot, query):
    await query.message.edit(
        text=text_ps,
        reply_markup=InlineKeyboardMarkup(buttons_ps),
        disable_web_page_preview=True,
    )



text_sg = """
**SangMata**

<blockquote>This feature inspired from SangMata Bot. I'm created simple detection to check user data include username, first_name, and last_name.
/sangmata_set [on/off] - Enable/disable sangmata in groups.</blockquote>
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


text_cos = """
**Couples:**

/couples - To Choose Couple Of The Day in group.
"""
buttons_cos = [
    [
        InlineKeyboardButton("⬅️", callback_data="settings"),
        InlineKeyboardButton("❌", callback_data="close"),
    ]
]


@Bot.on_callback_query(filters.regex("^cos$"))
async def abot_cb_hanibibbdler(bot, query):
    await query.message.edit(
        text=text_cos,
        reply_markup=InlineKeyboardMarkup(buttons_cos),
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
