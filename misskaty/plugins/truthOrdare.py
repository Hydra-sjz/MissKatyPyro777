import aiohttp

from misskaty.custom_filter import register
#from Emilia.helper.disable import disable


async def fetch_question(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data.get("question")


async def get_dare_question():
    return await fetch_question("https://api.truthordarebot.xyz/v1/dare")


async def get_truth_question():
    return await fetch_question("https://api.truthordarebot.xyz/v1/truth")


@register(pattern="dare")
async def dare(event):
    dare = await get_dare_question()
    if dare:
        await event.reply(f"{dare}")


@register(pattern="truth")
async def truth(event):
    truth = await get_truth_question()
    if truth:
        await event.reply(f"{truth}")


# DONE: Truth or Dare
