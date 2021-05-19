from __future__ import annotations

from enum import Enum
import logging
from typing import Any, Dict, List, Sequence, Union

from khl import Msg
from .add import add_video

from .._command import MyCommand


# class Category(Enum):
#     GUIDE = '攻略',
#     COMP = '集锦',
#     REPLAY = '录像'
#     OTHER = '其他'

#     @classmethod
#     def get_key(cls, value: str) -> Union[Enum, None]:
#         try:
#             return cls._value2member_map_[(value, )]
#         except Exception as e:
#             logging.error(e)
#             return None


class VideoEntry(MyCommand):
    trigger = ['视频']

    async def execute(self, msg: Msg, *args: str):
        if not len(args):
            return await self.entry(msg)
        if args[0] in ['add', '添加']:
            return await self.add(msg, list(args[1:]))
        if args[0] == 'search':
            return await self.search(msg, list(args[1:]))

    async def entry(self, msg: Msg):
        pass

    async def add(self, msg: Msg, args: List[str]):
        try:
            await add_video(msg, args)
        except ValueError as e:
            await msg.ctx.bot.send(msg.ctx.channel.id,
                                   e.args[0],
                                   temp_target_id=msg.ctx.user.id)

    async def search(self, msg: Msg, args: List[str]):
        try:
            pass
        except Exception as e:
            await msg.ctx.bot.send(msg.ctx.channel.id,
                                   e.args[0],
                                   temp_target_id=msg.ctx.user.id)