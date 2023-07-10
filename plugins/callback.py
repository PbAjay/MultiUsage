import asyncio, pyrogram
from helper.text import txt as tg 
from plugins.functions.http import get

from plugins.font_btn import style_btn_back, nxt_fonts_nxt, style_btn_editz
from pyrogram import Client, filters, __version__, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery                            

from image.edit_1 import (bright, mix, black_white, g_blur, normal_blur, box_blur)
from image.edit_2 import (circle_with_bg, circle_without_bg, sticker, edge_curved, contrast, sepia_mode, pencil, cartoon)                              
from image.edit_3 import (green_border, blue_border, black_border, red_border)
from image.edit_4 import (rotate_90, rotate_180, rotate_270, inverted, round_sticker, removebg_white, removebg_plain, removebg_sticker)
from image.edit_5 import (normalglitch_1, normalglitch_2, normalglitch_3, normalglitch_4, normalglitch_5, scanlineglitch_1, scanlineglitch_2, scanlineglitch_3, scanlineglitch_4, scanlineglitch_5)                             
 

@Client.on_callback_query()
async def callback(client: Client, query: CallbackQuery): 
    if query.data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif query.data == "start":
       await query.message.edit(
           text = tg.STAT.format(query.from_user.mention),        
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("📯 ᴜᴩᴅᴀᴛᴇꜱ", url="https://t.me/MLZ_BOTZ"),
               InlineKeyboardButton("🍁 ꜱᴜᴩᴩᴏʀᴛ ", url="https://t.me/MLZ_BOTZ_SUPPORT")
               ],[            
               InlineKeyboardButton("ℹ️ ʜᴇʟᴩ", callback_data="help"),
               InlineKeyboardButton("📡 ᴀʙᴏᴜᴛ", callback_data="about") 
               ]]
               )
       )
    elif query.data == "help":
        buttons = [[                           
            InlineKeyboardButton('ʟᴏɢᴏ ᴍᴀᴋᴇʀ', callback_data='logomake'), 
            InlineKeyboardButton('ɪɴꜰᴏ & ɪᴅ', callback_data='info'),
            InlineKeyboardButton('ᴛᴇʟᴇɢʀᴀᴩʜ', callback_data='tgraph')
            ],[
            InlineKeyboardButton('ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ', callback_data='tts'),
            InlineKeyboardButton('ʟʏʀɪᴄs', callback_data='lyrics'),
            InlineKeyboardButton('ʏᴏᴜᴛᴜʙᴇ ᴅʟ', callback_data='ytdl')
            ],[
            InlineKeyboardButton('ᴩʜᴏᴛᴏ ᴛᴏᴏʟ', callback_data='phediter'),
            InlineKeyboardButton('ʀᴇᴘᴏ', callback_data='repo'),
            InlineKeyboardButton('ᴡʀɪᴛᴇ', callback_data='write')
            ],[
            InlineKeyboardButton('ꜱᴛɪᴄᴋᴇʀ', callback_data='stickertool'),
            InlineKeyboardButton('ᴜʀʟ sʜᴏʀᴛ', callback_data='url'),
            InlineKeyboardButton('ꜰᴏɴᴛ', callback_data='fontstyle')            
            ],[
            InlineKeyboardButton('ᴄᴀʀʙᴏɴ', callback_data='carben'),
            InlineKeyboardButton('sᴏɴɢ', callback_data='song')                      
            ],[
            InlineKeyboardButton('⏮️ ʙᴀᴄᴋ', callback_data='start'),           
        ]]
        await query.message.edit_text(                     
            text=tg.HELP,
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=enums.ParseMode.HTML
        )
    
    elif query.data == "info":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.INFO,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML     
       )       
    elif query.data == "logomake":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.LOGO,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML     
       )                 
    elif query.data == "song":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.SONG,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML     
       )                 
    elif query.data == "url":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.URL,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML     
       )                 
    elif query.data == "lyrics":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.LYRICS,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML     
       )           
    elif query.data == "tgraph":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.TELE,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML     
       )   
    elif query.data == "repo":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.REPO,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML     
       )   
    elif query.data == "write":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.WRITE,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML     
       )   
    elif query.data == "tts":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.TTS,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML   
       )   
    elif query.data == "ytdl":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.YTDL,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML  
       )    
    elif query.data == "phediter":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.IMAGE,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML  
       )    
    elif query.data == "paster":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.PASTE,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML  
       )    
    elif query.data == "carben":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.CARB_TXT,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML     
       )    
    elif query.data == "stickertool":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.STICKER,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML     
       )    
    elif query.data == "fontstyle":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]    
       await query.message.edit(
           text=tg.FONT,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML    
       )    
    elif query.data == "fun":
       buttons = [[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="help"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.FUN,
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML   
       )    
    elif query.data == "about":       
       buttons = [[
           InlineKeyboardButton("ᴏᴡɴᴇʀ", url="t.me/MATRIX_TG"),
           InlineKeyboardButton("ᴅᴇᴠs", callback_data="source")  
           ],[        
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="start"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.ABT.format(v=__version__, bot=client.mention),
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.HTML        
       )            
    elif query.data == "source":
       buttons = [[
           InlineKeyboardButton("👨‍💻 ᴅᴇᴠ 1", url="https://t.me/AJAYxTG"),
           InlineKeyboardButton("👨‍💻 ᴅᴇᴠ 2", url="https://t.me/MATRIX_TG")
           ],[
           InlineKeyboardButton("⏮️ ʙᴀᴄᴋ", callback_data="start"),
           InlineKeyboardButton("🔒 ᴄʟᴏꜱᴇ", callback_data="close")
       ]]               
       await query.message.edit(
           text=tg.SOURCE.format(dev=list_of_users),
           reply_markup=InlineKeyboardMarkup(buttons),
           disable_web_page_preview = True,
           parse_mode=enums.ParseMode.MARKDOWN
       )    
    elif query.data == "removebg":
       await query.message.edit_text(
           text="**sᴇʟᴇᴄᴛ ʀᴇǫᴜɪʀᴇᴅ ᴍᴏᴅᴇ**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="ᴡɪᴛʜ ᴡʜɪᴛᴇ ʙɢ", callback_data="rmbgwhite"),
               InlineKeyboardButton(text="ᴡɪᴛʜᴏᴜᴛ ʙɢ", callback_data="rmbgplain"),
               ],[
               InlineKeyboardButton(text="sᴛɪᴄᴋᴇʀ", callback_data="rmbgsticker"),
               ],[
               InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='photo')
               ]]
           )
       )
    elif query.data == "stick":
       await query.message.edit(
           text="**sᴇʟᴇᴄᴛ ᴀ ᴛʏᴘᴇ**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="ɴᴏʀᴍᴀʟ", callback_data="stkr"),
               InlineKeyboardButton(text="ᴇᴅɢᴇ ᴄᴜʀᴠᴇᴅ", callback_data="cur_ved"),
               ],[                    
               InlineKeyboardButton(text="ᴄɪʀᴄʟᴇ", callback_data="circle_sticker")
               ],[
               InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='photo')
               ]]                
           )
       )
    elif query.data == "rotate":
       await query.message.edit_text(
           text="**sᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇɢʀᴇᴇ**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="180", callback_data="180"),
               InlineKeyboardButton(text="90", callback_data="90")
               ],[
               InlineKeyboardButton(text="270", callback_data="270")
               ],[
               InlineKeyboardButton('𝙱𝙰𝙲𝙺', callback_data='photo')
               ]]
           )
       )
    elif query.data == "glitch":
       await query.message.edit_text(
           text="**sᴇʟᴇᴄᴛ ʀᴇǫᴜɪʀᴇᴅ ᴍᴏᴅᴇ**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="ɴᴏʀᴍᴀʟ", callback_data="normalglitch"),
               InlineKeyboardButton(text="sᴄᴀɴ ʟᴀɪɴs", callback_data="scanlineglitch")
               ],[
               InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='photo')
               ]]
           )
       )
    elif query.data == "normalglitch":
       await query.message.edit_text(
           text="**sᴇʟᴇᴄᴛ ɢʟɪᴛᴄʜ ᴘᴏᴡᴇʀ ʟᴇᴠᴇʟ**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="1", callback_data="normalglitch1"),
               InlineKeyboardButton(text="2", callback_data="normalglitch2"),
               InlineKeyboardButton(text="3", callback_data="normalglitch3"),
               ],[
               InlineKeyboardButton(text="4", callback_data="normalglitch4"),
               InlineKeyboardButton(text="5", callback_data="normalglitch5"),
               ],[
               InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='glitch')
               ]]
           )
       )
    elif query.data == "scanlineglitch":
       await query.message.edit_text(
           text="**sᴇʟᴇᴄᴛ ɢʟɪᴛᴄʜ ᴘᴏᴡᴇʀ ʟᴇᴠᴇʟ**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="1", callback_data="scanlineglitch1"),
               InlineKeyboardButton(text="2", callback_data="scanlineglitch2"),
               InlineKeyboardButton(text="3", callback_data="scanlineglitch3"),
               ],[
               InlineKeyboardButton(text="4", callback_data="scanlineglitch4"),
               InlineKeyboardButton(text="5", callback_data="scanlineglitch5"),
               ],[
               InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='glitch')
               ]]
           )
       )
    elif query.data == "blur":
       await query.message.edit(
           text="**sᴇʟᴇᴄᴛ ᴀ ᴛʏᴘᴇ**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="ʙᴏx", callback_data="box"),
               InlineKeyboardButton(text="ɴᴏʀᴍᴀʟ", callback_data="normal"),
               ],[
               InlineKeyboardButton(text="ɢᴀᴜssɪᴀɴ", callback_data="gas")
               ],[
               InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='photo')
               ]]
           )
       )
    elif query.data == "circle":
       await query.message.edit_text(
           text="**sᴇʟᴇᴄᴛ ʀᴇǫᴜɪʀᴇᴅ ᴍᴏᴅᴇ**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="ᴡɪᴛʜ ʙɢ", callback_data="circlewithbg"),
               InlineKeyboardButton(text="ᴡɪᴛʜᴏᴜᴛ ʙɢ", callback_data="circlewithoutbg"),
               ],[
               InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='photo')
               ]]
           )
       )
    elif query.data == "border":
       await query.message.edit(
           text="**sᴇʟᴇᴄᴛ ʙᴏʀᴅᴇʀ**",
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(text="ʀᴇᴅ", callback_data="red"),
               InlineKeyboardButton(text="ɢʀᴇᴇɴ", callback_data="green"),
               ],[
               InlineKeyboardButton(text="ʙʟᴀᴄᴋ", callback_data="black"),
               InlineKeyboardButton(text="ʙʟᴜᴇ", callback_data="blue"),
               ],[                    
               InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='photo')   
               ]]                
           )
       )
    elif query.data == "bright":
        await bright(client, query.message)
    elif query.data == "mix":
        await mix(client, query.message)
    elif query.data == "b|w":
        await black_white(client, query.message)
    elif query.data == "circlewithbg":
        await circle_with_bg(client, query.message)
    elif query.data == "circlewithoutbg":
        await circle_without_bg(client, query.message)
    elif query.data == "green":
        await green_border(client, query.message)
    elif query.data == "blue":
        await blue_border(client, query.message)
    elif query.data == "red":
        await red_border(client, query.message)
    elif query.data == "black":
        await black_border(client, query.message)
    elif query.data == "circle_sticker":
        await round_sticker(client, query.message)
    elif query.data == "inverted":
        await inverted(client, query.message)
    elif query.data == "stkr":
        await sticker(client, query.message)
    elif query.data == "cur_ved":
        await edge_curved(client, query.message)
    elif query.data == "90":
        await rotate_90(client, query.message)
    elif query.data == "180":
        await rotate_180(client, query.message)
    elif query.data == "270":
        await rotate_270(client, query.message)
    elif query.data == "contrast":
        await contrast(client, query.message)
    elif query.data == "box":
        await box_blur(client, query.message)
    elif query.data == "gas":
        await g_blur(client, query.message)
    elif query.data == "normal":
        await normal_blur(client, query.message)
    elif query.data == "sepia":
        await sepia_mode(client, query.message)
    elif query.data == "pencil":
        await pencil(client, query.message)
    elif query.data == "cartoon":
        await cartoon(client, query.message)
    elif query.data == "normalglitch1":
        await normalglitch_1(client, query.message)
    elif query.data == "normalglitch2":
        await normalglitch_2(client, query.message)
    elif query.data == "normalglitch3":
        await normalglitch_3(client, query.message)
    elif query.data == "normalglitch4":
        await normalglitch_4(client, query.message)
    elif query.data == "normalglitch5":
        await normalglitch_5(client, query.message)
    elif query.data == "scanlineglitch1":
        await scanlineglitch_1(client, query.message)
    elif query.data == "scanlineglitch2":
        await scanlineglitch_2(client, query.message)
    elif query.data == "scanlineglitch3":
        await scanlineglitch_3(client, query.message)
    elif query.data == "scanlineglitch4":
        await scanlineglitch_4(client, query.message)
    elif query.data == "scanlineglitch5":
        await scanlineglitch_5(client, query.message)
    elif query.data == "rmbgwhite":
        await removebg_white(client, query.message)
    elif query.data == "rmbgplain":
        await removebg_plain(client, query.message)
    elif query.data == "rmbgsticker":
        await removebg_sticker(client, query.message)
    elif query.data == "photo":
        buttons = [[
            InlineKeyboardButton(text="𝖡𝗋𝗂𝗀𝗍𝗁", callback_data="bright"),
            InlineKeyboardButton(text="𝖬𝗂𝗑𝖾𝖽", callback_data="mix"),
            InlineKeyboardButton(text="𝖡 & 𝖶", callback_data="b|w"),
            ],[
            InlineKeyboardButton(text="𝖢𝗂𝗋𝖼𝗅𝖾", callback_data="circle"),
            InlineKeyboardButton(text="𝖡𝗅𝗎𝗋", callback_data="blur"),
            InlineKeyboardButton(text="𝖡𝗈𝗋𝖽𝖾𝗋", callback_data="border"),
            ],[
            InlineKeyboardButton(text="𝖲𝗍𝗂𝖼𝗄𝖾𝗋", callback_data="stick"),
            InlineKeyboardButton(text="𝖱𝗈𝗍𝖺𝗍𝖾", callback_data="rotate"),
            InlineKeyboardButton(text="𝖢𝗈𝗇𝗍𝗋𝖺𝗌𝗍", callback_data="contrast"),
            ],[
            InlineKeyboardButton(text="𝖲𝖾𝗉𝗂𝖺", callback_data="sepia"),
            InlineKeyboardButton(text="𝖯𝖾𝗇𝖼𝗂𝗅", callback_data="pencil"),
            InlineKeyboardButton(text="𝖢𝖺𝗋𝗍𝗈𝗈𝗇", callback_data="cartoon"),
            ],[
            InlineKeyboardButton(text="𝖨𝗇𝗏𝖾𝗋𝗍", callback_data="inverted"),
            InlineKeyboardButton(text="𝖦𝗅𝗂𝗍𝖼𝗁", callback_data="glitch"),
            InlineKeyboardButton(text="𝖱𝖾𝗆𝗈𝗏𝖾 𝖡𝖦", callback_data="removebg")
            ],[
            InlineKeyboardButton(text="𝖢𝗅𝗈𝗌𝖾", callback_data="close_data")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)        
        await query.message.edit_text(        
            text="Select your required mode from below!",
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "nxt":
       await nxt_fonts_nxt(client, query)
    elif query.data == "fontblack":
       await style_btn_back(client, query)    
    elif "style" in query.data:
       cmd, style = query.data.split('+')
       await style_btn_editz(client, query, style) 

               
