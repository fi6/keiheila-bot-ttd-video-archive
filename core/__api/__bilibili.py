from datetime import date, datetime, timedelta
from random import random
from typing import Any, Callable, Dict, List
from bilibili_api import live, user, video, Credential
from core.types import LiveInfo
import logging
import asyncio
from models import VideoArchive
import configs.auth


class __Bilibili():
    interval = 1
    jitter = 0.5
    last_time = datetime.now()
    verify = Credential(sessdata=configs.auth.bili_auth['sessdata'],
                        bili_jct=configs.auth.bili_auth['bili_jct'],
                        buvid3=configs.auth.bili_auth['buvid3'])

    async def check_frequency(self):
        if datetime.now() - self.last_time < timedelta(seconds=self.interval):
            self.last_time = datetime.now()
            await asyncio.sleep(self.interval + self.jitter * random())
        else:
            self.last_time = datetime.now()
        return

    async def add_user_info(self, info: LiveInfo):
        await self.check_frequency()
        u = user.User(uid=info.mid)
        user_info = await u.get_user_info()
        logging.info('live start user info : {info}'.format(info=user_info))
        info.add_extra(user_info)
        return info

    async def get_live_info(self, room_display_id: int):
        await self.check_frequency()
        lv = live.LiveRoom(room_display_id=room_display_id)
        info = lv.get_room_play_info()
        return await info

    async def get_user_videos(self, uid: int):
        await self.check_frequency()
        u = user.User(uid=uid)
        vids = await u.get_videos()
        if not vids:
            raise ValueError('no user videos got for {}'.format(uid))
        return vids['list']['vlist']

    async def get_video_info(self, bvid: str) -> Dict[str, Any]:
        await self.check_frequency()
        v = video.Video(bvid=bvid)
        return await v.get_info()

    async def get_video_tags(self, bvid: str):
        await self.check_frequency()
        v = video.Video(bvid=bvid)
        return await v.get_tags()

    async def get_video_archive_doc(self, bvid: str, save=False):
        vid_all = await self.get_video_info(bvid)
        tags = await self.get_video_tags(bvid)
        tag_names: List[str] = [t['tag_name'] for t in tags]
        fields = VideoArchive._fields.keys()
        vid_doc = VideoArchive(
            **{k: v
               for k, v in vid_all.items() if k in fields})
        vid_doc._raw = vid_all
        vid_doc.publish = datetime.fromtimestamp(vid_all['pubdate'])
        vid_doc.uid = vid_all['owner']['mid']
        vid_doc.tags = tag_names
        vid_doc.author = vid_all['owner']['name']
        if save:
            vid_doc.save()
        return vid_doc

    async def submit_video(self, title: str, characters: List[str], source_url,
                           video_file: str, cover_file: str):
        filename = video.video_upload(video_file, verify=self.verify)
        cover_url = video.video_cover_upload(cover_file, verify=self.verify)
        v = video.VideoUploaderPageObject()
        data = {
            "copyright": 2,  # reprint
            "cover": cover_url,
            "desc": "无端迫害",  # desc for video
            "desc_format_id": 0,
            "dynamic": "",  # dynamic info
            "interactive": 0,
            "no_reprint": 0,
            'source': source_url,  # source url
            "subtitles": {
                "lan": "",
                "open": 0
            },
            "tag": "任天堂明星大乱斗,比赛录像," + ','.join(characters),
            "tid": 17,
            "title": title,
            "videos": [{
                "desc": "",
                "filename": filename,
                "title": "P1"
            }],
            "up_close_danmaku": False,  #"bool, 是否关闭弹幕。",
            "up_close_reply": False,  #"bool, 是否关闭评论。",
        }
        result = video.video_submit(data, verify=self.verify)
        print(result)


# UPLOAD_CONFIG = {
#   "copyright": 1, #"1 自制，2 转载。",
#   "source": "", #"str, 视频来源。投稿类型为转载时注明来源，为原创时为空。",
#   "desc": "", #"str, 视频简介。",
#   "desc_format_id": 0,
#   "dynamic": "", #"str, 动态信息。",
#   "interactive": 0,
#   "open_elec": 0, #"int, 是否展示充电信息。1 为是，0 为否。",
#   "no_reprint": 1, #"int, 显示未经作者授权禁止转载，仅当为原创视频时有效。1 为启用，0 为关闭。",
#   "subtitles": {
#     "lan": "", #"字幕语言，不清楚作用请将该项设置为空",
#     "open": 0
#   },
#   "tag": "学习,测试", #"str, 视频标签。使用英文半角逗号分隔的标签组。示例：标签1,标签2,标签3",
#   "tid": 208, #"int, 分区ID。可以使用 channel 模块进行查询。",
#   #"title": "英语测试第一弹", #"视频标题",
#   "up_close_danmaku": False, #"bool, 是否关闭弹幕。",
#   "up_close_reply": False, #"bool, 是否关闭评论。",
# }