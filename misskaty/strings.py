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
