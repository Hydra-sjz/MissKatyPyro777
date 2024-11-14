from pyrogram import Client, filters
from pyrogram.types import Message

from anime_api.apis import NekosAPI
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tpblite import TPB
from io import BytesIO
import asyncio
import subprocess
import random
import redgifs
import time
import yt_dlp
import os
import subprocess
import requests
from misskaty import app

#YouTube Data API v3 key
api_key = 'AIzaSyDNgFQoa0H4nhTVHRV_hTRibTfdozaNG24'

#Spotify API credentials
client_id = '3897229c442f411d913a41194ce021bd'
client_secret = '36ed57b8e8c54d808e4512f4812c9da6'

#Unsplash API access key
UNSPLASH_ACCESS_KEY = 'uQ2KzkpBUDVFmVvELqwab0v2oW9SXL14T4PmcH97YYs'


#Pexels API key
PEXELS_API_KEY = 'JPP297l85tUiaNFHlojzzgnvCRwwcGacFGOxWl7L9vKTwIrcFWw0ly2t'

api = NekosAPI()
BASE_URL = "https://api.waifu.pics"

ANIME_COMMANDS = [
    "waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss",
    "lick", "pat", "smug", "bonk", "yeet", "blush", "smile", "wave", "highfive", "handhold",
    "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe"
]

# You can use any domain of the piratebay
tpb = TPB('https://tpb.party')

# Replace with your Google Custom Search Engine API key
GAPI_KEY = "AIzaSyDaLXgspHCsn4ihgQ2bUszCJDAA8-_MHo4"

# Replace with your Google Custom Search Engine ID
SEARCH_ENGINE_ID = "17ca9eebfb9084a7e"
BING_ENGINE_ID = "d0bd6decd107344a8"
YANDEX_ENGINE_ID="d2357bba448e6459d"
DDG_ENGINE_ID="261c139e42ea74c5b"
WEB_ENGINE_ID="your-search-engine-id"


#BARD MODULE NOT WORKING FOR MOST CASES

#Enter Any cookie values you want to pass to the session object.
# COOKIE_DICT = {
#     "__Secure-1PSID": "",
#     "__Secure-1PSIDTS": "",
#     "__Secure-1PSIDCC": "",
# }

# bard = BardCookies(cookie_dict=COOKIE_DICT)

KEYWORD = 0
user_states = {}


audio_ydl = yt_dlp.YoutubeDL({
    "format": "bestaudio/best",
    "outtmpl": "%(title)s.mp3",
    "extract_flat": True,
    "youtube_api_key": api_key,
    "noplaylist": False
})


video_ydl = yt_dlp.YoutubeDL({
    "format": "best",
    "outtmpl": "%(title)s.%(ext)s",
    "allow_playlist_files": True
})


def send_message(chat_id, message):
    message.reply_text(chat_id, message)


def send_upload_progress(chat_id, message_id):
    async def callback(current, total):
        progress = (current / total) * 100
        await app.edit_message_text(chat_id, message_id, text=f"File Upload Progress: {progress:.2f}%")

    return callback


