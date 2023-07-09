#codes created by @lallus_tg
#use this codes with proper credits 

import logging
import os
import requests
from pyrogram import Client, filters


@Client.on_message(filters.command('repo'))
async def git(Kashmira, message):
    pablo = await message.reply_text("ᴩʀᴏᴄᴇꜱꜱɪɴɢ...")
    args = message.text.split(None, 1)[1]
    if len(message.command) == 1:
        await pablo.edit("ɴᴏ ɪɴᴩᴜᴛ ꜰᴏᴜɴᴅ")
        return
    r = requests.get("https://api.github.com/search/repositories", params={"q": args})
    lool = r.json()
    if lool.get("total_count") == 0:
        await pablo.edit("ɴᴏ ʀᴇᴩᴏꜱ ꜰᴏᴜɴᴅ")
        return
    else:
        lol = lool.get("items")
        qw = lol[0]
        txt = f"""
<b>ɴᴀᴍᴇ :</b> <i>{qw.get("name")}</i>

<b>ꜰᴜʟʟ ɴᴀᴍᴇ:</b> <i>{qw.get("full_name")}</i>

<b>ʟɪɴᴋ :</b> {qw.get("html_url")}

<b>ꜰᴏʀᴋ ᴄᴏᴜɴᴛ :</b> <i>{qw.get("forks_count")}</i>

<b>ᴏᴩᴇɴ ɪꜱꜱᴜᴇ :</b> <i>{qw.get("open_issues")}</i>
"""
        if qw.get("description"):
            txt += f'<b>ᴅᴇꜱᴄʀɪᴩᴛɪᴏɴ :</b> <code>{qw.get("description")}</code>'
            

        if qw.get("language"):
            txt += f'<b>ʟᴀɴɢᴜᴀɢᴇ :</b> <code>{qw.get("language")}</code>'
            

        if qw.get("size"):
            txt += f'<b>ꜱɪᴢᴇ :</b> <code>{qw.get("size")}</code>'
            

        if qw.get("score"):
            txt += f'<b>ꜱᴄᴏʀᴇ :</b> <code>{qw.get("score")}</code>'
            

        if qw.get("created_at"):
            txt += f'<b>ᴄʀᴇᴀᴛᴇᴅ ᴀᴛ:</b> <code>{qw.get("created_at")}</code>'
            

        if qw.get("archived") == True:
            txt += f"<b>This Project is Archived</b>"
        await pablo.edit(txt, disable_web_page_preview=True)
