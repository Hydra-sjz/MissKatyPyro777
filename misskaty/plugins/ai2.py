from .paste import create_paste
from pyrogram.types import *

from pyrogram import Client, filters
from HorridAPI import Mango
from misskaty import app

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
      
