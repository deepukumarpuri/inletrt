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
**Hello đ {}

I'm a Text To Speech Bot

For more click help.... 

đ¤ Developer : [Anonymous](https://t.me/DKBOTZHELP)**
"""
    ABOUT_TEXT = """
**My Name : Text To Speech Bot
â Developed By : [Anonymous](https://t.me/DKBOTZHELP)
â Updates Channel : [DK BOTZ](https://t.me/DKBOTZ)
â Support : [DK BOTZ Support](https://t.me/DK_BOTZ)
â Language : [Python 3](https://www.python.org)
â Library : [Pyrogram](https://docs.pyrogram.org)
â Server : [Heroku](https://heroku.com)

ÂŠī¸ Made By @DKBOTZ â¤ī¸**
"""

    HELP_TEXT = """**Hello đ, Follow these Steps..

đ Send me any Text..

đ Select the Select Your Language

đ I will Convert To Voice And Send You

â¨ **Available Commands** â¨

đ /about - About The Bot

đ /help - How To Use Bot

đ /start - Start the Bot

đ /pop - Delete Your Data...

đ /lang - Select Your Language

ÂŠ @DKBOTZ â¤ī¸**
"""

