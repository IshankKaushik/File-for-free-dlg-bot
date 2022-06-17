# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyrogram.types import ReplyKeyboardMarkup

                      
@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**JOIN MY UPDATES CHANNEL TO USE ME..**\n\n**THIS IS VIP BOT, ONLY VIP CHANNEL SUBSCRIBERS CAN USE THIS BOT..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("JOIN UPDATES CHANNEL.. (click here)", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text="**𝙷𝙴𝙻𝙻𝙾...⚡**\n\n**𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙵𝙸𝙻𝙴/𝚅𝙸𝙳𝙴𝙾 𝚃𝙾 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙻𝙸𝙽𝙺 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙾𝚁 𝙱𝙾𝚃.**\n\n**𝙸 𝙲𝙰𝙽 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙴 𝙳𝙸𝚁𝙴𝙲𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾/𝙵𝙸𝙻𝙴𝚂 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙾𝙽𝙻𝙸𝙽𝙴 & 𝙵𝙾𝚁 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶..\n\n𝚄𝚂𝙴 /help 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝙳𝙴𝚃𝙰𝙸𝙻𝚂...\n\n𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾/𝙵𝙸𝙻𝙴 𝚃𝙾 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚉....**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🧑‍💻 DEVELOPER 🧑‍💻", url="https://t.me/ishank_kaushik"), InlineKeyboardButton("🛠️ WEBSITE 🛠️", url="https://www.ishank.ml")],
                   
                ]
            ),
            disable_web_page_preview=True
        )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**JOIN MY UPDATES CHANNEL TO USE ME..**\n\n**THIS IS VIP BOT, ONLY VIP CHANNEL SUBSCRIBERS CAN USE THIS BOT..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("JOIN UPDATES CHANNEL.. (click here)", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]                           
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text = "**YOUR LINK IS GENERATED...⚡\n\n📧 FILE NAME :-\n{}\n {}\n\n📥 DOWNLOAD LINK :- {}\n\n♻️ 𝚃𝙷𝙸𝚂 𝙻𝙸𝙽𝙺 𝙸𝚂 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙰𝙽𝙳 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙴𝚇𝙿𝙸𝚁𝙴 ♻️\n\n@Ishank_Kaushik**"
        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙽𝙾𝚆 ⚡", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**JOIN MY UPDATES CHANNEL TO USE ME..**\n\n**THIS IS VIP BOT, ONLY VIP CHANNEL SUBSCRIBERS CAN USE THIS BOT..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("JOIN UPDATES CHANNEL.. (click here)", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="**┣⪼ SEND ME ANY FILE/VIDEO THEN I WILL GIVE YOU PERMANENT SHAREABLE LINK OF IT...\n\n┣⪼ THIS LINK CAN BE USED TO DOWNLOAD OR TO STREAM USING EXTERNAL VIDEO PLAYERS THROUGH MY SERVER.\n\n┣⪼ FOR STREAMING JUST COPY THE LINK AND PASTE IT IN YOUR VIDEO PLAYER TO START STREAMING.\n\n┣⪼ THIS BOT IS CREATED BY @Ishank_Kaushik, YOU HAVE TO BUY KEYS TOH USE THIS BOT../\n\n┣⪼ FOR MORE INFORMATION :- /about\n\n\nTHANKS FOR READING**", 
  parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🧑‍💻 DEVELOPER 🧑‍💻", url="https://t.me/ishank_kaushik"), InlineKeyboardButton("🛠️ WEBSITE 🛠️", url="https://www.ishank.ml")],
               
            ]
        )
    )

@StreamBot.on_message(filters.command('about') & filters.private & ~filters.edited)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**JOIN MY UPDATES CHANNEL TO USE ME..**\n\n**THIS IS VIP BOT, ONLY VIP CHANNEL SUBSCRIBERS CAN USE THIS BOT..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("JOIN UPDATES CHANNEL.. (click here)", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b>𝚂𝙾𝙼𝙴𝚃𝙷𝙸𝙽𝙶 𝙰𝙱𝙾𝚄𝚃 𝙼𝙴</b>
<b>╭━━━━━━━〔TFM-SERVER BOT〕</b>
┃
┣⪼<b>BOT-NAME : <a href='https://t.me/tfm_server_bot'>TFM-SERVER BOT</a></b>
┣⪼<b>UPDATES : <a href='https://t.me/MWUpdatez'></a></b>
┣⪼<b>SUPPORT : <a href='https://t.me/OpusTechz'>𝙾𝙿𝚄𝚂-𝚃𝙴𝙲𝙷𝚉</a></b>
┣⪼<b>SERVER : 𝙷𝙴𝚁𝚄𝙺𝙾</b>
┣⪼<b>LIBRARY : 𝙿𝚁𝙾𝙶𝚁𝙰𝙼</b>
┣⪼<b>LANGUAGE: 𝙿𝚈𝚃𝙷𝙾𝙽 3</b>
┣⪼<b>SOURCE-CODE : <a href='https://t.me/ishank_kaushim'>YOU HAVE TO BUY IT</a></b>
┣⪼<b>INSTAGRAM : <a href='https://instagram.com/its_ishank'>its_Ishank</a></b>
┃
<b>╰━━━━━━━〔YOU HAVE TO BUY KEYS TO USE THIS BOT〕</b>""",
  parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🧑‍💻 DEVELOPER 🧑‍💻", url="https://t.me/ishank_kaushik"), InlineKeyboardButton("🛠️ WEBSITE 🛠️", url="https://www.ishank.ml")],
               
            ]
        )
    )
