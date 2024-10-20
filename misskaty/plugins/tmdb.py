from pyrogram import Client, filters
import requests
from misskaty import app


TMDB_API_KEY = "23c3b139c6d59ebb608fe6d5b974d888"


@app.on_message(filters.command(["tmdb"]))
async def movie_command(client, message):
    try:
        # Check if the user provided a movie name after the /movie command
        if len(message.command) > 1:
            movie_name = " ".join(message.command[1:])

            # Fetch movie information from TMDb API
            movie_info = get_movie_info(movie_name)

            # Send the movie information as a reply
            await message.reply_text(movie_info)
        else:
            await message.reply_text("Please enter a movie name after the /movie command.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

def get_movie_info(movie_name):
    tmdb_api_url = f"https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": movie_name}
    
    response = requests.get(tmdb_api_url, params=params)
    data = response.json()

    if data.get("results"):
        # Get information about the first movie in the results
        movie = data["results"][0]
        
        # Fetch additional details using the movie ID
        details_url = f"https://api.themoviedb.org/3/movie/{movie['id']}"
        details_params = {"api_key": TMDB_API_KEY}
        details_response = requests.get(details_url, params=details_params)
        details_data = details_response.json()
        
        # Extract relevant information
        title = details_data.get("title", "N/A")
        release_date = details_data.get("release_date", "N/A")
        overview = details_data.get("overview", "N/A")
        providers = details_data.get("providers", "N/A")
        vote_average = details_data.get("vote_average", "N/A")
        
        # Extract actor names
        cast_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits"
        cast_params = {"api_key": TMDB_API_KEY}
        cast_response = requests.get(cast_url, params=cast_params)
        cast_data = cast_response.json()
        actors = ", ".join([actor["name"] for actor in cast_data.get("cast", [])])
        
        # Extract total collection
        revenue = details_data.get("revenue", "N/A")
        
        # Format and return movie information
        info = (
            f"🔖 **Title:** __{title}__\n"
            f"📅 **Release Date:** `{release_date}`\n"
            f"📮 **Vote Average:** `{vote_average}`\n"
            f"📊 **Total Collection:** `{revenue}`\n\n"
            f"📱 **Available Platforms:** __{providers}__\n"
            f"🌀 **Overview:** __{overview}__\n\n"
            f"🕴️ **Actor Names:** __{actors}__\n\n**Powered by**: @XBOTS_X | ©️ @GojoSatoru_Xbot"
        )
        return info
    else:
        return "Movie not found or API request failed."
