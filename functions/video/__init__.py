from __future__ import annotations

from enum import Enum
import logging
from typing import Any, Dict, List, Sequence, Union

from bilibili_api import video
from khl import Msg
from khl.command import Command
from khl.message import TextMsg
from utils.db import archives
from .add import add_video

from .._command import MyCommand


class Category(Enum):
    GUIDE = '攻略',
    COMP = '集锦',
    REPLAY = '录像'
    OTHER = '其他'

    @classmethod
    def get_key(cls, value: str) -> Union[Enum, None]:
        try:
            return cls._value2member_map_[(value, )]
        except Exception as e:
            logging.error(e)
            return None


class VideoEntry(MyCommand):
    trigger = ['视频']

    async def execute(self, msg: Msg, *args: str):
        if not len(args):
            return await self.entry(msg)
        if args[0] in ['add', '添加']:
            return await self.add(msg, list(args[1:]))
        if args[0] == 'create' and len(args) == 1:
            return await self.create(msg)
        if args[0] == 'create' and len(args) == 2:
            return await self.create_from(msg, args[1])

    async def entry(self, msg: Msg):
        pass

    async def add(self, msg: TextMsg, args: List[str]):
        try:
            await add_video(msg, args)
        except ValueError as e:
            await msg.ctx.bot.send(msg.ctx.channel.id,
                                   e.args[0],
                                   temp_target_id=msg.ctx.user.id)
