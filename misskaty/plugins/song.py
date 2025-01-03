import os
import requests
from pyrogram import Client, filters
from misskaty import app

def fetch_song(song_name):
    url = f"https://song-teleservice.vercel.app/song?songName={song_name.replace(' ', '%20')}"
    try:
        response = requests.get(url)
        return response.json() if response.status_code == 200 and "downloadLink" in response.json() else None
    except Exception as e:
        print(f"API Error: {e}")
        return None

@app.on_message(filters.command(["song", "s"]))
async def handle_song(client, message):
    song_name = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    if not song_name:
        return await message.reply("try like this [/song name]")

    song_info = fetch_song(song_name)
    if not song_info:
        return await message.reply(f"sorry I cant find **{song_name}** somg.")

    filename = f"{song_info['trackName']}.mp3"
    download_url = song_info['downloadLink']

    # Download and save the file
    with requests.get(download_url, stream=True) as r, open(filename, "wb") as file:
        for chunk in r.iter_content(1024):
            if chunk:
                file.write(chunk)

    caption = (f"""__{song_info['trackName']}/{song_info['album']} Released on {song_info['releaseDate']}__\n\n**Uploaded by:** @GojoSatoru_Xbot\n©️ @XBOTS_X""")

    # Send audio and clean up
    await message.reply_audio(audio=open(filename, "rb"), caption=caption)
    os.remove(filename)
