import asyncio
import logging
from random import random
from typing import List

from core.types import UserVideo
from bilibili_api import user, video
from models import Video, VerifiedUp


async def check_video(priority: int):
    ups: List[VerifiedUp] = VerifiedUp.objects(tag='video', priority=priority)
    uplist = [up.uid for up in ups]
    sleep_time = 300 / len(uplist) + 2 * random()
    for id in uplist.values():
        existing = Video.objects(mid=id).order_by('-pubdate').only('bvid')[:5]
        bvids = [v.bvid for v in existing]
        cnt = 0
        for vid in user.get_videos_g(int(id), order='pubdate'):
            vid = UserVideo(**vid)
            if cnt >= 3:
                break
            cnt += 1
            if vid.bvid in bvids:
                continue
            vid_all = video.get_video_info(bvid=vid.bvid)
            tags: List[str] = video.get_tags(bvid=vid.bvid)
            fields = Video._fields.keys()
            vid_doc = Video(
                **{k: v
                   for k, v in vid_all.items() if k in fields})
            vid_doc.mid = vid_all['owner']['mid']
            vid_doc.tags = [t['tag_name'] for t in tags]
            vid_doc.author = vid_all['owner']['name']
            vid_doc.save()
            yield vid_doc
            logging.info('added new video: {vid}'.format(vid=vid_all))

        await asyncio.sleep(sleep_time)
