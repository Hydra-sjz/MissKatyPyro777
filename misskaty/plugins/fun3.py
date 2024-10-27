from pyrogram.types import Message
from pyrogram import filters
from misskaty import app as bot
import random
import requests 
        

BOT_ID = "7057123792"
@bot.on_message(filters.regex('good morning'))
def gm(_, m: Message):
    reply = m.reply_to_message
    if reply:
        m.reply(f"good morning! {reply.from_user.mention}")
    else:
        m.reply(f"good morning! {m.from_user.mention}")
 

@bot.on_message(filters.regex('good night'))
def gn(_, m: Message):
    reply = m.reply_to_message
    if reply:
        m.reply(f"good night! {reply.from_user.mention}")
    else:
        m.reply(f"good night! {m.from_user.mention}")
    
gbam_text = """
#GBANNED
**Froma Chat:** @{}
**Admin:** {}
**User :** {}
**Reason:** `{}`
**Chat Count:** `{}`
"""


gban_img = "https://telegra.ph/file/0a0657d58149b982efcd0.jpg"

@bot.on_message(filters.command(["gban", "gbam"]))
async def gbams(_, m: Message):
      reply = m.reply_to_message
      if not reply:
       return await m.reply("reply someone:\n/gban or /gbam")
      user1 = m.from_user
      reason = m.text.split(None, 1)[1] or "None"
      count = random.randint(10,30)
      user2 = reply.from_user
      chat = m.chat
      if reply.from_user.id == BOT_ID:
          return await m.reply_text("nigga I can't gban myself")
      if reply:
           gbam = await m.reply_photo(gban_img,caption="Gbaning...")
      await gbam.edit_caption(gbam_text.format(chat.username,user1.mention,
                                            user2.mention,reason,count))
       
@bot.on_message(filters.command('meme'))
def ddmeme(_,message: Message):
      res = requests.get('https://some-random-api.ml/meme').json()
      url = res['image']
      text = res['caption']
      message.reply_photo(photo=url, caption=text)

      
@bot.on_message(filters.command("gjoke"))
def joker(_, message: Message):
        res = requests.get('https://some-random-api.ml/joke').json()
        text = res['joke']
        message.reply_text(text)
        
@bot.on_message(filters.command("tickle"))
def ticfkle(_, message: Message):
        res = requests.get('https://nekos.best/tickle').json()
        tickle = res['tickle']
        message.reply_animation(tickle)
