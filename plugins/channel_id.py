from pyrogram import filters
from pyrogram import Client, enums
from pyrogram.file_id import FileId
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    if msg.forward_from:
        text = "<u>ɪɴғᴏʀᴍᴀᴛɪᴏɴ</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>ʙᴏᴛ ɪɴғᴏ</u>"
        else:
            text += "<u>ᴜsᴇʀ ɪɴғᴏ</u>"
        text += f'\n\nɴᴀᴍᴇ : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:

            text += f'\n\nᴜsᴇʀɴᴀᴍᴇ : @{msg.forward_from["username"]} \n\nɪᴅ : <code>{msg.forward_from["id"]}</code>\n\nᴅᴄ : {msg.forward_from["dc_id"]}'           
        else:
            text += f'\n\nɪᴅ : `{msg.forward_from["id"]}`\n\n\n\nᴅᴄ : {msg.forward_from["dc_id"]}'

        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"ᴇʀʀᴏʀ <b><i>{hidden}</i></b> ᴇʀʀᴏʀ",
                quote=True,
            )
        else:
            text = f"<u>ɪɴғᴏʀᴍᴀᴛɪᴏɴ</u>.\n\n"
            if msg.forward_from_chat["type"] == enums.ChatType.CHANNEL:
                text += "<u>ᴄʜᴀɴɴᴇʟ</u>"
            if msg.forward_from_chat["type"] == enums.ChatType.GROUP:
                text += "<u>ɢʀᴏᴜᴘ</u>"
            text += f'\n\nɴᴀᴍᴇ {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:

                text += f'\n\nғʀᴏᴍ : @{msg.forward_from_chat["username"]}'
                text += f'\n\nɪᴅ : `{msg.forward_from_chat["id"]}`\n\nᴅᴄ : {msg.forward_from_chat["dc_id"]}'
            else:
                text += f'\n\nɪᴅ `{msg.forward_from_chat["id"]}`\n\n{msg.forward_from_chat["dc_id"]}'                                           

            await msg.reply(text, quote=True)








