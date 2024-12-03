from telethon import errors

# admin
CAN_CHANGE_INFO = "You need to be admin and should have can_change_info permission to perform this task."
NOT_ADMIN = "You need to be an admin to perform this task."
NOT_OWNER = "You need to be owner of this chat to perform this task."
ON_ADMIN = "You cannot perform this command on admins."
OFF_ADMIN = "You cannot perform this command on non-admins."
CAN_BAN = "You need to be admin and should have ban_right to perform this task."
CAN_PROMOTE = (
    "You need to be admin and should have promote_user right to perform this task."
)
CAN_PIN = "You need to be admin and should have pin_message right to perform this task."
CAN_DELETE = (
    "You need to be admin and should have delete_message right to perform this task."
)
NOT_TOPIC = (
    "You need to be admin and should have manage_topics right to perform this task."
)

# bot
botban = (
    "You need to make me admin with ban_users right so that i can perform this command!"
)
botpromote = "You need to make me admin with promote_users right so that i can perform this command!"
botinfo = "You need to make me admin with can_change_info right so that i can perform this command!"

# private
is_pvt = "Group only command."

# errors
index = "Please provide me some term or reply with some text to perform this command correctly."
nouser = "No user found."
invalid = "Invalid username/id given."
media = "Reply with some media/photo to perform this command."
imedia = "Invalid file/media provided"


# exceptions
error_messages = {
    errors.ChatAdminRequiredError: "You need to make me an admin with appropriate rights so that I can perform this command!",
    errors.AdminsTooMuchError: "Already too many admins.",
    errors.AdminRankInvalidError: "Title too large or invalid title provided.",
    errors.BotChannelsNaError: "This user was promoted by someone else, so I cannot change admin privileges.",
    errors.AdminRankEmojiNotAllowedError: "Emojis are not allowed in the admin's title.",
    errors.PhotoCropSizeSmallError: "The image is too small.",
    errors.ImageProcessFailedError: "Failed to process the image.",
    errors.ChatAboutNotModifiedError: "The about text should be different than the current one.",
    errors.ChatAboutTooLongError: "The about text is too long. Please provide a shorter one.",
    errors.ChatSendMediaForbiddenError: "I am not allowed to send media in this chat. Please make me an admin to do so.",
    errors.ChatSendGifsForbiddenError: "I am not allowed to send gifs in this chat. Please make me an admin to do so.",
    errors.ChatSendStickersForbiddenError: "I am not allowed to send stickers in this chat. Please make me an admin to do so.",
    errors.ChatNotModifiedError: "The chat title provided is the same as the current one.",
    errors.TopicDeletedError: "The topic is already deleted.",
}



