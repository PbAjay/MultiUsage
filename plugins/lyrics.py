from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

import requests 

import os


API = "https://apis.xditya.me/lyrics?song="

@Client.on_message(filters.text & filters.command(["lyrics"]))
async def sng(bot, message):
        if not message.reply_to_message:
          await message.reply_text("ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ")
        else:          
          mee = await message.reply_text("`ꜱᴇᴀʀᴄʜɪɴɢ...`")
          song = message.reply_to_message.text
          chat_id = message.from_user.id
          rpl = lyrics(song)
          await mee.delete()
          try:
            await mee.delete()
            await bot.send_message(chat_id, text = rpl, reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs ", url = f"t.me/mkn_bots_updates")]]))
          except Exception as e:                            
             await message.reply_text(f"ɪ ᴄᴀɴ'ᴛ ᴀ ꜱᴏɴɢ ᴡɪᴛʜ`{song}`ᴛʜɪꜱ ɴᴀᴍᴇ", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url = f"t.me/mkn_bots_updates")]]))


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 ꜱᴜᴄᴄᴇꜱꜰᴜʟʟʏ ᴇxᴛʀᴀᴄᴛᴇᴅ ʟʏɪʀɪᴄꜱ ᴏꜰ {song}**\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**ᴍᴀᴅᴇ ʙʏ ᴀɪ**'
        return text

