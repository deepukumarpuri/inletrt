# (c) @DKBOTZHELP
# This is very simple Telegram Bot.
# Coded by a Pro Developer.


import os
import time
from configs import Config
from pyrogram import Client, filters
from helpers.database.access_db import db
from helpers.database.add_user import AddUserToDatabase
from helpers.forcesub import ForceSub
from helpers.broadcast import broadcast_handler
from pyrogram.errors import FloodWait, UserNotParticipant, MessageNotModified
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, InputMediaPhoto

QueueDB = {}
ReplyDB = {}
FormtDB = {}
NubBot = Client(
    session_name=Config.SESSION_NAME,
    api_id=int(Config.API_ID),
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

START_BUTTONS = InlineKeyboardMarkup(
            [[InlineKeyboardButton("📮 UPDATE CHANNEL", url="https://t.me/DKBOTZ")],
             [InlineKeyboardButton("ℹ️ Help", callback_data="help"),
              InlineKeyboardButton("🤖 About", callback_data="about"), 
              InlineKeyboardButton("⛔ Close", callback_data="close")], 
             ]
          )

HELP_BUTTONS = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🏡 Home", callback_data="home"),
                 InlineKeyboardButton("🤖 About", callback_data="about"),
                 InlineKeyboardButton("⛔ Close", callback_data="close")]
            ]
        )

ABOUT_BUTTONS = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📮 Feedback Dev", url="https://t.me/DKBOTZHELP")],
                [InlineKeyboardButton("🏡 Home", callback_data="home"),
                 InlineKeyboardButton("⛔ Close", callback_data="close")]
            ]
        )
@NubBot.on_message(filters.private & filters.command("start"))
async def start_handler(bot: Client, m: Message, cb=False):
    await AddUserToDatabase(bot, m)
    FSub = await ForceSub(bot, m)
    if FSub == 400:
        return
    if not cb:
        send_msg = await m.reply_text("**👀 Processing......**", quote=True)    
    await send_msg.edit(
      text=f"{Config.START_TEXT}".format(m.from_user.mention), 
      reply_markup=START_BUTTONS, 
      disable_web_page_preview=True
       )
    if cb:
        return await m.message.edit(
                 text=f"{Config.START_TEXT}".format(m.from_user.mention),
                 reply_markup=START_BUTTONS,
                 disable_web_page_preview=True
                     )
@NubBot.on_message(filters.private & filters.command("help"))
async def help_handler(bot: Client, m: Message, cb=False):
    await AddUserToDatabase(bot, m)
    FSub = await ForceSub(bot, m)
    if FSub == 400:
        return
    if not cb:
        send_msg = await m.reply_text("**👀 Processing......**", quote=True)    
    await send_msg.edit(
      text=f"{Config.HELP_TEXT}".format(m.from_user.mention), 
      reply_markup=HELP_BUTTONS, 
      disable_web_page_preview=True
       )
    if cb:
        return await m.message.edit(
                 text=f"{Config.HELP_TEXT}".format(m.from_user.mention),
                 reply_markup=HELP_BUTTONS,
                 disable_web_page_preview=True
                     )
    
@NubBot.on_message(filters.private & filters.command("about"))
async def about_handler(bot: Client, m: Message, cb=False):
    await AddUserToDatabase(bot, m)
    FSub = await ForceSub(bot, m)
    if FSub == 400:
        return
    if not cb:
        send_msg = await m.reply_text("**👀 Processing......**", quote=True)    
    await send_msg.edit(
      text=f"{Config.ABOUT_TEXT}", 
      reply_markup=ABOUT_BUTTONS, 
      disable_web_page_preview=True
       )
    if cb:
        return await m.message.edit(
                 text=f"{Config.ABOUT_TEXT}",
                 reply_markup=ABOUT_BUTTONS,
                 disable_web_page_preview=True
                     )

@NubBot.on_message(filters.private & filters.command("broadcast") & filters.reply & filters.user(Config.BOT_OWNER) & ~filters.edited)
async def _broadcast(_, m: Message):
    await broadcast_handler(m)


@NubBot.on_message(filters.private & filters.command("status") & filters.user(Config.BOT_OWNER))
async def _status(_, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await m.reply_text(
        text=f"**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Total Users in DB: {total_users}**",
        parse_mode="Markdown",
        quote=True
    )


@NubBot.on_message(filters.private & filters.command("check") & filters.user(Config.BOT_OWNER))
async def check_handler(bot: Client, m: Message):
    if len(m.command) == 2:
        editable = await m.reply_text(
            text="**Checking User Details...**"
        )
        user = await bot.get_users(user_ids=int(m.command[1]))
        detail_text = f"**Name:** [{user.first_name}](tg://user?id={str(user.id)})\n" \
                      f"**Username:** `{user.username}`\n" \
                      f"**Upload as Doc:** `{await db.get_upload_as_doc(id=int(m.command[1]))}`\n" \
                      f"**Generate Screenshots:** `{await db.get_generate_ss(id=int(m.command[1]))}`\n"
        await editable.edit(
            text=detail_text,
            parse_mode="Markdown",
            disable_web_page_preview=True
        )

@NubBot.on_message(filters.private & filters.command("ban_user") & filters.user(Config.BOT_OWNER))
async def ban(c: Client, m: Message):
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to ban any user from the bot.\n\nUsage:\n\n`/ban_user user_id ban_duration ban_reason`\n\nEg: `/ban_user 1234567 28 You misused me.`\n This will ban user with id `1234567` for `28` days for the reason `You misused me`.",
            quote=True
        )
        return
    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = ' '.join(m.command[3:])
        ban_log_text = f"Banning user {user_id} for {ban_duration} days for the reason {ban_reason}."
        try:
            await c.send_message(
                user_id,
                f"You are banned to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin**"
            )
            ban_log_text += '\n\nUser notified successfully!'
        except:
            traceback.print_exc()
            ban_log_text += f"\n\nUser notification failed! \n\n`{traceback.format_exc()}`"
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(
            ban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


@NubBot.on_message(filters.private & filters.command("unban_user") & filters.user(Config.BOT_OWNER))
async def unban(c: Client, m: Message):
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to unban any user.\n\nUsage:\n\n`/unban_user user_id`\n\nEg: `/unban_user 1234567`\n This will unban user with id `1234567`.",
            quote=True
        )
        return
    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user {user_id}"
        try:
            await c.send_message(
                user_id,
                f"Your ban was lifted!"
            )
            unban_log_text += '\n\nUser notified successfully!'
        except:
            traceback.print_exc()
            unban_log_text += f"\n\nUser notification failed! \n\n`{traceback.format_exc()}`"
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(
            unban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


@NubBot.on_message(filters.private & filters.command("banned_users") & filters.user(Config.BOT_OWNER))
async def _banned_usrs(_, m: Message):
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ''
    async for banned_user in all_banned_users:
        user_id = banned_user['id']
        ban_duration = banned_user['ban_status']['ban_duration']
        banned_on = banned_user['ban_status']['banned_on']
        ban_reason = banned_user['ban_status']['ban_reason']
        banned_usr_count += 1
        text += f"> **user_id**: `{user_id}`, **Ban Duration**: `{ban_duration}`, **Banned on**: `{banned_on}`, **Reason**: `{ban_reason}`\n\n"
    reply_text = f"Total banned user(s): `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open('banned-users.txt', 'w') as f:
            f.write(reply_text)
        await m.reply_document('banned-users.txt', True)
        os.remove('banned-users.txt')
        return
    await m.reply_text(reply_text, True)



NubBot.run()
