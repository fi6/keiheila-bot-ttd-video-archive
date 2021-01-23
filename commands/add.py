from os import name
from typing import Dict, Union
from utils.link_parser import link_parser
from khl.command_preview import AppCommand
from khl.command_preview.typings import BaseSession
from enum import Enum
from utils.db import archives
from bilibili_api import video
from __future__ import annotations


class Category(Enum):
    GUIDE = '攻略',
    COMP = '集锦',
    REPLAY = '录像'
    OTHER = '其他'

    @classmethod
    def get_key(cls, value: str) -> Union[Enum, None]:
        try:
            return cls._value2member_map_[(value, )]
        except:
            return None


class AddVideo(AppCommand):
    trigger = '添加'
    help = ('发送`。添加视频 角色 分类 链接`即可。如果视频与角色无关，请写"通用"。\n'
            '角色请尽量以官方译名为准，系统会尝试自动解析。\n'
            '分类只包括攻略，集锦，其他三类。')

    async def func(
        self, session: BaseSession
    ) -> Union[BaseSession, BaseSession.ResultTypes, None]:
        char = session.args[0:-2]
        category = session.args[-2]
        link = session.args[-1]

        bvid = await link_parser(link)

        if not bvid:
            return await session.reply('不是有效的b站链接，请检查。如果这是一个误报，请@冰飞。')

        video_info: Dict[str, str | int] | None = video.get_video_info(
            bvid=bvid)
        video_tags = video.get_tags(bvid=bvid)

        if not video_info:
            return await session.reply('无法从b站爬取~')

        new_archive = {
            'char': char,
            'category': category,
            'link': link,
            'bvid': video_info['bvid'],
            'owner': video_info['owner']['name'],
            'title': video_info['title'],
            'pubdate': video_info['pubdate']
        }
        archives.find({'bvid': link})
        new_archive_doc = archives.insert_one(new_archive)
        await session.reply('档案已添加')