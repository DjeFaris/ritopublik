import os
import re
from platform import python_version as y
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Kynan.events import register
from Kynan import telethn as tbot
from Kynan import (OWNER_USERNAME, BOT_USERNAME, )


PHOTO = "https://telegra.ph/file/ac39d453c8f9b93859009.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"┏━━━━━━━━━━━━━━━━━━━━┓\n"
  TEXT += f"┠➣ **ᴍᴀɴᴀɢᴇʀ ʙᴏᴛ**\n"
  TEXT += f"┠➣ **ᴍʏ ᴏᴡɴᴇʀ : [OWNER](https://t.me/{OWNER_USERNAME})**\n"
  TEXT += f"┠➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`\n"
  TEXT += f"┠➣ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n"
  TEXT += f"┠➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
  TEXT += f"┠➣ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n"
  TEXT += "┗━━━━━━━━━━━━━━━━━━━━┛"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/{BOT_USERNAME}?start=help"), Button.url("ᴅᴏɴᴀsɪ ​❤️", "https://telegra.ph/file/67d31a4224e3e0211448a.jpg")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
