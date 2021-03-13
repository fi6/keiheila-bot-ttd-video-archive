from __future__ import annotations
import asyncio
import logging

from core.uplist import roomlist
from core.types import LiveInfo
from bilibili_api import live, user
from cacheout import Cache
import random

living_cache = Cache(ttl=300, default=None)


async def check() -> LiveInfo | None:
    sleep_time = 1 + random.random() * 0.2
    for i, id in enumerate(roomlist.values()):
        last_info: LiveInfo | None = living_cache.get(id)
        if not last_info:
            info = LiveInfo(live.get_room_play_info(id))
            logging.info('{mid} expired in cache'.format(mid=info.mid))
            living_cache.set(id, info)
            continue
        elif last_info.live_status != 1:
            info = LiveInfo(live.get_room_play_info(int(id)))
            living_cache.set(id, info)
            # logging.debug(living_cache.expire_times())
            if info.live_status == 1:
                # just start living
                user_info = user.get_user_info(info.mid)
                logging.info(
                    'live start user info : {info}'.format(info=user_info))
                info.add_extra(user_info)
                return info
        elif last_info.live_status == 1:
            pass
            # logging.debug('living')
        if i == len(roomlist.values()) - 1:
            break
        await asyncio.sleep(sleep_time)

    return None


def get_room_info():
    pass