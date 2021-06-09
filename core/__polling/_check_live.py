from __future__ import annotations
import asyncio
import core
import logging

from core.uplist import roomlist
from core.types import LiveInfo
from cacheout import Cache
import random

living_cache = Cache(ttl=300, default=None)


async def check() -> LiveInfo | None:
    sleep_time = 5 + random.random() * 0.5
    for i, id in enumerate(roomlist.values()):
        last_info: LiveInfo | None = living_cache.get(id)
        if not last_info:
            info = LiveInfo(await core.api.bilibili.get_live_info(id))
            logging.info('{mid} expired in cache'.format(mid=info.mid))
            living_cache.set(id, info)
            continue
        elif last_info.live_status != 1:
            info = LiveInfo(await core.api.bilibili.get_live_info(id))
            living_cache.set(id, info)
            logging.info('checking live info for {id}'.format(id=id))
            # logging.debug(living_cache.expire_times())
            if info.live_status == 1:
                # just start living
                return await core.api.bilibili.add_user_info(info)
        elif last_info.live_status == 1:
            pass
            # logging.debug('living')
        if i == len(roomlist.values()) - 1:
            break
        await asyncio.sleep(sleep_time)

    return None


def get_room_info():
    pass