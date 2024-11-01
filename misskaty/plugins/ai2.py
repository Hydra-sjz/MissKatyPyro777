from pyrogram import Client, filters, enums
import requests
import urllib.parse
import asyncio
from pyrogram.types import Message
from misskaty import app

# Function to query the AI API
def ask_query(query, model=None):
    default_model = 'gpt-4o'
    system_prompt = """Hey! I'm Gojo x Sotoru."""

    model = model or default_model

    if model == default_model:
        query = f"{system_prompt}\n\nUser: {query}"

    encoded_query = urllib.parse.quote(query)
    url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("result", "No response found.")
    else:
        return f"Error fetching response from API. Status code: {response.status_code}"

# Function to simulate typing action
async def send_typing_action(client: Client, chat_id: int, duration: int = 1):
    """Simulate typing action for a specified duration before sending a response."""
    await client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    await asyncio.sleep(duration)

# Retrieve the model from the database (Stub function, replace with actual implementation)
def get_model_from_db(group_id):
    return 'claude-sonnet-3.5'  # Replace this with actual database retrieval logic

# Handler for the "/ask" command
@app.on_message(filters.command("ask"))
async def handle_querasoy(client, message):
    if len(message.command) < 2:
        await message.reply_text("<b>Please provide a query to ask.</b>")
        return

    user_query = message.text.split(maxsplit=1)[1]
    
    # Get user's mention
    user_mention = message.from_user.mention

    # Simulate typing action before sending the response
    await send_typing_action(client, message.chat.id, duration=2)

    # Fetch the response from the AI API
    response = ask_query(user_query)

    # Send the response back to the user with mention
    await message.reply_text(f"{user_mention}, <b>{response}</b>")

# Handle mentions of the bot in group chats
@app.on_message(filters.mentioned & filters.group)
async def handle_amention(client: Client, message: Message) -> None:
    group_id = message.chat.id

    user_text = None

    # Check if the message is a reply to another message
    if message.reply_to_message and message.reply_to_message.text:
        user_text = message.reply_to_message.text.strip()
    elif len(message.text.split(" ", 1)) > 1:
        user_text = message.text.split(" ", 1)[1].strip()

    if user_text:
        model_name = get_model_from_db(group_id)  # Retrieve the default model

        # Simulate typing action and wait before sending the response
        await send_typing_action(client, group_id)

        api_response = ask_query(user_text, model_name)

        # Reply with the model name in the response
        await message.reply(f"<b>{api_response}</b>")
    else:
        await message.reply("<b>Please ask a question after mentioning me</b>")


#=====================BLACK-BOX=====================≠====
# Function to query the AI API
def ask_query_bb(query, model='blackboxai'):
    try:
        # Encode the query for URL safety
        encoded_query = urllib.parse.quote(query)
        url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

        # Make the request to the API
        response = requests.get(url)
        if response.status_code == 200:
            # Return the result if found, else give a fallback message
            return response.json().get("result", "Sorry, I couldn’t find a response.")
        else:
            return f"⚠️ Error fetching response from the API. Status code: {response.status_code}"
    except Exception as e:
        return f"⚠️ An unexpected error occurred: {e}"

# Handler for the "/blackbox" command
@app.on_message(filters.command("blackbox"))
async def handle_bbquery(client, message):
    # Check if the user provided a query
    if len(message.command) < 2:
        await message.reply_text("<b>📝 Please enter a query to get started.</b>")
        return

    # Retrieve the user's query
    user_query = message.text.split(maxsplit=1)[1]
    user_mention = message.from_user.mention

    # Simulate typing action before sending response
    await send_typing_action(client, message.chat.id, duration=2)

    # Fetch the response from the AI API
    response = ask_query_bb(user_query)

    # Construct the response message with user mention and response
    await message.reply_text(f"{user_mention},<b> {response}</b>")

#===================
def ask_querycs(query, model='claude-sonnet-3.5'):
    try:
        # Encode the query for URL safety
        encoded_query = urllib.parse.quote(query)
        url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

        # Send request to the API
        response = requests.get(url)
        if response.status_code == 200:
            # Return the API result if available, otherwise a fallback message
            return response.json().get("result", "🤔 I'm not sure how to respond to that.")
        else:
            return f"⚠️ Error: Unable to fetch a response from the API. (Status code: {response.status_code})"
    except Exception as e:
        return f"⚠️ An unexpected error occurred - {e}"

