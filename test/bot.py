import sys
sys.path.append('.')

from functions import bot


async def async_print(x):
    print(x)


bot.on_raw_event(async_print)
bot.run()