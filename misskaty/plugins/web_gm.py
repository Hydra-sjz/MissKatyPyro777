import asyncio
import random
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram import filters
from misskaty import app as Mbot
#from walls import ANIM_PICS, ANIMALS_PICS, LOGO_PICS, CARS_PICS, DROWIG_PICS, FUNNY_PICS, ENTERT_PICS, GAME_PICS, LOVE_PICS, MUSIC_PICS, NATURE_PICS, SAYING_PICS, SPACE_PICS, COMIC_PICS, SPORT_PICS, PATTER_PICS, TECHNO_PICS, DESIN_PICS, HOLDAY_PICS, PEOPL_PICS, OTHERS_PICS                      
from misskaty.vars import LOG_CHANNEL
from misskaty.core import pyro_cooldown

WBG = """
🕹️ **WEB GAMES LOG ALERT** 🕹️

📛**Triggered Command** : /webgame
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @Musicx_dlbot
"""

cap_g = """
🤗Hey {}, 👾 Welcome to Web Games Module.
Choose the below bottons to play Web Games.
"""
#==========
@Mbot.on_message(filters.private & filters.command("webgame") & pyro_cooldown.wait(10)) 
async def w_game(client, message):
    m1 = await message.reply_animation(
        animation="https://te.legra.ph/file/ff1864a8e2266baa680f7.mp4",
        caption=cap_g.format(message.from_user.first_name), 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "🎮PoKi Games", "🎮CrazyGames"
            ],[
                "🎮BGames", "🎮Webgames .io" 
            ],[
                "🎮Now gg", "🎮GamePix"
            ],[
                "➖➖➖➖➖➖➖➖➖➖"
            ],[ 
                "🕹️Skribbl .io", "🕹️Diep .io"
            ],[
                "🕹️TicTac Toe", "🕹️Connect 4"
            ],[
                "🕹️Chess 1", "🕹️Chess 2"
            ],[
                "🕹️Gomoku", "🕹️Blazing Blades"
            ],[
                "🕹️2048", "🕹️Gartic.io"
            ],[
                "🕹️Wordle", "🕹️Sqword"
            ],[
                "❌ CLOSE ❌"
            ]], 
            
            resize_keyboard=True
        ) 
    )
    #w1 = await message.reply_text(wall_tottal)
    await client.send_message(LOG_CHANNEL, WBG.format(message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
    await message.delete()
    await asyncio.sleep(1200)
    await m1.delete()
    #await w1.delete()

@Mbot.on_message(filters.private & filters.regex("◀️ Go to Back")) 
async def w_game2(client, message):
    m1 = await message.reply_animation(
        animation="https://te.legra.ph/file/ff1864a8e2266baa680f7.mp4",
        caption=cap_g.format(message.from_user.first_name), 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "🎮PoKi Games", "🎮CrazyGames"
            ],[
                "🎮BGames", "🎮Webgames .io" 
            ],[
                "🎮Now gg", "🎮GamePix"
            ],[
                "➖➖➖➖➖➖➖➖➖➖"
            ],[ 
                "🕹️Skribbl .io", "🕹️Diep .io"
            ],[
                "🕹️TicTac Toe", "🕹️Connect 4"
            ],[
                "🕹️Chess 1", "🕹️Chess 2"
            ],[
                "🕹️Gomoku", "🕹️Blazing Blades"
            ],[
                "🕹️2048", "🕹️Gartic.io"
            ],[
                "🕹️Wordle", "🕹️Sqword"
            ],[
                "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    )
    #w1 = await message.reply_text(wall_tottal)
    await message.delete()
    await asyncio.sleep(1200)
    await m1.delete()
#================Main=================


@Mbot.on_message(filters.private & filters.regex("🎮PoKi Games") & pyro_cooldown.wait(10))
async def pokig(client, message):
    pk = await message.reply_text(
        text="**🕹️ Poki Games** [ㅤ](t.me/Msxg_bot/webpoki)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await pk.delete()
    
@Mbot.on_message(filters.private & filters.regex("🎮CrazyGames") & pyro_cooldown.wait(10))
async def cgg(client, message):
    cg = await message.reply_text(
        text="**🕹️ Crazy Games** [ㅤ](http://t.me/Msxg_bot/webcrazyg)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await cg.delete()
    
@Mbot.on_message(filters.private & filters.regex("🎮BGames") & pyro_cooldown.wait(10))
async def bgg(client, message):
    bg = await message.reply_text(
        text="**🕹️ BGAMES** [ㅤ](t.me/Msxg_bot/webbg)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await bg.delete()
    
@Mbot.on_message(filters.private & filters.regex("🎮Webgames .io") & pyro_cooldown.wait(10))
async def wbg(client, message):
    wg = await message.reply_text(
        text="**🕹️ WebGames .io** [ㅤ](http://t.me/Msxg_bot/webgio)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await wg.delete()
    
@Mbot.on_message(filters.private & filters.regex("🕹️Skribbl .io") & pyro_cooldown.wait(10))
async def skg(client, message):
    sb = await message.reply_text(
        text="**🕹️ Skribbl .io** [ㅤ](http://t.me/Msxg_bot/websrb)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await sb.delete()

@Mbot.on_message(filters.private & filters.regex("🕹️Diep .io") & pyro_cooldown.wait(10))
async def dptg(client, message):
    di = await message.reply_text(
        text="**🕹️ Diep .io** [ㅤ](http://t.me/Msxg_bot/webderp)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()

@Mbot.on_message(filters.private & filters.regex("🕹️TicTac Toe") & pyro_cooldown.wait(10))
async def tttpg(client, message):
    di = await message.reply_text(
        text="**🕹️ Tic Tac Toe** [ㅤ](https://t.me/Msxg_bot/webttt)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()

@Mbot.on_message(filters.private & filters.regex("🕹️Connect 4") & pyro_cooldown.wait(10))
async def cng(client, message):
    di = await message.reply_text(
        text="**🕹️ Connect 4** [ㅤ](http://t.me/Msxg_bot/webcn4)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()

@Mbot.on_message(filters.private & filters.regex("🕹️Gomoku") & pyro_cooldown.wait(10))
async def gomkg(client, message):
    di = await message.reply_text(
        text="**🕹️ Gomoku** [ㅤ](http://t.me/Msxg_bot/webgmk)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()

@Mbot.on_message(filters.private & filters.regex("🕹️Chess 1") & pyro_cooldown.wait(10))
async def chsg(client, message):
    di = await message.reply_text(
        text="**🕹️ Chess 1** [ㅤ](http://t.me/Msxg_bot/webchs)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()
    
@Mbot.on_message(filters.private & filters.regex("🕹️Chess 2") & pyro_cooldown.wait(10))
async def chs2g(client, message):
    di = await message.reply_text(
        text="**🕹️ Chess 2** [ㅤ](http://t.me/Msxg_bot/webchs2)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()

@Mbot.on_message(filters.private & filters.regex("🕹️Blazing Blades") & pyro_cooldown.wait(10))
async def blazg(client, message):
    di = await message.reply_text(
        text="**🕹️ Blazing Blades** [ㅤ](http://t.me/Msxg_bot/webblz)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()

@Mbot.on_message(filters.private & filters.regex("🎮Now gg") & pyro_cooldown.wait(10))
async def nowgg(client, message):
    di = await message.reply_text(
        text="**🎮 Now. GG** [ㅤ](http://t.me/Msxg_bot/appnwgg)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()

@Mbot.on_message(filters.private & filters.regex("🎮GamePix") & pyro_cooldown.wait(10))
async def gmpx(client, message):
    di = await message.reply_text(
        text="**🎮Game Pix** [ㅤ](http://t.me/Msxg_bot/appgpix)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()

@Mbot.on_message(filters.private & filters.regex("🕹️2048") & pyro_cooldown.wait(10))
async def hshs(client, message):
    di = await message.reply_text(
        text="**🕹️ 2048** [ㅤ](http://t.me/Msxg_bot/app248)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()

@Mbot.on_message(filters.private & filters.regex("🕹️Gartic.io") & pyro_cooldown.wait(10))
async def grio(client, message):
    di = await message.reply_text(
        text="**🕹️ Gartic. io** [ㅤ](http://t.me/Msxg_bot/appgtio)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()

@Mbot.on_message(filters.private & filters.regex("🕹️Wordle") & pyro_cooldown.wait(10))
async def wrd(client, message):
    di = await message.reply_text(
        text="**🕹️Wordle** [ㅤ](http://t.me/Msxg_bot/appwrd)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()

@Mbot.on_message(filters.private & filters.regex("🕹️Sqword") & pyro_cooldown.wait(10))
async def sqwd(client, message):
    di = await message.reply_text(
        text="**🕹️ Sqword** [ㅤ](http://t.me/Msxg_bot/appsqw)", 
        reply_markup=ReplyKeyboardMarkup(
            [[
                "◀️ Go to Back", "❌ CLOSE ❌"
            ]], 
            resize_keyboard=True
        ) 
    ) 
    await asyncio.sleep(4)
    await message.delete()
    await asyncio.sleep(1800)
    await di.delete()
