# DONE: SFW

import nekos
from requests import get

from misskaty import tle as meow
from misskaty.custom_filter import register
#from Emilia.helper.disable import disable
from misskaty.ultis_ex.wmilia_m.decorators import exception

url_sfw = "https://api.waifu.pics/sfw/"


@exception
async def send_media(event, img):
    if event.reply_to:
        replied_message = await event.get_reply_message()
        if replied_message:
            return await meow.send_file(event.chat_id, img, reply_to=replied_message.id)
        else:
            return await event.reply(file=img)
    return await event.reply(file=img)


@register(pattern="waifu")
async def waifu(event):
    url = f"{url_sfw}waifu"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="cosplay2")
async def waicosu(event):
    r = get("https://waifu-api.vercel.app").json()
    await send_media(event, r)


@register(pattern="neko")
async def neko(event):
    url = f"{url_sfw}neko"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="shinobu")
async def shinobu(event):
    url = f"{url_sfw}shinobu"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="megumin")
async def megumin(event):
    url = f"{url_sfw}megumin"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="bully")
async def bully(event):
    url = f"{url_sfw}bully"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="cuddle")
async def cuddle(event):
    url = f"{url_sfw}cuddle"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="cry")
async def cry(event):
    url = f"{url_sfw}cry"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="hug")
async def hug(event):
    url = f"{url_sfw}hug"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="awoo")
async def awoo(event):
    url = f"{url_sfw}awoo"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="kiss")
async def kiss(event):
    url = f"{url_sfw}kiss"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="lick")
async def lick(event):
    url = f"{url_sfw}lick"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="pat")
async def pat(event):
    url = f"{url_sfw}pat"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="smug")
async def smug(event):
    url = f"{url_sfw}smug"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="bonk")
async def bonk(event):
    url = f"{url_sfw}bonk"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="yeet")
async def yeet(event):
    url = f"{url_sfw}yeet"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="blush")
async def blush(event):
    url = f"{url_sfw}blush"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="smile")
async def smile(event):
    url = f"{url_sfw}smile"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="wave")
async def wave(event):
    url = f"{url_sfw}wave"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="highfive")
async def highfive(event):
    url = f"{url_sfw}highfive"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="handhold")
async def handhold(event):
    url = f"{url_sfw}handhold"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="nom")
async def nom(event):
    url = f"{url_sfw}nom"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="bite")
async def bite(event):
    url = f"{url_sfw}bite"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="glomp")
async def glomp(event):
    url = f"{url_sfw}glomp"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="slap")
async def slap(event):
    url = f"{url_sfw}slap"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="kill")
async def killgif(event):
    url = f"{url_sfw}kill"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="kicks")
async def kickgif(event):
    url = f"{url_sfw}kick"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="happy")
async def happy(event):
    url = f"{url_sfw}happy"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="wink")
async def wink(event):
    url = f"{url_sfw}wink"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="poke")
async def poke(event):
    url = f"{url_sfw}poke"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="dance")
async def dance(event):
    url = f"{url_sfw}dance"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="cringe")
async def cringe(event):
    url = f"{url_sfw}cringe"
    result = get(url).json()
    img = result["url"]
    await send_media(event, img)


@register(pattern="wallpaperg")
async def wallpaper(event):
    target = "wallpaper"
    await send_media(event, (nekos.img(target)))


@register(pattern="tickle")
async def tickle(event):
    target = "tickle"
    await send_media(event, (nekos.img(target)))


@register(pattern="ngif")
async def ngif(event):
    target = "ngif"
    await send_media(event, (nekos.img(target)))


@register(pattern="feed")
async def feed(event):
    target = "feed"
    await send_media(event, (nekos.img(target)))


@register(pattern="gasm")
async def gasm(event):
    target = "gasm"
    await send_media(event, (nekos.img(target)))


@register(pattern="avatar")
async def avatar(event):
    target = "avatar"
    await send_media(event, (nekos.img(target)))


@register(pattern="foxgirl")
async def foxgirl(event):
    target = "fox_girl"
    await send_media(event, (nekos.img(target)))


@register(pattern="gecg")
async def gecg(event):
    target = "gecg"
    await send_media(event, (nekos.img(target)))


@register(pattern="lizard")
async def lizard(event):
    target = "lizard"
    await send_media(event, (nekos.img(target)))


@register(pattern="goose")
async def goose(event):
    target = "goose"
    await send_media(event, (nekos.img(target)))


@register(pattern="woof")
async def woof(event):
    target = "woof"
    await send_media(event, (nekos.img(target)))
