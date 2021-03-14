import asyncio
import time

from chinese_calendar.utils import is_workday
from utils.date import get_cn_time
from apscheduler.events import EVENT_JOB_ERROR
from pyee import AsyncIOEventEmitter
import pytz
from . import _check_live
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
    start_flag: bool = True
    scheduler = AsyncIOScheduler(
        {'apscheduler.timezone': pytz.timezone('Asia/Shanghai')})

    def __init__(self, loop=None):
        super().__init__(loop=loop)
        # self.scheduler.start(paused=True)
        # self.live_check_job = self.scheduler.add_job(self.check_living,
        #                                              'interval',
        #                                              seconds=2.7,
        #                                              jitter=0.5)
        # self.video_check_job = self.scheduler.add_job(self.check_video,
        #                                               'interval',
        #                                               seconds=180,
        #                                               jitter=20)
        # self.scheduler.add_listener(self.__job_listener, EVENT_JOB_ERROR)
        # logging.getLogger('apscheduler').setLevel(logging.ERROR)

    async def start(self):
        logging.info('polling start')
        asyncio.create_task(self.check_live_start())
        asyncio.get_event_loop().create_task(self.check_video_start())
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

    async def check_live_start(self):
        while True:
            await asyncio.sleep(1)

            if not self.start_flag:
                continue
            # print('flag true')
            try:
                # raise Exception('test')
                now = get_cn_time()
                if now.hour <= 18 and is_workday(now):
                    continue
                elif now.hour < 8:
                    continue
                live_info = await _check_live.check()
                if live_info:
                    self.emit('live_start', live_info)
            except Exception as e:
                logging.exception(e)
                self.pause()
                asyncio.get_event_loop().call_later(1800, self.resume)

    def pause(self):
        self.start_flag = False
        logging.info('polling paused')

    def resume(self):
        self.start_flag = True
        logging.info('polling resumed')

    async def check_video_start(self):
        cnt = 11
        while True:
            await asyncio.sleep(1.1)
            if not self.start_flag:
                continue
            cnt += 1
            # print('polling video')
            await self._check_video(1)
            if cnt % 3 == 0:
                asyncio.get_event_loop().create_task(self._check_video(0))
            if cnt >= 12:
                asyncio.get_event_loop().create_task(self._check_video(-1))
                cnt = 0
            await asyncio.sleep(180)

    async def _check_video(self, priority):
        if priority == 0:
            await asyncio.sleep(1)
        elif priority == -1:
            await asyncio.sleep(2)
        async for video in check_video(priority):
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
