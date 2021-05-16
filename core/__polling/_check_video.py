import asyncio
import core
from datetime import datetime
import logging
from random import random
from typing import List

from core.types import UserVideo
from models import VideoUpdate, VerifiedUp


async def check_video(priority: int):
    # get up list
    ups: List[VerifiedUp] = VerifiedUp.objects(tag='video', priority=priority)
    uplist = [up.uid for up in ups]
    # calculate sleep time
    sleep_time = 180 * (1.5 - priority * 0.5) / len(uplist) + 2 * random()
    logging.info('priority: {p}, up list total: {total}'.format(
        p=priority, total=len(uplist)))
    for id in uplist:
        existing = VideoUpdate.objects(
            uid=id).order_by('-publish').only('bvid')[:5]
        bvids = [v.bvid for v in existing]
        cnt = 0
        for vid in await core.api.bilibili.get_user_videos(int(id)):
            vid = UserVideo(**vid)
            if cnt >= 3:
                break
            cnt += 1
            if vid.bvid in bvids:
                continue
            vid_all = await core.api.bilibili.get_video_info(vid.bvid)
            tags = await core.api.bilibili.get_video_tags(vid.bvid)
            tag_names: List[str] = [t['tag_name'] for t in tags]
            if '任天堂明星大乱斗' not in tag_names:
                logging.debug((vid_all, tag_names))
                continue
            vid_doc = create_video_doc(vid_all, tag_names)
            # print(vid_doc)
            yield vid_doc
            logging.info('added new video: {vid}'.format(vid=vid_all))
            await asyncio.sleep(random())

        await asyncio.sleep(sleep_time)


def create_video_doc(vid_all, tag_names):
    fields = VideoUpdate._fields.keys()
    vid_doc = VideoUpdate(**{k: v for k, v in vid_all.items() if k in fields})
    vid_doc._raw = vid_all
    vid_doc.publish = datetime.fromtimestamp(vid_all['pubdate'])
    vid_doc.uid = vid_all['owner']['mid']
    vid_doc.tags = tag_names
    vid_doc.author = vid_all['owner']['name']
    up = VerifiedUp.objects(uid=vid_doc.uid)
    if len(up):
        vid_doc.up_ref = up[0]
    vid_doc.save()
    return vid_doc
