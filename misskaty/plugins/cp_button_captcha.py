from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from misskaty import BOT_USERNAME, app as pgram
from misskaty.ultis_ex.wmilia_m.button_gen import button_markdown_parser
from misskaty.ultis_ex.wmilia_m.chat_status import isUserAdmin
from misskaty.ultis_ex.wmilia_m.rules_mongo import get_rules
from misskaty.ultis_ex.wmilia_m.welcome_mongo import (
    GetCaptchaSettings,
    GetUserCaptchaMessageIDs,
    GetWelcome,
    isReCaptcha,
    isRuleCaptcha,
    isUserVerified,
    isWelcome,
)
from misskaty.plugins.cp_captcharules_button import ruleCaptchaButton


async def CaptchaButton(chat_id, user_id):
    captcha_mode, captcha_text, captcha_kick_time = await GetCaptchaSettings(chat_id)
    captchaButton = list()

    if (await isRuleCaptcha(chat_id)) and (await get_rules(chat_id)) is not None:
        captchaButton = [
            [
                InlineKeyboardButton(
                    text=captcha_text,
                    url=f"http://t.me/{BOT_USERNAME}?start=captcha_button_{user_id}_{chat_id}",
                )
            ]
        ]
    else:
        if await isUserVerified(chat_id, user_id):
            captchaButton = None
        else:
            captchaButton = [
                [
                    InlineKeyboardButton(
                        text=captcha_text, callback_data=f"captcha_{user_id}"
                    )
                ]
            ]

    return captchaButton


@Client.on_callback_query(filters.create(lambda _, __, query: "captcha_" in query.data))
async def CaptchaCallback(client: Client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    chat_id = callback_query.message.chat.id
    new_user_id = int(callback_query.data.split("_")[1])

    if new_user_id == user_id:
        if await isWelcome(chat_id):
            Content, Text, DataType = await GetWelcome(chat_id)
            Text, buttons = button_markdown_parser(Text)

            reply_markup = None
            if len(buttons) > 0:
                reply_markup = InlineKeyboardMarkup(buttons)
        else:
            reply_markup = None
        await callback_query.edit_message_reply_markup(reply_markup=reply_markup)
        await callback_query.answer(text="Thank for your time!")
        await pgram.restrict_chat_member(
            chat_id, new_user_id, ChatPermissions(can_send_messages=True)
        )
    else:
        await callback_query.answer(text="This button isn't made for you!")


async def buttonCaptchaRedirect(message):
    user_id = message.from_user.id
    if message.text.split()[1].split("_")[1] == "button":
        new_user_id = int(message.text.split()[1].split("_")[2])
        new_chat_id = int(message.text.split()[1].split("_")[3])

        if new_user_id == user_id:
            # Already Verified users
            if not (await isReCaptcha(chat_id=new_chat_id)):
                if await isUserVerified(new_chat_id, new_user_id):
                    await message.reply(
                        "You already passed the CAPTCHA, You don't need to verify yourself again.",
                        quote=True,
                    )
                    return

            # Admins captcha message
            if await isUserAdmin(
                message,
                pm_mode=True,
                chat_id=new_chat_id,
                user_id=new_user_id,
                silent=True,
            ):
                await message.reply(
                    "You are admin, You don't have to complete CAPTCHA.", quote=True
                )
                return

            (
                message_id,
                correct_captcha,
                chances,
                captcha_list,
            ) = await GetUserCaptchaMessageIDs(chat_id=new_chat_id, user_id=user_id)
            await ruleCaptchaButton(
                message=message, chat_id=new_chat_id, message_id=message_id
            )
