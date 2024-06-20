import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from LoverMusic import LOGGER, app, userbot
from LoverMusic.core.call import Anony
from LoverMusic.misc import sudo
from LoverMusic.plugins import ALL_MODULES
from LoverMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("LoverMusic").error(
            "No Pyrogram String Defined !!..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("LoverMusic").warning(
            "Spotify Queries Not Working Without Spotify ID & Secret."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AnonXMusic.plugins" + all_module)
    LOGGER("LoverMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("LoverMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Kaal.decorators()
    LOGGER("LoverMusic").info("Congratulations, Your LoverMusic Bot Now Deployed ...")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