# Not used but kept here for future purposes
def convert_to_mp3(filename,chat_id):
    if filename.endswith('.mp3'):
        return filename

    output_filename = f"{os.path.splitext(filename)[0]}.mp3"
    subprocess.run(['ffmpeg', '-i', filename, '-codec:a', 'libmp3lame', '-q:a', '2', output_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if os.path.exists(output_filename):
        send_message(chat_id, "Audio conversion finished!")
        return output_filename
    else:
        return None


def search_youtube(query):
    results = audio_ydl.extract_info(f"ytsearch5:{query}", download=False)
    return results.get("entries", [])


def get_random_image(category, image_type):
    url = f"{BASE_URL}/{image_type}/{category}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "url" in data:
            return data["url"]
        elif "files" in data and len(data["files"]) > 0:
            return data["files"][0]
    return None


def fetch_image(category, image_type):
    image_url = get_random_image(category, image_type)
    return image_url


def extract_youtube_music_url(output):
    lines = output.split('\n')  
    youtube_music_url = None

    for line in lines:
        if line.startswith('Downloaded') and 'music.youtube.com' in line:
            parts = line.split(': ')
            if len(parts) > 1:
                youtube_music_url = parts[-1].strip()  
                break

    return youtube_music_url
    
async def send_status(chat_id, message):
    await message.reply_text(chat_id, message)
    
def download_audio(url):
    reply_text("Audio download started...")
    with audio_ydl as ydl:
        info = ydl.extract_info(url)
        filename = ydl.prepare_filename(info)
        reply_text("Audio download finished!")
        return filename


def download_video(url,chat_id):
    send_message(chat_id, "Video download started...")
    with video_ydl as ydl:
        info = ydl.extract_info(url)
        filename = ydl.prepare_filename(info)
        send_message(chat_id, "Video download finished!")
        return filename
#========================


#=============°===
@app.on_message(filters.command("ytsearch2"))
async def search_hhcommand(client, message):
    try:
        query = message.text.split(" ", 1)[1]
        results = search_youtube(query)

        for idx, result in enumerate(results, start=1):
            title = result.get("title")
            url = result.get("url")  
            if url:  
                await message.reply_text(f"{idx}. {title}\n{url}\n\n**Powered by**: @XBOTS_X | ©️ @GojoSatoru_Xbot")
            else:
                await message.reply_text(f"{idx}. {title}\nURL not found")

    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")
        
       
@app.on_message(filters.command("audio"))
async def song_command(client, message):
    try:
        #chat_id = message.chat.id
        await message.reply_text("Searching for the song...")
        query = message.text.split(" ", 1)[1]
        results = search_youtube(query)

        if results:
            top_result = results[0]
            audio_url = top_result["url"]

            try:
                await message.reply_text("Song Found! Starting download...")
                filename = download_audio(audio_url)

                if filename:
                    # await send_status(chat_id, "Download complete. Converting to MP3...")

                    # mp3_filename = convert_to_mp3(filename,chat_id)

                    # if mp3_filename:
                    #chat_id = message.chat.id
                    await message.text("Uploading audio...")

                    await message.audio(filename)

                    await message.reply_text("Audio upload finished!")
                    os.remove(filename)
                        # os.remove(mp3_filename)
                    # else:
                    #     await send_status(chat_id, "Error: Unsupported file format")
                else:
                    await message.reply_text("Error: Unsupported file format")
            except Exception as e:
                await message.reply_text(f"Error: {str(e)}")
        else:
            await message.reply_text("No results found for the provided query.")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")



@app.on_message(filters.command("spotdl"))
async def spotdl_command(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a Spotify or YouTube link.")
            return

        await message.message.reply_text("Downloading...")

        process = subprocess.Popen(
            f"python -m spotdl {query}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output, error = process.communicate()

        if error:
            await message.reply_text(f"Error: {error}")
        else:
            file_name = ""
            for filename in os.listdir("."):
                if filename.endswith(".mp3"):
                    file_name = filename
                    break

            if file_name:
                await message.reply_text("Download Finished!, Uploading...")
                with open(file_name, "rb") as file:
                    await message.reply_audio(file)
                os.remove(file_name)  # Delete the file after sending
                await message.reply_text("Downloaded and sent!")

    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")


@app.on_message(filters.command("spotify"))
async def spotify_search(client, message):
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query for Spotify.")
            return

        await message.reply_text("Searching on Spotify...")

        
        results = sp.search(q=query, limit=10)  

        if results:
            await message.reply_text("Search Results from Spotify:")
            for idx, item in enumerate(results['tracks']['items'], start=1):
                await message.reply_text(
                    f"{idx}. **Name**: `{item['name']}`\n **Artists**: `{', '.join([artist['name'] for artist in item['artists']])}`\n**Album**: `{item['album']['name']}`\n**URL**: {item['external_urls']['spotify']}"
                )
        else:
            await message.reply_text("No results found on Spotify.")
    except Exception as e:
        await message.reply_text(f'An error occurred: {str(e)}')



@app.on_message(filters.command("quote2"))
async def get_rahndom_quote(client, message):
    try:
        response = requests.get("https://animechan.xyz/api/random")
        if response.status_code == 200:
            quote = response.json()
            formatted_quote = f"**Anime**: `{quote['anime']}`\n**Character**: `{quote['character']}`\n**Quote**: __\"{quote['quote']}\"__"
            await message.reply_text(formatted_quote)
        else:
            await message.reply_text("Failed to fetch a quote. Try again later.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")



@app.on_message(filters.command("mquote"))
async def get_many_quotes(client, message):
    try:
        response = requests.get("https://animechan.xyz/api/quotes")
        if response.status_code == 200:
            quotes = response.json()
            formatted_quotes = "\n\n".join([f"**Anime**: `{quote['anime']}`\n**Character**: `{quote['character']}`\n**Quote**: __\"{quote['quote']}\"__" for quote in quotes])
            await message.reply_text(formatted_quotes)
        else:
            await message.reply_text("Failed to fetch quotes. Try again later.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
        


#@app.on_message(filters.command(ANIME_COMMANDS))
def image_fetch_handler(client, message):
    command = message.command[0]
    image_url = fetch_image(command, "sfw") 
    if image_url:
        client.reply_photo(photo=image_url)
    else:
        client.reply_text("Failed to fetch the image.")




@app.on_message(filters.command("cat2"))
async def catgirl_command(client, message):
    try:
        
        image = api.get_random_image(categories=["catgirl"])

        await message.reply_photo(image.url)
    except Exception as e:
        await message.reply_text(f'An error occurred: {str(e)}')


@app.on_message(filters.command("meme"))
async def handle_meme_command(client, message):
    api_url = "https://meme-api.com/gimme"

    response = requests.get(api_url)
    await message.reply_text("Downloading...")
    if response.status_code == 200:
        meme_data = response.json()

        title = meme_data['title']
        meme_url = meme_data['url']

        meme_file = requests.get(meme_url)

        if meme_file.status_code == 200:
            file_extension = meme_url.split('.')[-1]
            file_name = f"{title}.{file_extension}"

            with open(file_name, 'wb') as file:
                file.write(meme_file.content)

            # send_message(message.chat.id, "Uploading meme...")
            if file_extension in ['png', 'jpg', 'gif']:
                await message.reply_photo(file_name, caption=title)
            elif file_extension in ['mp4', 'gifv']:
                await message.reply_video(file_name, caption=title)
                await message.reply_text("Meme upload finished!")

            os.remove(file_name)

        else:
            await reply_text("Failed to download the meme.")
    else:
        await reply_text("Failed to fetch the meme from the API.")

@app.on_message(filters.command("mormeme"))
async def handle_many_meme_command(client, message):

    api_url = "https://meme-api.com/gimme/5"

    response = requests.get(api_url)
    await message.reply_text("Downloading...")
    if response.status_code == 200:
        memes_data = response.json()

        memes_list = memes_data['memes']

        for meme in memes_list:
            title = meme['title']
            meme_url = meme['url']

  
            meme_file = requests.get(meme_url)

            if meme_file.status_code == 200:
                
                file_extension = meme_url.split('.')[-1]
                file_name = f"{title}.{file_extension}"

                with open(file_name, 'wb') as file:
                    file.write(meme_file.content)

                # send_message(message.chat.id, "Uploading meme...")
                if file_extension in ['png', 'jpg', 'gif']:
                    await message.reply_photo(file_name, caption=title)
                elif file_extension in ['mp4', 'gifv']:
                    await message.reply_video(file_name, caption=title)
                    await message.reply_text("Meme upload finished!")
                os.remove(file_name)

            else:
                await message.reply_text(f"Failed to download the meme '{title}'.")

    else:
        await message.reply_text("Failed to fetch memes from the API.")



@app.on_message(filters.command("reddit"))
async def handle_reddit_command(client, message):
    await message.reply_text("Downloading...")
    # Specify any subreddits of your choice
    subreddits = ["wholesomememes", "memes", "funny", "aww"] 


    selected_subreddit = random.choice(subreddits)

    api_url = f"https://meme-api.com/gimme/{selected_subreddit}"

    response = requests.get(api_url)
    
    if response.status_code == 200:
        meme_data = response.json()

        title = meme_data['title']
        meme_url = meme_data['url']

        meme_file = requests.get(meme_url)

        if meme_file.status_code == 200:
            file_extension = meme_url.split('.')[-1]
            file_name = f"{title}.{file_extension}"

            with open(file_name, 'wb') as file:
                file.write(meme_file.content)

            # send_message(message.chat.id, "Uploading meme...")
            if file_extension in ['png', 'jpg', 'gif']:
                await message.reply_photo(file_name, caption=title)
            elif file_extension in ['mp4', 'gifv']:
                await message.reply_video(file_name, caption=title)
                await message.reply_text("upload finished!")

            os.remove(file_name)

        else:
            await message.reply_text("Failed to download the meme.")
    else:
        await message.reply_text("Failed to fetch the meme from the API.")

@app.on_message(filters.command("morddit"))
async def handle_multiple_reddit_command(client, message):
    # Specify any subreddits you want
    subreddits = ["wholesomememes", "memes", "funny", "aww"]  

    memes_to_fetch = 5 #change according to your needs

    all_memes = []
    await message.reply_text("Downloading...")
    for _ in range(memes_to_fetch):

        selected_subreddit = random.choice(subreddits)
        api_url = f"https://meme-api.com/gimme/{selected_subreddit}"

        response = requests.get(api_url)

        if response.status_code == 200:
            meme_data = response.json()
            all_memes.append(meme_data)
        else:
            await message.reply_text(f"Failed to fetch meme from {selected_subreddit}.")

    for meme_data in all_memes:
        title = meme_data['title']
        meme_url = meme_data['url']

        meme_file = requests.get(meme_url)

        if meme_file.status_code == 200:
            file_extension = meme_url.split('.')[-1]
            file_name = f"{title}.{file_extension}"

            with open(file_name, 'wb') as file:
                file.write(meme_file.content)

            # send_message(message.chat.id, "Uploading meme...")
            if file_extension in ['png', 'jpg', 'gif']:
                await message.reply_photo(file_name, caption=title)
            elif file_extension in ['mp4', 'gifv']:
                await message.reply_video(file_name, caption=title)
                await message.reply_text("upload finished!")

            os.remove(file_name)

        else:
            await message.reply_text("Failed to download the meme.")




@app.on_message(filters.command("unsplash"))
async def unsplash_command(client, message):
    try:
        query = " ".join(message.command[1:])
        if query:
            response = requests.get(f'https://api.unsplash.com/search/photos?query={query}&client_id={UNSPLASH_ACCESS_KEY}')
            data = response.json()

            if 'results' in data:
                await message.reply_text("Searching for images...")
                photos = data['results']
                if photos:
                    await message.reply_text("Images found!, Uploading...")
                    for index, photo in enumerate(photos[:10], start=1):  # Send the first 5 images
                        image_url = photo['urls']['regular']
                        image_file = requests.get(image_url)
                        if image_file.status_code == 200:

                            await message.reply_photo(image_url)
                        else:
                            await message.reply_text("Failed to fetch image.")
                else:
                    await message.reply_text("Can't find images for that keyword.")
            else:
                await message.reply_text("Failed to get images.")
        else:
            await message.reply_text("Please provide a keyword to search for images.")

    except Exception as e:
        await message.reply_text(f'An error occurred: {str(e)}')
        
        

@app.on_message(filters.command("pexi"))
async def ipex_command(client, message):
    try:
        keyword = " ".join(message.command[1:])
        if keyword:
            headers = {
                'Authorization': PEXELS_API_KEY,
            }
            params = {
                'query': keyword,
                'per_page': 5,
            }
            await message.reply_text("Fetching Images...")
            response = requests.get('https://api.pexels.com/v1/search', headers=headers, params=params)
            data = response.json()
            photos = data.get('photos')
            if photos:
                await message.reply_text("Images Found!, Uploading...")
                for photo in photos:
                    image_url = photo['src']['medium']
                    await message.reply_photo(image_url)
            else:
                await message.reply_text("No images found for the keyword.")
        else:
            await message.reply_text("Please provide a keyword to search for images.")
    except Exception as e:
        await message.reply_text(f'An error occurred: {str(e)}')



@app.on_message(filters.command("pexv"))
async def vpex_command(client, message):
    try:
        keyword = " ".join(message.command[1:])
        if keyword:
            headers = {
                'Authorization': PEXELS_API_KEY,
            }
            params = {
                'query': keyword,
                'per_page': 5,
            }
            await message.reply_text("Fetching Videos...")
            response = requests.get('https://api.pexels.com/videos/search', headers=headers, params=params)
            data = response.json()
            videos = data.get('videos')
            if videos:
                await message.reply_text("Videos Found!, Uploading...")
                for video in videos:
                    video_url = video['video_files'][0]['link']
                    await message.reply_video(video_url)
            else:
                await message.reply_text("No videos found for the keyword.")
        else:
            await message.reply_text("Please provide a keyword to search for videos.")
    except Exception as e:
        await message.reply_text(f'An error occurred: {str(e)}')        



@app.on_message(filters.command("tor"))
async def pirate_bay_command(client, message):
    try:
        search_query = " ".join(message.command[1:])
        if search_query:
            await message.reply_text("Searching for torrents...")
            torrents = tpb.search(search_query)

            if torrents:
                await message.reply_text(f"Found {len(torrents)} torrents:")
                for torrent in torrents:
                    magnet_link = torrent.magnetlink  # Retrieve magnet link
                    info = (
                        f"**Title**: {torrent.title}\n"
                        f"**Uploader**: {torrent.uploader}\n"
                        f"**Category**: {torrent.category}\n"
                        f"**Seeders**: {torrent.seeds}\n"
                        f"**Leechers**: {torrent.leeches}\n"
                        f"**Upload Date**: {torrent.upload_date}\n"
                        f"**Filesize**: {torrent.filesize}\n"
                        f"**Magnet Link**: `{magnet_link}`\n"  # Send magnet link
                    )
                    await message.reply_text(info)
            else:
                await message.reply_text("No torrents found for the keyword.")
        else:
            await message.reply_text("Please provide a keyword to search for torrents.")
    except Exception as e:
        await message.reply_text(f'An error occurred: {str(e)}')




@app.on_message(filters.command("clone"))
async def clone_repo(client, message):
    try:
        
        url = " ".join(message.command[1:])
        

        if not url:
            await message.reply("Please provide a valid GitHub repository URL.")
            return

        
        zip_url = f"{url.rstrip('/')}/archive/refs/heads/main.zip"  # Assuming 'main' branch, adjust as needed
        

        response = requests.get(zip_url)
        
        if response.status_code == 200:
            
            await message.reply_document(document=response.content, file_name="repository.zip")
            await message.reply("Repository zip file sent!")
        else:
            await message.reply("Failed to fetch the repository zip file.")
            
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
        
        
        

@app.on_message(filters.command("repo"))
async def search_github_repos(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query for repositories.")
            return

        await message.reply_text("Searching for GitHub repositories...")

        # GitHub API search request
        response = requests.get(f"https://api.github.com/search/repositories?q={query}&per_page=10")
        if response.status_code == 200:
            data = response.json()
            repos = data.get('items', [])

            if repos:
                await message.reply_text("Top 10 GitHub Repositories:")
                for index, repo in enumerate(repos[:10], start=1):
                    repo_name = repo.get('full_name')
                    stars = repo.get('stargazers_count')
                    forks = repo.get('forks_count')
                    repo_url = repo.get('html_url')

                    await message.reply_text(f"{index}.  **Name**: `{repo_name}`\n **Stars**: `{stars}`\n**Forks**: `{forks}`\n**URL**: {repo_url}")
                    
            else:
                await message.reply_text("No repositories found for the query.")
        else:
            await message.reply_text("Failed to fetch repositories.")
    except Exception as e:
        await message.reply_text(f'An error occurred: {str(e)}')




@app.on_message(filters.command("google"))
async def google_search(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query.")
            return

        await message.reply_text("Searching on Google...")

        response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={GAPI_KEY}&cx={SEARCH_ENGINE_ID}&q={query}")
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            if items:
                await message.reply_text("Top search results:")
                for index, item in enumerate(items[:10], start=1):
                    title = f"[{item.get('title')}]({item.get('link')})"
                    snippet = item.get('snippet')


                    await message.reply_text(
                        f"{index}. {title}\n\n{snippet}",
                        disable_web_page_preview=False
                    )
            else:
                await message.reply_text("No search results found.")
        else:
            await message.reply_text("Failed to fetch search results.")
            
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
        
        

@app.on_message(filters.command("bingt"))
async def bing_sfearch(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query.")
            return

        await message.reply_text("Searching on Bing...")

        response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={GAPI_KEY}&cx={BING_ENGINE_ID}&q={query}")
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            if items:
                await message.reply_text("Top search results:")
                for index, item in enumerate(items[:10], start=1):
                    title = f"[{item.get('title')}]({item.get('link')})"
                    snippet = item.get('snippet')

                    await message.reply_text(
                        f"{index}. {title}\n\n{snippet}",
                        disable_web_page_preview=False
                    )
            else:
                await message.reply_text("No search results found.")
        else:
            await message.reply_text("Failed to fetch search results.")
            
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
        
        
        
@app.on_message(filters.command("yandex"))
async def yandex_search(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query.")
            return

        await message.reply_text("Searching on Yandex...")

        response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={GAPI_KEY}&cx={YANDEX_ENGINE_ID}&q={query}")
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            if items:
                await message.reply_text("Top search results:")
                for index, item in enumerate(items[:10], start=1):
                    title = f"[{item.get('title')}]({item.get('link')})"
                    snippet = item.get('snippet')

                    await message.reply_text(
                        f"{index}. {title}\n\n{snippet}",
                        disable_web_page_preview=False
                    )
            else:
                await message.reply_text("No search results found.")
        else:
            await message.reply_text("Failed to fetch search results.")
            
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")


@app.on_message(filters.command("ddg"))
async def ddg_search(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query.")
            return

        await message.reply_text("Searching on DuckDuckGo...")

        response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={GAPI_KEY}&cx={DDG_ENGINE_ID}&q={query}")
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            if items:
                await message.reply_text("Top search results:")
                for index, item in enumerate(items[:10], start=1):
                    title = f"[{item.get('title')}]({item.get('link')})"
                    snippet = item.get('snippet')

                    await message.reply_text(
                        f"{index}. {title}\n\n{snippet}",
                        disable_web_page_preview=False
                    )
            else:
                await message.reply_text("No search results found.")
        else:
            await message.reply_text("Failed to fetch search results.")
            
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

        

@app.on_message(filters.command("web"))
async def web_searcfh(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query.")
            return

        await message.reply_text("Searching the web...")

        response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={GAPI_KEY}&cx={WEB_ENGINE_ID}&q={query}")
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            if items:
                await message.reply_text("Top search results:")
                for index, item in enumerate(items[:10], start=1):
                    title = f"[{item.get('title')}]({item.get('link')})"
                    snippet = item.get('snippet')

                    await message.reply_text(
                        f"{index}. {title}\n\n{snippet}",
                        disable_web_page_preview=False
                    )
            else:
                await message.reply_text("No search results found.")
        else:
            await message.reply_text("Failed to fetch search results.")
            
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")



        
        
@app.on_message(filters.command("webimg"))
async def image_search(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query for images.")
            return

        await message.reply_text("Searching for images...")

        response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={GAPI_KEY}&cx={WEB_ENGINE_ID}&q={query}&searchType=image&num=10")
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            if items:
                await message.reply_text("Top 10 image results:")
                for index, item in enumerate(items[:10], start=1):
                    image_url = item.get('link')

                    await message.reply_photo(image_url)
            else:
                await message.reply_text("No image results found.")
        else:
            await message.reply_text("Failed to fetch image results.")
            
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")


        
        
@app.on_message(filters.command("ggimg"))
async def image_search2(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query for images.")
            return

        await message.reply_text("Searching for images...")

        response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={GAPI_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&searchType=image&num=10")
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            if items:
                await message.reply_text("Top 10 image results:")
                for index, item in enumerate(items[:10], start=1):
                    image_url = item.get('link')

                    await message.reply_photo(image_url)
            else:
                await message.reply_text("No image results found.")
        else:
            await message.reply_text("Failed to fetch image results.")
            
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
        
        
        
        
@app.on_message(filters.command("bingimg"))
async def image_search3(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query for images.")
            return

        await message.reply_text("Searching for images...")

        response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={GAPI_KEY}&cx={BING_ENGINE_ID}&q={query}&searchType=image&num=10")
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            if items:
                await message.reply_text("Top 10 image results:")
                for index, item in enumerate(items[:10], start=1):
                    image_url = item.get('link')

                    await message.reply_photo(image_url)
            else:
                await message.reply_text("No image results found.")
        else:
            await message.reply_text("Failed to fetch image results.")
            
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")


        
        
@app.on_message(filters.command("yandeximg"))
async def image_search4(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query for images.")
            return

        await message.reply_text("Searching for images...")

        response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={GAPI_KEY}&cx={YANDEX_ENGINE_ID}&q={query}&searchType=image&num=10")
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            if items:
                await message.reply_text("Top 10 image results:")
                for index, item in enumerate(items[:10], start=1):
                    image_url = item.get('link')

                    await message.reply_photo(image_url)
            else:
                await message.reply_text("No image results found.")
        else:
            await message.reply_text("Failed to fetch image results.")
            
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")


        
        
@app.on_message(filters.command("ddgimg"))
async def image_search5(client, message):
    try:
        query = " ".join(message.command[1:])
        if not query:
            await message.reply("Please provide a search query for images.")
            return

        await message.reply_text("Searching for images...")

        response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={GAPI_KEY}&cx={DDG_ENGINE_ID}&q={query}&searchType=image&num=10")
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            if items:
                await message.reply_text("Top 10 image results:")
                for index, item in enumerate(items[:10], start=1):
                    image_url = item.get('link')

                    await message.reply_photo(image_url)
            else:
                await message.reply_text("No image results found.")
        else:
            await message.reply_text("Failed to fetch image results.")
            
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")


        

# Handler for /bard command
# @app.on_message(filters.command("bard"))
# async def bard_command(client, message):

#     try:
#         query = " ".join(message.command[1:])
#         if query:
#             await app.send_message(message.chat.id, "Creating Response...")
#             # Use Bard API to get an answer based on the user's query
#             answer = bard.get_answer(query)['content']
#             await app.send_message(message.chat.id, answer)
#         else:
#             await app.send_message(message.chat.id, "Please provide a query to get an answer.")
#     except Exception as e:
#         await app.send_message(message.chat.id, f'An error occurred: {str(e)}')
