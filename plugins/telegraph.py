import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import *
from telegraph import upload_file


@Client.on_message(filters.command("telegraph") & filters.private)
async def telegraph_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        return await update.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ 5ᴍʙ")
    if not ( replied.photo or replied.video ):
        return await update.reply_text("ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀ ᴠᴀʟɪᴅ ᴍᴇᴅɪᴀ ғɪʟᴇ")
    text = await update.reply_text("<code>ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛᴏ ᴍʏ sᴇʀᴠᴇʀ....</code>", disable_web_page_preview=True)   
    media = await replied.download()   
    await text.edit_text("<code>ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴄᴏᴍᴘʟᴇᴛᴇᴅ. ɴᴏᴡ ɪ'ᴍ ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ telegra.ph ʟɪɴᴋ....</code>", disable_web_page_preview=True)                                            
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        return await text.edit_text(text=f"Error :- {error}", disable_web_page_preview=True)          
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return    
    await text.edit_text(
        text=f"<b>ʟɪɴᴋ :-</b>\n\n<code>https://graph.org{response[0]}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text="ᴏᴘᴇɴ ʟɪɴᴋ", url=f"https://graph.org{response[0]}"),
            InlineKeyboardButton(text="sʜᴀʀᴇ ʟɪɴᴋ", url=f"https://telegram.me/share/url?url=https://graph.org{response[0]}")
            ],[
            InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close")
            ]]
        )
    )
