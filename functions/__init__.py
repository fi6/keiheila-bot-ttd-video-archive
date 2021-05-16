from khl.message import TextMsg
from ._entry import BotEntry
from ._instance import bot  # noqa
from .event import EventEntry
from . import notification  # noqa
from .video import VideoEntry

bot_entry = BotEntry(EventEntry())
bot.add_command(bot_entry)


@bot.on_text_msg
async def entry(msg: TextMsg):
    if '2114466526' in msg.mention and len(
            msg.mention) == 1 and msg.content.startswith('@'):
        args = msg.content.split()
        if not len(args) > 1:
            return
        args = args[1:]
        await bot_entry.execute(msg, *args)
