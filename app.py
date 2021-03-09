import asyncio
import core
import logging
from functions import bot

logging.basicConfig(level=logging.INFO)


# @bot.command(name='echo')
# async def func(session: Session):
#     logging.info(await session.reply(f'{session.args}'))
#     return None

# # everything done, go ahead now!
async def run_bot():
    bot.run()


async def main():
    await asyncio.gather(run_bot(), core.polling.start())


asyncio.run(main())

# async def main():
#     async with asyncio.Semaphore(5):
#         asyncio.ensure_future(main())
#         bot.run()

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         asyncio.ensure_future(main())
#         loop.run_forever()
#     finally:
#         loop.run_until_complete(loop.shutdown_asyncgens())
#         loop.close()
