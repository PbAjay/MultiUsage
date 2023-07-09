from pyrogram import Client, filters
from pyrogram.types import *
import requests 


@Client.on_message(filters.command("write"))
async def handwriting(client, message):
    if len(message.command) < 2:
        return await message.reply_text("ɢɪᴠᴇ ꜱᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ...")
    m = await message.reply_text("ᴩʟᴇᴀꜱᴇ ᴡᴀɪᴛ ᴀᴍ  ᴡʀɪᴛᴇɪɴɢ...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    API = "https://apis.xditya.me/write?text=" + name
    url = requests.get(API).url
    await m.edit("ᴜᴩʟᴏᴅɪɴɢ...")
    me = await client.get_me()
    await message.reply_photo(url, caption=f"""**ʀᴇǫᴜᴇꜱᴛᴇᴅ ʙʏ {message.from_user.mention}**\n
""",
    reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton(text="ᴅᴏᴡɴʟᴏᴀᴅ", url=url)]]))
