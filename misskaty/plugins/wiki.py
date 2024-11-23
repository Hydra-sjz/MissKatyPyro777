# DONE: Wikipedia

import aiohttp
import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

from misskaty import tle as meow
from misskaty.custom_filter import register
from misskaty.ultis_ex.wmilia_m.decorators import *


class AsyncWikipedia:
    def __init__(self, title):
        self.title = title

    def summary(self):
        try:
            page = wikipedia.page(self.title)
            return page.summary
        except DisambiguationError as e:
            raise e
        except PageError as e:
            raise e


async def get_wikipedia_summary(search):
    wiki = AsyncWikipedia(search)
    summary = wiki.summary()
    return summary


@register(pattern="wiki")
@rate_limit(40, 60)
async def wiki(event):
    if event.is_reply:
        search_query = (await event.get_reply_message()).text.strip()
    else:
        input_args = event.text.split(None, 1)
        if len(input_args) < 2:
            await event.reply("Provide some query to search!")
            return
        search_query = input_args[1].strip()

    try:
        async with aiohttp.ClientSession() as session:
            wikipedia.set_lang("en")
            wikipedia.set_rate_limiting(True)
            AsyncWikipedia.session = session
            summary = await get_wikipedia_summary(search_query)
            result = f"<b>{search_query}</b>\n\n"
            result += f"<i>{summary}</i>\n"
            result += f"""<a href="https://en.wikipedia.org/wiki/{search_query.replace(" ", "%20")}">Read more...</a>"""
    except DisambiguationError as e:
        result = (
            f"Disambiguated pages found! Adjust your query accordingly.\n\n<i>{e}</i>"
        )
    except PageError as e:
        result = f"<code>{e}</code>"
    except Exception as e:
        print(f"Error: {e}")
        result = "An error occurred while processing your request."

    if len(result) > 4000:
        with open("result.txt", "w") as f:
            f.write(f"{result}\n\nUwU OwO OmO UmU")
        with open("result.txt", "rb") as f:
            await meow.send_file(
                event.chat_id,
                file=f,
                file_name=f.name,
                parse_mode="html",
                force_document=True,
            )
    else:
        await event.reply(result, parse_mode="html", link_preview=False)
