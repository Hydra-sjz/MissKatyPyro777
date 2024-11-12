# DONE: Topics

from telethon import functions

import misskaty.strings as strings
from misskaty import tle as meow
from misskaty.custom_filter import register
from misskaty.ultis_ex.wmilia_m.admins import can_manage_topics
from misskaty.ultis_ex.wmilia_m.decorators import *


@usage("/newtopic [name]")
@example("/newtopic Games")
@description(
    "This will create a new topic with the given name inside a topic-enabled group."
)
@register(pattern="newtopic")
@anonadmin_checker
@exception
@logging
async def create_topic(event):
    if event.is_private:
        return await event.reply(strings.is_pvt)

    if not await can_manage_topics(event, event.sender_id):
        return

    args = event.text.split(None, 1)[1]

    if event.chat.forum:
        if not args:
            return await usage_string(event, create_topic)

        topic = await meow(
            functions.channels.CreateForumTopicRequest(
                channel=event.chat_id, title=args
            )
        )
        result = topic.updates[1].message
        await event.reply(f"Successfully created {args}\nID: {result.id}")
        await meow.send_message(
            event.chat_id,
            f"Congratulations {args} created successfully\nID: {result.id}",
            reply_to=result.id,
        )
        return "NEW_TOPIC", None, None
    else:
        return await event.reply("You can create topics in topics-enabled groups only.")


@usage("/deletetopic [topic id]")
@example("/deletetopic 1234567890")
@description(
    "This will delete the topic with the given ID inside a topic-enabled group. It will not work for general topics."
)
@register(pattern="deletetopic")
@anonadmin_checker
@exception
@logging
async def delete_topic(event):
    if event.is_private:
        return await event.reply(strings.is_pvt)

    if not await can_manage_topics(event, event.sender_id):
        return

    if event.chat.forum:
        try:
            topic_id = event.text.split(None, 1)[1]
            topic_id = int(topic_id)
        except (ValueError, TypeError):
            return await usage_string(event, delete_topic)

        await meow(
            functions.channels.DeleteTopicHistoryRequest(
                channel=event.chat_id, top_msg_id=topic_id
            )
        )
        return "DELETE_TOPIC", None, None
    else:
        return await event.reply(
            "You can perform this action in topics-enabled groups only."
        )


@usage("/closetopic [topic id]")
@example("/closetopic 1234567890")
@description(
    "This will close the topic with the given ID inside a topic-enabled group. It will not work for general topics."
)
@register(pattern="closetopic")
@anonadmin_checker
@exception
@logging
async def close_topic(event):
    if event.is_private:
        return await event.reply(strings.is_pvt)

    if not await can_manage_topics(event, event.sender_id):
        return

    if event.chat.forum:
        try:
            topic_id = event.text.split(None, 1)[1]
            topic_id = int(topic_id)
        except (ValueError, TypeError):
            return await usage_string(event, close_topic)

        await meow(
            functions.channels.EditForumTopicRequest(
                channel=event.chat_id, topic_id=topic_id, closed=True
            )
        )
        return "CLOSED_TOPIC", None, None
    else:
        return await event.reply(
            "You can perform this action in topics-enabled groups only."
        )


@usage("/opentopic [topic id]")
@example("/opentopic 1234567890")
@description(
    "This will open the topic with the given ID inside a topic-enabled group. It will not work for general topics since they are already opened."
)
@register(pattern="opentopic")
@anonadmin_checker
@exception
@logging
async def open_topic(event):
    if event.is_private:
        return await event.reply(strings.is_pvt)

    if not await can_manage_topics(event, event.sender_id):
        return

    if event.chat.forum:
        try:
            topic_id = event.text.split(None, 1)[1]
            topic_id = int(topic_id)
        except (ValueError, TypeError):
            return await usage_string(event, open_topic)

        await meow(
            functions.channels.EditForumTopicRequest(
                channel=event.chat_id, topic_id=topic_id, closed=False
            )
        )
        return "OPENED_TOPIC", None, None
    else:
        return await event.reply(
            "You can perform this action in topics-enabled groups only."
        )


@register(pattern="renametopic")
@exception
@anonadmin_checker
@logging
async def rename_topic(event):
    if event.is_private:
        return await event.reply(strings.is_pvt)

    if not await can_manage_topics(event, event.sender_id):
        return

    args = event.text.split(None, 1)[1]

    if not args:
        return await event.reply("Please provide a new name for the topic.")

    if event.chat.forum:
        try:
            topic_id = event.reply_to.reply_to_msg_id
        except (ValueError, TypeError):
            return await event.reply(
                "Please execute this command inside the topic which you want to rename."
            )

        result = await meow(
            functions.channels.EditForumTopicRequest(
                channel=event.chat_id, topic_id=topic_id, title=args
            )
        )
        if result:
            topic_name = result.updates[1].message.action.title
            await event.reply(f"Successfully renamed the topic to {topic_name}!")
            return "RENAMED_TOPIC", None, None
    else:
        return await event.reply(
            "You can perform this command in topics-enabled groups only."
        )
