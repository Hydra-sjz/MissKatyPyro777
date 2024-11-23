import httpx
from pyrogram import Client, filters 
from pyrogram.types import Message

from misskaty import app as Abishnoi

timeout = httpx.Timeout(40, pool=None)

http = httpx.AsyncClient(http2=True, timeout=timeout)


# Api key used in weather.com's mobivle app.
weather_apikey = "8de2d8b3a93542c9a2d8b3a935a2c909"

get_coords = "https://api.weather.com/v3/location/search"
url = "https://api.weather.com/v3/aggcommon/v3-wx-observations-current"

headers = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; M2012K11AG Build/SQ1D.211205.017)"
}


@Abishnoi.on_message(filters.command("weather"))
async def weather(c: Client, m: Message):
    if len(m.command) == 1:
        return await m.reply_text(
            "<b>ᴜsᴀɢᴇ:</b> <code>/weather location ᴏʀ city</code> - ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴛʜᴇ ᴡᴇᴀᴛʜᴇʀ ɪɴ <i>ʟᴏᴄᴀᴛɪᴏɴ ᴏʀ ᴄɪᴛʏ</i>"
        )

    r = await http.get(
        get_coords,
        headers=headers,
        params=dict(
            apiKey=weather_apikey,
            format="json",
            language="en",
            query=m.text.split(maxsplit=1)[1],
        ),
    )
    loc_json = r.json()

    if not loc_json.get("location"):
        await m.reply_text("🥏 Location not found...")
    else:
        pos = f"{loc_json['location']['latitude'][0]},{loc_json['location']['longitude'][0]}"
        r = await http.get(
            url,
            headers=headers,
            params=dict(
                apiKey=weather_apikey,
                format="json",
                language="en",
                geocode=pos,
                units="m",
            ),
        )
        res_json = r.json()

        obs_dict = res_json["v3-wx-observations-current"]

        res = "🗺️ <b>{location}</b>:\n\n🌡️<b>Temperature</b> : <code>{temperature} °C</code>\n🧨<b>Temperature Feels like</b> : <code>{feels_like} °C</code>\n🍃 <b>Air Humidity</b> : <code>{air_humidity}%</code>\n🌬️ <b>Wind Speed</b>: <code>{wind_speed} km/h</code>\n\n- <i>{overview}</i>".format(
            location=loc_json["location"]["address"][0],
            temperature=obs_dict["temperature"],
            feels_like=obs_dict["temperatureFeelsLike"],
            air_humidity=obs_dict["relativeHumidity"],
            wind_speed=obs_dict["windSpeed"],
            overview=obs_dict["wxPhraseLong"],
        )

        await m.reply_text(res)
