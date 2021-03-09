from __future__ import annotations
from typing import Any, Dict, Sequence
from utils import link_parser
from bilibili_api import video


def add_video(char, category, url):
    bvid = link_parser(url)
    video_info: Dict[str, Any] | None = video.get_video_info(bvid=bvid)
    video_tags: Sequence[str] = video.get_tags(bvid=bvid)

    if not video_info:
        raise ValueError
    new_archive = {
        'char': char,
        'category': category,
        'url': url,
        'bvid': video_info['bvid'],
        'owner': video_info['owner']['name'],
        'title': video_info['title'],
        'pubdate': video_info['pubdate']
    }
    archives.find({'bvid': url})
    new_archive_doc = archives.insert_one(new_archive)