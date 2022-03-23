import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

bot = Client(
   "Telegra.ph-x Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@epusthakalaya_bots.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
   await message.reply_chat_action("typing")
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>🔥𝓗𝓲 𝓣𝓱𝓮𝓻𝓮,</b>

𝗜'𝗺 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗽𝗵 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗿 𝗥𝗼𝗯𝗼𝘁 🇱🇰

📝𝗜 𝗖𝗮𝗻 𝗨𝗽𝗹𝗼𝗮𝗱 𝗣𝗵𝗼𝘁𝗼𝘀 𝗢𝗿 𝗩𝗶𝗱𝗲𝗼𝘀 𝗬𝗼𝘂 𝗦𝗲𝗻𝗱 𝗠𝗲 𝗧𝗼 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗽𝗵📤
📌𝗛𝗶𝘁 𝗛𝗲𝗹𝗽 𝗕𝘂𝘁𝘁𝗼𝗻 𝗧𝗼 𝗙𝗶𝗻𝗱 𝗢𝘂𝘁 𝗠𝗼𝗿𝗲 𝗔𝗯𝗼𝘂𝘁 𝗛𝗼𝘄 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲🙋‍♂️

⚙️𝗣𝗼𝘄𝗲𝗿𝗱 𝗕𝘆 :- <b>@AnonymousBotsInfinity</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Help 🚀", callback_data="help"),
                                        ],[
                                        InlineKeyboardButton(
                                            "Updates 🍀", url="https://t.me/AnonymousBotInfinity"),
                                        InlineKeyboardButton(
                                            "Support 🌺", url="https://t.me/AnonymousBotInfinitySupport")
                                        ],[
                               ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@epusthakalaya_bots.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await bot.send_message(
               chat_id=message.chat.id,
               text="""𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗽𝗵 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗿 𝗥𝗼𝗯𝗼𝘁 𝗛𝗲𝗹𝗽 𝗠𝗲𝗻𝘂📮

📊𝗝𝘂𝘀𝘁 𝗦𝗲𝗻𝗱 𝗔 𝗣𝗵𝗼𝘁𝗼 , 𝗚𝗶𝗳 𝗢𝗿 𝗩𝗶𝗱𝗲𝗼 𝗟𝗲𝘀𝘀 𝗧𝗵𝗮𝗻 𝟱𝗠𝗕 𝗙𝗶𝗹𝗲 𝗦𝗶𝘇𝗲, 𝗜'𝗹𝗹 𝗨𝗽𝗹𝗼𝗮𝗱 𝗜𝘁 𝗧𝗼 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗽𝗵📤

⚙️𝗣𝗼𝘄𝗲𝗿𝗱 𝗕𝘆 :- <b>@AnonymousBotsInfinity</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back ↩️", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About 🧿", callback_data="about"),
                                  ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@epusthakalaya_bot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await bot.send_message(
               chat_id=message.chat.id,
               text="""𝗔𝗯𝗼𝘂𝘁 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗽𝗵 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗿 𝗥𝗼𝗯𝗼𝘁 🇱🇰

✨ <b>My Name :</b> 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗽𝗵 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗿 𝗥𝗼𝗯𝗼𝘁 🇱🇰
👨‍💻 <b>Developer :</b> 𝙺𝚒𝚜𝚊𝚛𝚊 𝙿𝚎𝚜𝚊𝚗𝚓𝚒𝚝𝚑
🍀 <b>Data Base :</b> Mango DB
📝 <b>Language :</b> Python3
🧰 <b>Framework :</b> Pyrogram
📡 <b>Server :</b> Heroku
🌹 <b>Build Status :</b> 𝚅2.5

⚙️𝗣𝗼𝘄𝗲𝗿𝗱 𝗕𝘆 :- <b>@AnonymousBotsInfinity</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back ↩️", callback_data="help"),
                                        InlineKeyboardButton('🔐 Source Code 🔐', url='https://github.com/KisaraPesanjithPerera/Captain-Price')
                                ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@epusthakalayabots.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("Uploading To Telegraph 🔼...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("📸 Photo Size Should Be Less Than 5MB!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!**\n\n👉<code>https://telegra.ph{response[0]}</code>\n\n⚙️𝗣𝗼𝘄𝗲𝗿𝗱 𝗕𝘆 :- @AnonymousBotsInfinity',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@epusthakalaya_bots.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("Uploading To Telegraph 🔼...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("📹 Video Size Should Be Less Than 5MB!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!**\n\n👉<code>https://telegra.ph{response[0]}</code>\n\n⚙️𝗣𝗼𝘄𝗲𝗿𝗱 𝗕𝘆 :- @AnonymousBotsInfinity',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@epusthakalaya_bots.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("Uploading To Telegraph 🔼...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("🏞 Gif Size Should Be Less Than 5MB!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!**\n\n👉<code>https://telegra.ph{response[0]}</code>\n\n⚙️𝗣𝗼𝘄𝗲𝗿𝗱 𝗕𝘆 :- @AnonymousBotsInfinity',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Jebot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
⚙️𝗣𝗼𝘄𝗲𝗿𝗱 𝗕𝘆 :- @AnonymousBotsInfinity
"""
)

bot.run()
