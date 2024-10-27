import requests
import nekos
from PIL import Image
import os

from misskaty import app as bot
from pyrogram import filters
from pyrogram.types import Message

"""
Working cmds:
/neko
/wallpaper
/waifu
/smug
/kiss
/foxgirl
/gasm
/tickle
/ngif
/feed
/cuddle
"""

@bot.on_message(filters.command("feed"))
def feedd(_,  m: Message):
    target = "feed"
    m.reply_video(nekos.img(target))
    
@bot.on_message(filters.command("neko"))
def ndeko(_,  m: Message):
    target = "neko"
    m.reply_photo(nekos.img(target))

@bot.on_message(filters.command("wallpaper"))
def wafllpaper(_,  m: Message):
    target = "wallpaper"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("ngif"))
def ngidf(_,  m: Message):
    target = "ngif"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("tickle"))
def ticklef(_,  m: Message):
    target = "tickle"
    m.reply_video(nekos.img(target))

@bot.on_message(filters.command("gasm"))
def gfasm(_,  m: Message):
    target = "gasm"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    m.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


@bot.on_message(filters.command("poke"))
def pobke(_,  m: Message):
    target = "poke"
    m.reply_animatiom(nekos.img(target))

    
@bot.on_message(filters.command("waifu"))
def hwaifu(_,  m: Message):
    target = "waifu"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    m.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


@bot.on_message(filters.command("kiss"))
def kikss(_,  m: Message):
    target = "kiss"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("cuddle"))
def cudhdle(_,  m: Message):
    target = "cuddle"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("foxgirl"))
def foxghirl(_,  m: Message):
    target = "fox_girl"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("smug"))
def simug(_,  m: Message):
    target = "smug"
    m.reply_animation(nekos.img(target))


@bot.on_message(filters.command("8ball"))
def bjaka(_,  m: Message):
    target = "8ball"
    m.reply_photo(nekos.img(target))

    
@bot.on_message(filters.command('wink'))
def wjink(_,message):
    reply = message.reply_to_message
    if reply:
        res = requests.get('https://some-random-api.ml/animu/wink').json()
        url = res['link']
        reply.reply_animation(url)
        
    else:
        message.reply_animation(url)
        
        
@bot.on_message(filters.command('hug'))
def bhug(_,message):
    reply = message.reply_to_message
    if reply:
        res = requests.get('https://some-random-api.ml/animu/hug').json()
        url = res['link']
        reply.reply_animation(url)
        
    else:
        message.reply_animation(url)

@bot.on_message(filters.command('pat'))
def phat(_,message):
    reply = message.reply_to_message
    if reply:
        res = requests.get('https://some-random-api.ml/animu/pat').json()
        url = res['link']
        reply.reply_animation(url)
        
    else:
        message.reply_animation(url)

@bot.on_message(filters.command("slap"))
def slagjp(_, message: Message):
    reply = message.reply_to_message
    if reply:
        res = requests.get("https://api.rei.my.id/v3/slap").json()
        url = res["url"]
        reply.reply_animation(url)
        
    else:
          message.reply_animation(url)
