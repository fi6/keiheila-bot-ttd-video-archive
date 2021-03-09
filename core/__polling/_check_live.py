from __future__ import annotations

from core.uplist import roomlist
from core.types import LiveInfo
from bilibili_api import live, user
import time
from cacheout import Cache
from random import randint

living_cache = Cache(ttl=120, default=None)


def check_living() -> LiveInfo | None:
    sleep_time = 1 + randint(0, 5)
    for id in roomlist.values():
        last_info: LiveInfo = living_cache.get(id)
        if not last_info:
            living_cache.set(id, LiveInfo(live.get_room_play_info(id)))
            continue
        if last_info.live_status == 0:
            info = LiveInfo(live.get_room_play_info(int(id)))
            living_cache.set(id, info)
            if info.live_status == 1:
                # just start living
                info.add_extra(user.get_user_info(id))
                return info
        time.sleep(sleep_time)
    return None
