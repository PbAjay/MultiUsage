from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters

"""Edit ചെയ്യുന്നവനോട്.. നിന്റെ തന്ത അല്ല ഈ code ഉണ്ടാക്കിയത് """

@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="sᴇʟᴇᴄᴛ ʏᴏᴜʀ ʀᴇǫᴜɪʀᴇᴅ ᴍᴏᴅᴇ ғʀᴏᴍ ʙᴇʟᴏᴡㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ʙʀɪɢᴛʜ", callback_data="bright"),
                        InlineKeyboardButton(text="ᴍɪxᴇᴅ", callback_data="mix"),
                        InlineKeyboardButton(text="ʙ&ᴡ", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="ᴄɪʀᴄʟᴇ", callback_data="circle"),
                        InlineKeyboardButton(text="ʙʟᴜʀ", callback_data="blur"),
                        InlineKeyboardButton(text="ʙᴏʀᴅᴇʀ", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="sᴛɪᴄᴋᴇʀ", callback_data="stick"),
                        InlineKeyboardButton(text="ʀᴏᴛᴀᴛᴇ", callback_data="rotate"),
                        InlineKeyboardButton(text="ᴄᴏɴᴛʀᴀsᴛ", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="sᴇᴘɪᴀ", callback_data="sepia"),
                        InlineKeyboardButton(text="ᴘᴇɴᴄɪʟ", callback_data="pencil"),
                        InlineKeyboardButton(text="ᴄᴀʀᴛᴏᴏɴ", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="ɪɴᴠᴇʀᴛ", callback_data="inverted"),
                        InlineKeyboardButton(text="ɢʟɪᴛᴄʜ", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="ʀᴇᴍᴏᴠᴇ ʙɢ", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close_data"),
                    ],
                ]
            ),
            reply_to_message_id=message.id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ!", quote=True)
            except Exception:
                return







