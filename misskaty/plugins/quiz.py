import random
import requests
import asyncio
from pyrogram import filters
from pyrogram.enums import PollType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from misskaty import app

# Track quiz loops and active polls per user
quiz_loops = {}
active_polls = {}  # To track active poll messages for each user

# Function to fetch a quiz question from the API
async def fetch_quiz_question():
    categories = [9, 17, 18, 20, 21, 27]  # Quiz categories
    url = f"https://opentdb.com/api.php?amount=1&category={random.choice(categories)}&type=multiple"
    response = requests.get(url).json()

    question_data = response["results"][0]
    question = question_data["question"]
    correct_answer = question_data["correct_answer"]
    incorrect_answers = question_data["incorrect_answers"]

    all_answers = incorrect_answers + [correct_answer]
    random.shuffle(all_answers)

    cid = all_answers.index(correct_answer)

    return question, all_answers, cid

# Function to send a quiz poll with an open_period for countdown
async def send_quiz_poll(client, chat_id, user_id, interval):
    # Fetch quiz question
    question, all_answers, cid = await fetch_quiz_question()

    # Delete the previous active poll if it exists
    if user_id in active_polls:
        try:
            await app.delete_messages(chat_id=chat_id, message_ids=active_polls[user_id])
        except Exception as e:
            print(f"Failed to delete previous poll: {e}")

    # Send new quiz poll with a countdown using open_period
    poll_message = await app.send_poll(
        chat_id=chat_id,
        question=question,
        options=all_answers,
        is_anonymous=False,
        type=PollType.QUIZ,
        #allows_multiple_answers=True,  # Allow multiple answers
        correct_option_id=cid,
        open_period=interval  # Countdown timer for the poll in seconds
    )

    # Store the message ID of the new poll
    if poll_message:
        active_polls[user_id] = poll_message.id  # Corrected to use `.id`

@app.on_message(filters.command(["quiz", "uiz"], prefixes=["/", "!", ".", "Q", "q"]))
async def quiz_info(client, message):
    user_id = message.from_user.id

    # Send the informational message
    await message.reply_text(
        "<b>Welcome to the Quiz Bot! </b>\n\n"
        "Here is how it works:\n"
        "1. Use `/quizon` to start a quiz loop. After you start, you will be asked to choose a time interval for the quiz.\n"
        "2. The available intervals are:\n"
        "   - 30 seconds\n"
        "   - 1 minute\n"
        "   - 5 minutes\n"
        "   - 10 minutes\n"
        "3. Once you choose an interval, the quiz will start, and you will get a new question at the chosen interval. Each quiz will automatically close after a specific time.\n"
        "4. Use `/quiz off` to stop the quiz loop at any time.\n\n"
        "**Commands**:\n"
        "• `/quizon` - Start the quiz loop\n"
        "• `/quizoff` - Stop the quiz loop\n\n"
        "Enjoy the quizzes! 🎉"
    )

# /quiz on command to show time interval options
@app.on_message(filters.command(["quizon", "uizon"], prefixes=["/", "!", ".", "Q", "q"]))
async def quiz_on(client, message):
    user_id = message.from_user.id

    # Create time interval buttons arranged in 4x2 grid
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("30s", callback_data="30_sec"), InlineKeyboardButton("1min", callback_data="1_min")],
            [InlineKeyboardButton("5min", callback_data="5_min"), InlineKeyboardButton("10min", callback_data="10_min")],
        ]
    )

    # Send buttons with a description
    await message.reply_text(
        "<b>Choose how often you want the quiz to run. </b>\n\n"
        "- 30s: Quiz every 30 seconds\n"
        "- 1min: Quiz every 1 minute\n"
        "- 5min: Quiz every 5 minutes\n"
        "- 10min: Quiz every 10 minutes\n\n"
        "<b>Use `/quizoff` to stop the quiz loop at any time. </b>",
        reply_markup=keyboard
    )

# Handle button presses for time intervals
@app.on_callback_query(filters.regex(r"^\d+_sec$|^\d+_min$"))
async def start_quiz_loop(client, callback_query):
    user_id = callback_query.from_user.id
    chat_id = callback_query.message.chat.id

    if user_id in quiz_loops:
        await callback_query.answer("Qᴜɪᴢ ʟᴏᴏᴘ ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ...!!", show_alert=True)
        return

    # Determine interval based on the button pressed
    if callback_query.data == "30_sec":
        interval = 30
        interval_text = "30 seconds"
    elif callback_query.data == "1_min":
        interval = 60
        interval_text = "1 minute"
    elif callback_query.data == "5_min":
        interval = 300
        interval_text = "5 minutes"
    elif callback_query.data == "10_min":
        interval = 600
        interval_text = "10 minutes"

    # Delete the original message with buttons
    await callback_query.message.delete()

    # Confirm that the quiz loop has started
    await callback_query.message.reply_text(f"✅ Qᴜɪᴢ ʟᴏᴏᴘ sᴛᴀʀᴛᴇᴅ! Yᴏᴜ'ʟʟ ʀᴇᴄᴇɪᴠᴇ ᴀ ǫᴜɪᴢ ᴇᴠᴇʀʏ {interval_text}.")

    quiz_loops[user_id] = True  # Mark loop as running

    # Start the quiz loop with the selected interval
    while quiz_loops.get(user_id, False):
        await send_quiz_poll(client, chat_id, user_id, interval)
        await asyncio.sleep(interval)  # Wait for the selected interval before sending the next quiz

# /quiz off command to stop the quiz loop
@app.on_message(filters.command(["quizoff", "uizoff"], prefixes=["/", "!", ".", "Q", "q"]))
async def stop_quiz(client, message):
    user_id = message.from_user.id

    if user_id not in quiz_loops:
        await message.reply_text("Nᴏ ǫᴜɪᴢ ʟᴏᴏᴘ ɪs ʀᴜɴɴɪɴɢ.")
    else:
        quiz_loops.pop(user_id)  # Stop the loop
        await message.reply_text("❌️ Qᴜɪᴢ ʟᴏᴏᴘ sᴛᴏᴘᴘᴇᴅ...!!")

        # Delete the active poll if there's one
        if user_id in active_polls:
            try:
                await app.delete_messages(chat_id=message.chat.id, message_ids=active_polls[user_id])
                active_polls.pop(user_id)
            except Exception as e:
                print(f"Failed to delete active poll: {e}")
