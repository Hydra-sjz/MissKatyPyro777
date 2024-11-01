from pyrogram import Client, filters
import requests
from misskaty import app
import time
import os

# Generate a detailed prompt for image creation
def generate_long_query(query):
    base_query = f"{query}."
    return base_query

@app.on_message(filters.command("draw"))
async def draw_image(client, message):
    if len(message.command) < 2:
        await message.reply_text("**Please provide a query to generate an image.** 😊")
        return

    # Generate a long query for better image results
    user_query = message.text.split(" ", 1)[1]
    query = generate_long_query(user_query)

    # Send initial message
    wait_message = await message.reply_text("**Generating image, please wait...** ⏳")

    # Generate image URL using the API
    url = f"https://text2img.codesearch.workers.dev/?prompt={query}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_data = response.json()
            image_url = image_data.get("image")
            if image_url:
                # Delete the wait message
                await wait_message.delete()
                # Send the generated image
                await message.reply_photo(photo=image_url, caption=f"🖼️**Generated Image for:** __{user_query}__\n\n📨**Requested by: {message.from_user.mention}**")
            else:
                await wait_message.edit_text("Failed to retrieve image URL. Please try again. ❌")
        else:
            await wait_message.edit_text("Error: Unable to generate image at this time. Please try later. 🚫")
    except Exception as e:
        await wait_message.edit_text(f"An error occurred: {e} ⚠️")

 

# Command handler for /gen
@app.on_message(filters.command(['imagine','generate']))
async def generate_image(client, message):
    # Get the prompt from the command
    prompt = ' '.join(message.command[1:])

    # Send a message to inform the user to wait
    wait_message = await message.reply_text("Please wait while I generate the image...")
    StartTime = time.time()


    # API endpoint URL
    url = 'https://ai-api.magicstudio.com/api/ai-art-generator'

    # Form data for the request
    form_data = {
        'prompt': prompt,
        'output_format': 'bytes',
        'request_timestamp': str(int(time.time())),
        'user_is_subscribed': 'false',
    }

    # Send a POST request to the API
    response = requests.post(url, data=form_data)

    if response.status_code == 200:
        try:
            if response.content:
                destination_dir = ''
                destination_path = os.path.join(destination_dir, 'generated_image.jpg')

                # Save the image to the destination path
                with open(destination_path, 'wb') as f:
                    f.write(response.content)

                # Delete the wait message
                await wait_message.delete()

                # Send the generated image
                await message.reply_photo(destination_path, caption=f"Here's the generated image!\nTime Taken: {time.time() - StartTime}")

                # Delete the generated image after sending
                os.remove(destination_path)
            else:
                await wait_message.edit_text("Failed to generate the image.")
        except Exception as e:
            await wait_message.edit_text("Error: {}".format(e))
    else:
        await wait_message.edit_text("Error: {}".format(response.status_code))
