from pyrogram.types import InlineKeyboardButton


class Data:
    HELP_MENU1 = [
        [
            InlineKeyboardButton(text="⚜️ Bᴀɴᴀʟʟ ⚜️", callback_data="banall"),
            InlineKeyboardButton(text="📍 Bɪʀᴛʜᴅᴀʏ 📍", callback_data="birthday"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Pɪɴɢ ⚜️", callback_data="core_help1"),
            InlineKeyboardButton(text="📍 Rᴇsᴛᴀʀᴛ 📍", callback_data="core_help2"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Eᴠᴀʟ ⚜️", callback_data="evaluators_help1"),
            InlineKeyboardButton(text="📍 Exᴇᴄ 📍", callback_data="evaluators_help2"),
        ],
        [
            InlineKeyboardButton(
                text="⚜️ Gᴏᴏᴅ Mᴏʀɴɪɴɢ ⚜️", callback_data="gwish_help1"
            ),
            InlineKeyboardButton(text="📍 Gᴏᴏᴅ Aғᴛᴇʀɴᴏᴏɴ 📍", callback_data="gwish_help2"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Gᴏᴏᴅ Nɪɢʜᴛ ⚜️", callback_data="gwish_help3"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Rᴀɪᴅ ⚜️", callback_data="raid_help1"),
            InlineKeyboardButton(text="📍 Rᴇᴘʟʏ Rᴀɪᴅ📍", callback_data="raid_help2"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Dʀᴇᴘʟʏ Rᴀɪᴅ ⚜️", callback_data="raid_help3"),
            InlineKeyboardButton(text="📍 Lɪsᴛ Rᴀɪᴅ 📍", callback_data="raid_help4"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Sʜᴀʏʀɪ ⚜️", callback_data="shayri_help1"),
            InlineKeyboardButton(text="📍 Sᴛᴏᴘ 📍", callback_data="shayri_help2"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Sᴘᴀᴍ ⚜️", callback_data="spam_help1"),
            InlineKeyboardButton(text="📍 Dᴇʟᴀʏ Sᴘᴀᴍ 📍", callback_data="spam_help2"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Pᴏʀɴ Sᴘᴀᴍ ⚜️", callback_data="spam_help3"),
            InlineKeyboardButton(text="📍 Hᴀɴɢ Sᴘᴀᴍ 📍", callback_data="spam_help4"),
        ],
        [
            InlineKeyboardButton(text="⚜️ U Sᴘᴀᴍ ⚜️", callback_data="unlimited_help1"),
            InlineKeyboardButton(text="📍 U Rᴀɪᴅ 📍", callback_data="unlimited_help2"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Aʙᴜsᴇ ⚜️", callback_data="unlimited_help3"),
            InlineKeyboardButton(text="📍 Sᴛᴏᴘ 📍", callback_data="unlimited_help4"),
        ],
        [
            InlineKeyboardButton(text="⚜️ Eᴄʜᴏ ⚜️", callback_data="unlimited_help5"),
        ],
        [
            InlineKeyboardButton(text="🔒 Cʟᴏsᴇ", callback_data="close"),
        ],
    ]
    REVERT = [
        [
            InlineKeyboardButton("Rᴇᴏᴘᴇɴ Hᴇʟᴘ Mᴇɴᴜ", callback_data="helpmenu1"),
        ],
    ]
    HELP_MENU2 = [
        [
            InlineKeyboardButton(text="🔙 Pʀᴇᴠɪᴏᴜs", callback_data="helpmenu1"),
        ],
        [
            InlineKeyboardButton(text="Cʟᴏsᴇ ", callback_data="close"),
        ],
        [
            InlineKeyboardButton(text="Nᴇxᴛ ⏭️", callback_data="helpmenu3"),
        ],
    ]
    HELP_MENU3 = [
        [
            InlineKeyboardButton(text="🔙 Pʀᴇᴠɪᴏᴜs", callback_data="helpmenu2"),
        ],
        [
            InlineKeyboardButton(text="Cʟᴏsᴇ ", callback_data="close"),
        ],
        [
            InlineKeyboardButton(text="Nᴇxᴛ ⏭️", callback_data="helpmenu1"),
        ],
    ]
