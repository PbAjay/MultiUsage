import pyrogram, asyncio, random, time, os
from pyrogram import Client, filters, enums
from pyrogram.types import *
from helper.database import add_user
from info import PICS
from helper.text import txt

@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    await add_user(bot, message)    
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton("📯 ᴜᴩᴅᴀᴛᴇꜱ", url="https://t.me/MLZ_BOTZ"),
        InlineKeyboardButton("🍁 ꜱᴜᴩᴩᴏʀᴛ ", url="https://t.me/MLZ_SUPPORT_BOTZ")
        ],[            
        InlineKeyboardButton("ℹ️ ʜᴇʟᴩ", callback_data="help"),
        InlineKeyboardButton("📡 ᴀʙᴏᴜᴛ", callback_data="about") 
    ]])
        
    if PICS:
        await message.reply_photo(photo=random.choice(PICS), caption=txt.STAT.format(message.from_user.mention), reply_markup=button)
    else:
        await message.reply_text(text=txt.STAT.format(message.from_user.mention), reply_markup=button, disable_web_page_preview=True)
        
                                              
@Client.on_message(filters.command(["id", "info"]))
async def media_info(bot, m): 
    message = m
    ff = m.from_user
    md = m.reply_to_message
    if md:
       try:
          if md.photo:
              await m.reply_text(text=f"**ʏᴏᴜʀ ᴘʜᴏᴛᴏ ɪᴅ ɪs **\n\n`{md.photo.file_id}`") 
          if md.sticker:
              await m.reply_text(text=f"**ʏᴏᴜʀ sᴛɪᴄᴋᴇʀ ɪᴅ ɪs **\n\n`{md.sticker.file_id}`")
          if md.video:
              await m.reply_text(text=f"**ʏᴏᴜʀ ᴠɪᴅᴇᴏ ɪᴅ ɪs **\n\n`{md.video.file_id}`")
          if md.document:
              await m.reply_text(text=f"**ʏᴏᴜʀ ᴅᴏᴄᴜᴍᴇɴᴛ ɪᴅ ɪs **\n\n`{md.document.file_id}`")
          if md.audio:
              await m.reply_text(text=f"**ʏᴏᴜʀ ᴀᴜᴅɪᴏ ɪᴅ ɪs **\n\n`{md.audio.file_id}`")
          if md.text:
              await m.reply_text("**ʜᴇʏ ᴍᴀɴ ʀᴇᴘʟʏ ᴡɪᴛʜ ( ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ, sᴛɪᴄᴋᴇʀ, ᴅᴏᴄᴜᴍᴇɴᴛ, ᴇᴛᴄ...) ᴏɴʟʏ ᴍᴇᴅɪᴀ **")  
          else:
              await m.reply_text("[404] Error..🤖")                                                                                      
       except Exception as e:
          print(e)
          await m.reply_text(f"[404] ᴇʀʀᴏʀ {e}")
                                        
    if not md:
        buttons = [[
            InlineKeyboardButton("📯 ᴜᴩᴅᴀᴛᴇꜱ", url="https://t.me/MLZ_BOTZ"),
            InlineKeyboardButton("🍁 ꜱᴜᴩᴩᴏʀᴛ ", url="https://t.me/MLZ_SUPPORT_BOTZ")
        ]]       
        mkn = await m.reply("please wait....")
        if ff.photo:
           user_dp = await bot.download_media(message=ff.photo.big_file_id)
           await m.reply_photo(
               photo=user_dp,
               caption=txt.INFO_TXT.format(id=ff.id, dc=ff.dc_id, n=ff.first_name, u=ff.username),
               reply_markup=InlineKeyboardMarkup(buttons),
               quote=True,
               parse_mode=enums.ParseMode.HTML,
               disable_notification=True
           )          
           os.remove(user_dp)
           await mkn.delete()
        else:  
           await m.reply_text(
               text=txt.INFO_TXT.format(id=ff.id, dc=ff.dc_id, n=ff.first_name, u=ff.username),
               reply_markup=InlineKeyboardMarkup(buttons),
               quote=True,
               parse_mode=enums.ParseMode.HTML,
               disable_notification=True
           )
