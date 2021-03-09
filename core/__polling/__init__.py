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
            living = check_living()
            if living:
                logging.info(
                    'live start event found {user}'.format(user=living.name))
                self.emit('live_start', living)
            if self.counter == 15:
                self.counter = 0
                for video in check_video():
                    logging.info('new video: {user} {title}'.format(
                        user=video.author, title=video.title))
                    self.emit('video_update', video)
            self.counter += 1
            # if interrupted:
            #     break


polling = __Polling()
