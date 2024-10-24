import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "28713982")
    API_HASH  = os.environ.get("API_HASH", "237e15f7c006b10b4fa7c46fee7a5377")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6110777488:AAHYEdx1lqPfiq5tUYDI87DomLz7TKoQgUw") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'AshutoshGoswami24,BotzPW').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    PORT = int(os.environ.get("PORT", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """ʜᴇʏ {} 
    
➻ 🫧 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ!.
    
➻ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ғɪʟᴇ

➻ ᴛʜɪs ʙᴏᴛ ᴀʟsᴏ sᴜᴘᴘᴏʀᴛs ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ
    
➻ ᴜsᴇ /ᴛᴜᴛᴏʀɪᴀʟ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ.

<b>ʙᴏᴛ ɪs ᴍᴀᴅᴇ ғᴏʀ ᴘᴜʙʟɪᴄ ᴜsᴇ ᴀɴᴅ ᴜsᴇ ᴄᴀɴ ᴀʟsᴏ ʀᴇɴᴀᴍᴇ 𝟷𝟾+ ᴄᴏɴᴛᴇɴᴛ ᴀʟsᴏ</b>

<b><a href='https://t.me/Anime_Madness'>/ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ</a></b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ `[episode]` :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴇᴘɪsᴏᴅᴇ ɴᴜᴍʙᴇʀ
✓ `[quality]` :- ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴠɪᴅᴇᴏ ʀᴇsᴏʟᴜᴛɪᴏɴ

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S01[episode] [quality][Dual Audio] @Anime_Madness</code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 ʟᴀɴɢᴜᴀɢᴇ :</b> <a href='https://python.org'>Python 3</a>
<b>📚 ʟɪʙʀᴀʀʏ :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 sᴇʀᴠᴇʀ :</b> <a href='https://heroku.com'>Heroku</a>
<b>🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b> <a href='https://t.me/LUFFY1JOYBOY'>ʟᴀᴡ sᴇɴᴘᴀɪ</a>
    
<b>♻️ Bot Made By :</b> @LUFFY1JOYBOY"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  ʜᴏᴡ ᴛᴏ sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>
    
⦿ ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ sɪᴍᴘʟʏ ʙʏ sᴇɴᴅɪɴɢ A ᴘʜᴏᴛᴏ ᴛᴏ Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🤖 ᴀɴɪᴍᴇ: @Anime_Madness
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>🥲 ᴛʜᴀɴᴋs  ғᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ! ❤️</b>
    
ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ʙᴏᴛs & ᴘʀᴏᴊᴇᴄᴛs, ʏᴏᴜ ᴄᴀɴ 🎁 ᴅᴏɴᴀᴛᴇ ᴍᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ғʀᴏᴍ 𝟷𝟶 ʀs ᴜᴘᴛᴏ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.
    
<b>ғᴏʀ ᴅᴏɴᴀᴛɪᴏɴ - ᴅᴍ @LUFFY1JOYBOY</b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
ᴊᴏɪɴ @Anime_Madness ᴛᴏ ʜᴇʟᴘ """