birthday_wish =  [
    "Wishing you a happy birthday filled with love and joy.",
    "Hope your birthday is as wonderful as you are.",
    "Happy birthday to someone who deserves an exceptional day.",
    "May your birthday be full of surprises and delight.",
    "Wishing you a year filled with new adventures and accomplishments.",
    "May your birthday be as sweet as cake and as joyful as the celebration.",
    "Here's to a fabulous birthday and a year filled with blessings.",
    "Sending you lots of love and warm wishes on your special day.",
    "May your birthday be a time for reflection, relaxation, and joy.",
    "Cheers to another year of making unforgettable memories!",
    "May your birthday be filled with laughter, love, and good times.",
    "Wishing you a birthday that's just as amazing as you are.",
    "Here's to a year filled with love, happiness, and success.",
    "May your birthday be filled with all the love and blessings you deserve.",
    "Sending you warm wishes for a joyful and memorable birthday.",
    "Wishing you a birthday that's as wonderful as you are.",
    "May your birthday be a time to celebrate all the amazing things you've accomplished.",
    "Here's to another year of blessings, love, and adventure.",
    "Sending you lots of love, hugs, and birthday wishes.",
    "May your birthday be full of sunshine, laughter, and good times.",
    "Wishing you a year filled with happiness, success, and love.",
    "Here's to a fantastic birthday and an even better year ahead!",
    "May your birthday be a day filled with joy, love, and celebration.",
    "Sending you lots of love and warm wishes on your special day.",
    "Wishing you a birthday that's as bright and beautiful as you are.",
    "May your birthday be full of love, laughter, and happiness.",
    "Here's to a year filled with exciting adventures and new opportunities.",
    "Wishing you a birthday that's just as amazing as you are.",
    "May your birthday be a time to reflect on all the wonderful things in your life.",
    "Sending you lots of love, hugs, and birthday wishes from afar.",
    "Wishing you a year filled with love, laughter, and all your heart desires.",
    "May your birthday be a time to relax, unwind, and enjoy the company of loved ones.",
    "Here's to another year of blessings, love, and adventure.",
    "Sending you warm wishes for a wonderful and unforgettable birthday.",
    "Wishing you a birthday that's as special and unique as you are.",
    "May your birthday be a time to cherish all the special moments and memories you've created.",
    "Here's to a year filled with joy, laughter, and happiness.",
    "Wishing you a birthday that's just as amazing as you are.",
    "May your birthday be a time to celebrate your wonderful achievements and accomplishments.",
    "Sending you lots of love, hugs, and birthday wishes to make your day extra special.",
    "Wishing you a year filled with love, happiness, and all your heart's desires.",
    "May your birthday be a time to create new memories and cherish old ones.",
    "Here's to another year of blessings, love, and adventure.",
    "Sending you warm wishes for a fabulous and unforgettable birthday.",
    "Wishing you a birthday that's full of love, laughter, and happiness.",
    "May your birthday be a time to appreciate all the wonderful people in your life.",
    "Wishing you a birthday as amazing as you are, filled with joy and memories to last a lifetime.",
    "May your birthday be full of laughter and love, and your year be full of happiness and success.",
    "Happy birthday to someone who makes the world a better place, may all your wishes come true.",
    "Sending you warm birthday wishes and virtual hugs, can't wait to celebrate in person!",
    "May your birthday be as special as you are, surrounded by all the people who love you the most.",
    "Wishing you a day filled with laughter and a year filled with new adventures and opportunities.",
    "Happy birthday to someone who's always there to brighten up my day, may your day be as bright as you are.",
    "Here's to a birthday that's just as awesome as you are, and a year filled with love and happiness.",
    "May your birthday be a time to reflect on all the wonderful memories you've made, and look forward to new ones.",
    "Wishing you a birthday that's full of surprises and excitement and a year filled with new beginnings.",
    "Happy birthday to my favourite person in the world, may your day be as special as you are to me.",
    "Sending you the biggest birthday hugs and all my love, may your day be filled with joy and celebration.",
    "May your birthday be a time to celebrate all your accomplishments and be proud of all you've achieved.",
    "Wishing you a birthday that's as bright and beautiful as you are, filled with love and laughter.",
    "Happy birthday to a true gem, may your day be filled with joy, laughter, and all the things you love.",
    "Here's to a birthday that's full of happiness, excitement, and all the people who make your life special.",
    "May your birthday be a time to let loose and have fun, and your year be filled with growth and success.",
    "Wishing you a birthday that's full of all the things you love and a year that's even better than the last.",
    "Happy birthday to someone who makes my life brighter, may your day be as amazing as you are.",
    "Sending you lots of love and virtual hugs on your special day, may your year be filled with blessings.",
    "May your birthday be a time to cherish all the people who make your life special, and celebrate the person you've become.",
    "Wishing you a birthday that's as unique and wonderful as you are, filled with love and laughter.",
    "Happy birthday to someone who's always been there for me, may your day be filled with joy and celebration.",
    "Here's to a birthday that's full of love, happiness, and all the things that bring you the most joy.",
    "May your birthday be a time to reflect on all the amazing things you've accomplished, and look forward to all that's to come.",
    "Wishing you a birthday that's full of surprises, happiness, and all the things that make you feel alive.",
    "Happy birthday to someone who brings a smile to my face every day, may your day be as wonderful as you are.",
    "Sending you all my love and warmest wishes on your special day, may your year be filled with love and happiness.",
    "May your birthday be a time to appreciate all the people who make your life special, and cherish all the memories you've created.",
    "Wishing you a birthday that's as beautiful as you are, filled with joy and celebration.",]