# Handler for the "/claude" command
@app.on_message(filters.command("claude"))
async def handle_querygp(client, message):
    # Check if the user provided a query
    if len(message.command) < 2:
        await message.reply_text("💬 <b>Please enter a query to proceed.</b>")
        return

    # Get the user query and mention
    user_query = message.text.split(maxsplit=1)[1]
    user_mention = message.from_user.mention

    # Simulate typing action before sending the response
    await send_typing_action(client, message.chat.id, duration=2)

    # Fetch the response from the AI API
    response = ask_querycs(user_query)

    # Send the formatted response
    await message.reply_text(
        f"{user_mention}, <b>{response}</b>"
    )
#====≠======
def ask_querygm(query, model='gemini-pro'):
    try:
        # Encode the user query for safe URL handling
        encoded_query = urllib.parse.quote(query)
        url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

        # Send the request to the API
        response = requests.get(url)
        if response.status_code == 200:
            # Return the response or a fallback message if no result is found
            return response.json().get("result", "I couldn't find an answer to that.")
        else:
            return f"⚠️ Could not retrieve data from the API. (Status code: {response.status_code})"
    except Exception as e:
        return f"⚠️ An unexpected error occurred: {e}"

# Handler for the "/gemini" command
@app.on_message(filters.command("gemini"))
async def handle_querygp(client, message):
    # Check if a query was provided by the user
    if len(message.command) < 2:
        await message.reply_text("💡 <b>Kindly provide a question to proceed.</b>")
        return

    # Get the user's question and mention
    user_query = message.text.split(maxsplit=1)[1]
    user_mention = message.from_user.mention

    # Simulate typing to enhance the user experience
    await send_typing_action(client, message.chat.id, duration=2)

    # Query the AI API for a response
    response = ask_querygm(user_query)

    # Send the response with user mention
    await message.reply_text(
        f"{user_mention}, <b>{response}</b>"
    )

#=========
def ask_querygpt(query, model='gpt-4o'):
    try:
        # Prepare the query for safe URL encoding
        encoded_query = urllib.parse.quote(query)
        url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

        # Make the API request
        response = requests.get(url)
        if response.status_code == 200:
            # Return the response or a fallback message if no response is found
            return response.json().get("result", "I'm unable to find an answer at the moment.")
        else:
            return f"⚠️ API Error: Could not retrieve data. (Status code: {response.status_code})"
    except Exception as e:
        return f"⚠️ An error occurred: {e}"

# Handler for the "/gpt" command
@app.on_message(filters.command("gpt"))
async def handle_qugptery(client, message):
    # Ensure a query is provided by the user
    if len(message.command) < 2:
        await message.reply_text("💬 <b>Please provide a question to continue.</b>")
        return

    # Extract the user's query and mention
    user_query = message.text.split(maxsplit=1)[1]
    user_mention = message.from_user.mention

    # Simulate typing for better UX
    await send_typing_action(client, message.chat.id, duration=2)

    # Get the AI response for the user query
    response = ask_querygpt(user_query)

    # Reply with the formatted response including user mention
    await message.reply_text(
        f"{user_mention},<b>{response}</b>"
    )

#===========
def ask_querylam(query, model='llama'):
    try:
        # Encode the user query for safe URL handling
        encoded_query = urllib.parse.quote(query)
        url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

        # Make the API request
        response = requests.get(url)
        if response.status_code == 200:
            # Return the result or a fallback message if no response is found
            return response.json().get("result", "🤔 I couldn't find an answer to that.")
        else:
            return f"⚠️ API Error: Unable to retrieve data. (Status code: {response.status_code})"
    except Exception as e:
        return f"⚠️ An error occurred: {e}"

# Handler for the "/llama" command
@app.on_message(filters.command("llama"))
async def handle_querlamay(client, message):
    # Ensure a query is provided by the user
    if len(message.command) < 2:
        await message.reply_text("💬 <b>Please provide a query to ask.</b>")
        return

    # Extract the user's query and mention
    user_query = message.text.split(maxsplit=1)[1]
    user_mention = message.from_user.mention

    # Simulate typing action before sending the response
    await send_typing_action(client, message.chat.id, duration=2)

    # Get the AI response for the user query
    response = ask_querylam(user_query)

    # Reply with the formatted response including user mention
    await message.reply_text(
        f"{user_mention},<b>{response}</b>"
    )
