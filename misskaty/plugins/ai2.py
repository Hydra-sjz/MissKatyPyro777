
from pyrogram.types import *
from HorridAPI import Async 
from pyrogram.types import InputMediaPhoto
from pyrogram import Client, filters
from HorridAPI import Mango
from misskaty import app
from HorridAPI import api
import requests
import json


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "content-type": "application/json",
}


async def create_paste(message, extension=None):
    siteurl = "https://pasty.lus.pm/api/v1/pastes"
    data = {"content": message}
    try:
        response = requests.post(url=siteurl, data=json.dumps(data), headers=headers)
    except Exception as e:
        return 'Long message, Error From pasty.lus.pm site crashed'
    if response.ok:
        response = response.json()
        purl = (
            f"https://pasty.lus.pm/{response['id']}.{extension}"
            if extension
            else f"https://pasty.lus.pm/{response['id']}.txt"
        )
        return purl


@app.on_message(filters.command("llamaai"))
async def llamashchat(client, message):
    
    if len(message.command) < 2:
        return await message.reply_text("Please provide the query")
        
    reply = message.reply_to_message    
    if reply:
        query = f"Old conversation: {l.text}\n\nNew conversation: {message.text}"
    else:
        query = " ".join(message.command[1:])
    msg = await message.reply_text("🔍")
    ai = api.llama(query)
    if len(ai) > 3700:
        result = await create_paste(ai)  
        await msg.edit(result)
    else:
        await msg.edit(ai)


@app.on_message(filters.command(["imgai", "imagesearch"]))
async def imagessss(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**Where is the query? 🤔\n\nPlease provide a query like:**\n\n`/img Luffy`")
    
    query = " ".join(message.command[1:])
    k = await message.reply_text("**Searching.. 🔍**")
    
    image = await Async().images(        
        query=query,
        page=7
    )
    
    MEDIA = []
    p = 0 
    for img in image["result"]:
        p += 1
        await k.edit(f"**⚡ Successfully fetched {p}**")
        MEDIA.append(InputMediaPhoto(media=img["images"]))
    
    if MEDIA:
        await message.reply_media_group(MEDIA)
        await k.delete()
    else:
        await k.edit("**No images found. 🙃**")


@app.on_message(filters.command("blackboxai"))
async def blacbskbox(client, message):
    
    if len(message.command) < 2:
        return await message.reply_text("Please provide the query")
            
    reply = message.reply_to_message    
    if reply:
        query = f"Old conversation: {l.text}\n\nNew conversation: {message.text}"
    else:
        query = " ".join(message.command[1:])
    msg = await message.reply_text("🔍")
    mango = Mango()
    response = mango.chat.completions.create(
        model="blackbox",      
        messages=[{"role": "user", "content": query}]
    )
    if len(response.text) > 3700:        
        result = await create_paste(response.text)  
        await msg.edit(result)       
    else:
        await msg.edit(response.text)
      

@app.on_message(filters.command("claudeai"))
async def claiaude(client, message):
    
    if len(message.command) < 2:
        return await message.reply_text("Please provide the query")
            
    reply = message.reply_to_message    
    if reply:
        query = f"Old conversation: {l.text}\n\nNew conversation: {message.text}"
    else:
        query = " ".join(message.command[1:])
    msg = await message.reply_text("🔍")
    mango = Mango()
    response = mango.chat.completions.create(
        model="claude-3.5-sonnet",      
        messages=[{"role": "user", "content": query}]
    )
    if len(response.text) > 3700:        
        result = await create_paste(response.text)  
        await msg.edit(result)       
    else:
        await msg.edit(response.text)


@app.on_message(filters.command("googleai"))
async def Googleaii(client, message):
    
    if len(message.command) < 2:
        return await message.reply_text("Please provide the query")
            
    reply = message.reply_to_message    
    if reply:
        query = f"Old conversation: {l.text}\n\nNew conversation: {message.text}"
    else:
        query = " ".join(message.command[1:])
    msg = await message.reply_text("🔍")
    mango = Mango()
    response = mango.chat.completions.create(
        model="gemini-1.5-flash",      
        messages=[{"role": "user", "content": query}]
    )
    if len(response.text) > 3700:        
        result = await create_paste(response.text)  
        await msg.edit(result)       
    else:
        await msg.edit(response.text)


@app.on_message(filters.command("gemma_ai"))
async def gemma_chat(client, message):
    
    if len(message.command) < 2:
        return await message.reply_text("Please provide the query")
        
    reply = message.reply_to_message    
    if reply:
        query = f"Old conversation: {l.text}\n\nNew conversation: {message.text}"
    else:
        query = " ".join(message.command[1:])
    msg = await message.reply_text("🔍")
    mango = Mango()
    response = mango.chat.completions.create(
        model="gemma2-9b-It",
        messages=[{"role": "user", "content": query}]
    )
    if len(response.text) > 3700:        
        result = await create_paste(response.text)  
        await msg.edit(result)       
    else:
        await msg.edit(response.text)


@app.on_message(filters.command(["gptai", "mango"]))
async def mango_chats(client, message):
    
    if len(message.command) < 2:
        return await message.reply_text("Please provide the query")
            
    reply = message.reply_to_message    
    if reply:
        query = f"Old conversation: {l.text}\n\nNew conversation: {message.text}"
    else:
        query = " ".join(message.command[1:])
    msg = await message.reply_text("🔍")
    mango = Mango()
    response = mango.chat.completions.create(
        model="gpt-3.5-turbo",      
        messages=[{"role": "user", "content": query}]
    )
    if len(response.text) > 3700:        
        result = await create_paste(response.text)  
        await msg.edit(result)       
    else:
        await msg.edit(response.text)

@app.on_message(filters.command("gpt4"))
async def gpt4ai(client, message):
    
    if len(message.command) < 2:
        return await message.reply_text("Please provide the query")
            
    reply = message.reply_to_message    
    if reply:
        query = f"Old conversation: {l.text}\n\nNew conversation: {message.text}"
    else:
        query = " ".join(message.command[1:])
    msg = await message.reply_text("🔍")
    mango = Mango()
    response = mango.chat.completions.create(
        model="gpt-4o",      
        messages=[{"role": "user", "content": query}]
    )
    if len(response.text) > 3700:        
        result = await create_paste(response.text)  
        await msg.edit(result)       
    else:
        await msg.edit(response.text)
      
