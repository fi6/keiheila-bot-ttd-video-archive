import asyncio
import time
from pyee import AsyncIOEventEmitter
from ._check_live import check_living
from ._check_video import check_video
import signal
import logging

# def signal_handler(signal, frame):
#     global interrupted
#     interrupted = True

# signal.signal(signal.SIGINT, signal_handler)

# interrupted = False


class __Polling(AsyncIOEventEmitter):
    counter: int = 0

    async def start(self):
        logging.info('polling start')
        while True:
            try:
                living = check_living()
                if living:
                    self.emit('live_start', living)
                    logging.info('emit live_start event')
                if self.counter == 15:
                    self.counter = 0
                    asyncio.create_task(self.check_video())
                self.counter += 1
            except Exception as e:
                time.sleep(3600)
                logging.exception(e)
            # if interrupted:
            #     break

    async def check_video(self):
        for video in check_video():
            logging.info('new video: {user} {title}'.format(user=video.author,
                                                            title=video.title))
            self.emit('video_update', video)


polling = __Polling()
