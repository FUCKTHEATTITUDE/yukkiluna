import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
import random
from random import choice
import string
from YukkiMusic import cloner, MUSIC_BOT_NAME
from config import API_ID, API_HASH
from pyrogram import Client
from pyrogram.types import BotCommand
import config
from strings import get_command
from ..logging import LOGGER

cloner = "6183502276:AAGZVPG5vPEb8RFFsW41g-SstFLgXY75SuU"
##Copy from here 
@Client.on_message((filters.regex(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}')) & filters.private)
async def on_clone(self, message):
    user_id = message.from_user.id 
    user_name = message.from_user.first_name
    bot_token = re.findall(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}', message.text, re.IGNORECASE)
    bot_token = bot_token[0] if bot_token else None
    bot_id = re.findall(r'\d[0-9]{8,10}', message.text)

    if not str(message.forward_from.id) != "93372553":
        msg = await message.reply_text(f"🔑 <code>{bot_token}</code>\n\nCopying system...")
        try:
            ai = Client(
                f"{bot_token}", API_ID, API_HASH,
                bot_token=bot_token,
                plugins={"root": "YukkiMusic.plugins"},
            )
            await ai.start()
            bot = await ai.get_me()
            details = {
                'bot_id': bot.id,
                'is_bot': True,
                'user_id': user_id,
                'name': bot.first_name,
                'token': bot_token,
                'username': bot.username
            }
            await msg.edit_text(f"✅ The bot @{bot.username} is now working like Groups Guard.\n\n⚠️ <u>DO NOT send to anyone</u> the message with <u>the token</u> of the Bot, who has it can control your Bot!\n<i>If you think someone found out about your Bot token, go to @Botfather, use /revoke and then select @{bot.username}</i>")
        except BaseException as e:
            await msg.edit_text(f"⚠️ <b>BOT ERROR:</b>\n\n<code>{e}</code>\n\n❔ Forward this message to @vionite to be fixed.")

### Commands
CLONE_COMMAND = get_command("CLONE_COMMAND")


@app.on_message(
    filters.command(CLONE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def clone(client, message: Message):
    chat_id = message.chat.id
    text = await message.reply_text("/clone")
    cmd = message.command
    phone = message.command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "YukkiMusic.plugins"})
        await client.start()
        user = await client.member.id()
        await message.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Now Add Your Bot And Assistant @{ASSUSERNAME} To Your Chat!\n\nThanks for Cloning.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
#End
##This code fit with every pyrogram Codes just import then @Client Xyz!
