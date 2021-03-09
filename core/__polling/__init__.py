from pyee import AsyncIOEventEmitter
from ._check_live import check_living
from ._check_video import check_video
import signal


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


signal.signal(signal.SIGINT, signal_handler)

interrupted = False


class __Polling(AsyncIOEventEmitter):
    counter: int = 0

    async def start(self):
        while True:
            living = check_living()
            if living:
                self.emit('live_start', living)
            if self.counter == 10:
                self.counter = 0
                for video in check_video():
                    self.emit('video_update', video)
            self.counter += 1
            if interrupted:
                break


polling = __Polling()
