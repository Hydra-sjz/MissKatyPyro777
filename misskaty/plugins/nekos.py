import requests

from PIL import Image
import os

from misskaty import app as bot
from pyrogram import filters
from pyrogram.types import Message



        
        
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
