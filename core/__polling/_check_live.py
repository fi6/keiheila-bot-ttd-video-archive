from __future__ import annotations

from core.uplist import uplist, roomlist
from core.types import LiveInfo
from bilibili_api import live, user
import time
from cacheout import Cache

living_cache = Cache(ttl=120, default=None)


def check_living() -> LiveInfo | None:
    sleep_time = 20 / len(roomlist)
    for id in uplist.values():
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
