import platform

from LegendBS.start import start_cmd
from pyrogram import Client
from pyrogram import __version__ as py_version
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from LegendGirl.Config import *

from ..core.clients import *

if START_PIC:
    START_PIC = START_PIC
else:
    START_PIC = "https://graph.org/file/d482f9ae1a0abf905c50d.jpg"


@Client.on_message(filters.command(["start"], prefixes=HANDLER))
async def _start(Legend: Client, message: Message):
    global START_MESSAGE
    my_detail = await Legend.get_me()
    my_mention = my_detail.mention
    if START_MESSAGE:
        START_MESSAGE = START_MESSAGE
    else:
        START_MESSAGE = f"Hᴇʏ! 🦋 {message.from_user.mention}❤️\n✥ I Aᴍ {my_mention}\n\n❖═══❃≛⃝❈•✵•≛⃝❈❃═══❖\n\n✥ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ** = {py_version}\n✥ **Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ** = {platform.python_version()}\n✥ **BᴏᴛSᴘᴀᴍ Vᴇʀsɪᴏɴ** = {version}\n\n❖═══❃≛⃝❈•✵•≛⃝❈❃═══❖"
    if ".jpg" in START_PIC or ".png" in START_PIC:
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_photo(
                    message.chat.id,
                    START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
                )
    elif ".mp4" in START_PIC.lower():
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_video(
                    message.chat.id,
                    START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
                )
    else:
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_message(
                    message.chat.id,
                    START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
                )
