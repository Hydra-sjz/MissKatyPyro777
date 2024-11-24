import urllib.parse
from requests import get
from lyricsgenius import Genius
from telethon import Button
from bs4 import BeautifulSoup

from misskaty.custom_filter import register, callbackquery

from misskaty.ultis_ex.wmilia_m.decorators import *
from misskaty.custom_filter import register


token = "_n604o_cEemM85tf6W0LkzVVItj8kjCijqKc4b1nlT96lX2evhoqHz6E4FX3MGhf"
genius = Genius(token)

@usage("/lyrics [song name]")
@description("Get lyrics of a song.")
@example("/lyrics Believer")
@register(pattern="lyrics|lyric")
@exception
async def lyrics(event):
    song = event.text.split(None, 1)[1]
    if not song:
        return await usage_string(event, lyrics)
    songed = genius.search_songs(song)
    buttons = []
    for songs in songed['hits'][:10]:
        try:
            artist = songs['result']['artist_names']
            title = songs['result']['title']
            url = songs['result']['url']
            if url:
                url = url.replace("https://genius.com/", "")
            b = [Button.inline(f"{title} by {artist}", data=f"m_{title}_{artist}_{url}")]
            buttons.append(b)
        except Exception as e:
            LOGGER.error(e)
            continue
    try:
        await event.reply("Choose the song you want to get the lyrics of", buttons=buttons)
    except Exception as e:
        LOGGER.error(e)
        await get_lyrics(event, song, None, None)

@callbackquery(pattern="m_(.*)_(.*)")
async def mlyrics(event):
    title, artist, url = str(event.data).split("_")[1:4]
    url = "https://genius.com/" + url
    await event.delete()
    await get_lyrics(event, title, artist, url)

async def get_lyrics(event, tit, art, url):
    wait = await event.reply("Please wait while bot is searching for the lyrics :3")
    t = tit.replace(" ", "%20")
    a = art.replace(" ", "%20") if art else "song"
    google_url = f"https://google.com/search?q={t}+{a}+lyrics"
    google_button = Button.url("Read Here", google_url)

    search_results = []
    lyrics = await extract_lyrics(url) if url else None
    if lyrics:
        search_results.append(f"**{tit}**\n**By {art}**\n\n`{lyrics}`")
        img = None
    else:
        search_url = f"https://api.safone.dev/lyrics?title={tit}&artist={art}"
        results = get(search_url).json()
        title, artist, lyrics, img = (
            results.get("title", ""),
            results.get("artist", ""),
            results.get("lyrics", ""),
            results.get("thumbnail", ""),
        )

        if lyrics:
            search_results.append(f"**{title}**\n**By {artist}**\n\n`{lyrics}`")

    meow = f"**Lyrics of {tit} on the internet:**\n\n" + "\n\n".join(search_results)

    try:
        if img:
            await event.reply(meow, buttons=[google_button], link_preview=False, file=img)
        else:
            await event.reply(meow, buttons=[google_button], link_preview=False)
    except (errors.MediaCaptionTooLongError, errors.FileContentTypeInvalidError, TypeError) as e:
        LOGGER.error(e)
        await event.reply(meow, buttons=[google_button], link_preview=False)
    except (errors.ChatWriteForbiddenError, errors.ButtonUrlInvalidError) as e:
        LOGGER.error(e)
        await event.reply(meow, link_preview=False)
    finally:
        await wait.delete()

async def extract_lyrics(url: str) -> str:
    try:
        r = get(url)
        if r.status_code != 200:
            return None
        else:
            soup = BeautifulSoup(r.content, "html.parser")
            list_html_lyrics = soup.find_all("div", class_="Lyrics__Container-sc-1ynbvzw-1 kUgSbL")
            list_generator = [lyric.stripped_strings for lyric in list_html_lyrics]
            all_lyrics = [" ".join(generator) for generator in list_generator]
            all_lyrics = "\n".join(all_lyrics)
            return all_lyrics
    except Exception as e:
        LOGGER.error(e)
        return None
