import logging
import asyncio
logging.basicConfig(level=logging.INFO)


async def main():
    import core
    from functions import bot
    asyncio.create_task(core.polling.start())
    bot.run()


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
