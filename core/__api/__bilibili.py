from datetime import date, datetime, timedelta
from typing import Any, Callable, List
from bilibili_api import live, user, video
from core.types import LiveInfo
import logging
import asyncio


class __Bilibili():
    interval = 1
    jitter = 0.5
    last_time = datetime.now()

    async def check_frequency(self):
        if datetime.now() - self.last_time < timedelta(seconds=self.interval):
            self.last_time = datetime.now()
            await asyncio.sleep(self.interval)
        else:
            self.last_time = datetime.now()
        return

    async def add_user_info(self, info: LiveInfo):
        await self.check_frequency()
        user_info = user.get_user_info(info.mid)
        logging.info('live start user info : {info}'.format(info=user_info))
        info.add_extra(user_info)
        return info

    async def get_live_info(self, room_display_id: int):
        await self.check_frequency()
        info = live.get_room_play_info(room_display_id)
        return info

    async def get_user_videos(self, uid: int):
        await self.check_frequency()
        return user.get_videos_g(uid, order='pubdate')

    async def get_video_info(self, bvid: str):
        await self.check_frequency()
        return video.get_video_info(bvid=bvid)

    async def get_video_tags(self, bvid: str):
        await self.check_frequency()
        return video.get_tags(bvid=bvid)
