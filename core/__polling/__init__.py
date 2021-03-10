import asyncio
import time

from chinese_calendar.utils import is_workday
from utils.date import get_cn_time
from apscheduler.events import EVENT_JOB_ERROR
from pyee import AsyncIOEventEmitter
import pytz
from ._check_live import check_living
from ._check_video import check_video
import signal
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from chinese_calendar import is_holiday

# def signal_handler(signal, frame):
#     global interrupted
#     interrupted = True

# signal.signal(signal.SIGINT, signal_handler)

# interrupted = False


class __Polling(AsyncIOEventEmitter):
    counter: int = 0

    scheduler = AsyncIOScheduler(
        {'apscheduler.timezone': pytz.timezone('Asia/Shanghai')})

    def __init__(self, loop=None):
        super().__init__(loop=loop)
        self.scheduler.start(paused=True)
        self.live_check_job = self.scheduler.add_job(self.check_living,
                                                     'interval',
                                                     seconds=2.7,
                                                     jitter=0.5)
        self.video_check_job = self.scheduler.add_job(self.check_video,
                                                      'interval',
                                                      seconds=180,
                                                      jitter=20)
        self.scheduler.add_listener(self.__job_listener, EVENT_JOB_ERROR)
        logging.getLogger('apscheduler').setLevel(logging.WARNING)

    async def check_living(self):
        now = get_cn_time()
        if now.hour <= 18 and is_workday(now):
            return
        elif now.hour < 8:
            return
        # raise Exception('error test')
        return await check_living()

    async def start(self):
        logging.info('polling start')
        self.scheduler.resume()
        # while True:
        #     try:
        #         living = await check_living()
        #         if living:
        #             self.emit('live_start', living)
        #             logging.info('emit live_start event')
        #         if self.counter == 15:
        #             self.counter = 0
        #             asyncio.create_task(self.check_video())
        #         self.counter += 1
        #     except Exception as e:
        #         time.sleep(3600)
        #         logging.exception(e)
        # if interrupted:
        #     break

    async def check_video(self):
        async for video in check_video():
            logging.info('new video: {user} {title}'.format(user=video.author,
                                                            title=video.title))
            self.emit('video_update', video)

    def __job_listener(self, event):
        if event.exception:
            logging.exception('event exception found: {exception}'.format(
                exception=event.exception))
            self.scheduler.pause()
            asyncio.get_event_loop().call_later(1200, self.scheduler.resume)


polling = __Polling()
