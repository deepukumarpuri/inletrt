# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    USER_ID = os.environ.get("USER_ID")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
    MONGODB_URI = os.environ.get("MONGODB_URI")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))

    START_TEXT = """
**Hello 👋 {}

I'm a Text To Speech Bot

For more click help.... 

🤖 Developer : [Anonymous](https://t.me/DKBOTZHELP)**
"""
    ABOUT_TEXT = """
**My Name : Text To Speech Bot
● Developed By : [Anonymous](https://t.me/DKBOTZHELP)
● Updates Channel : [DK BOTZ](https://t.me/DKBOTZ)
● Support : [DK BOTZ Support](https://t.me/DK_BOTZ)
● Language : [Python 3](https://www.python.org)
● Library : [Pyrogram](https://docs.pyrogram.org)
● Server : [Heroku](https://heroku.com)

©️ Made By @DKBOTZ ❤️**
"""

    HELP_TEXT = """**Hello 👋, Follow these Steps..

🌀 Send me any Text..

🌀 Select the Select Your Language

🌀 I will Convert To Voice And Send You

✨ **Available Commands** ✨

🌀 /about - About The Bot

🌀 /help - How To Use Bot

🌀 /start - Start the Bot

🌀 /pop - Delete Your Data...

🌀 /lang - Select Your Language

© @DKBOTZ ❤️**
"""

