from typing import Union
from khl.command_preview.app import AppCommand
from khl.command_preview.typings.types import BaseSession
from utils.get_videos import get_videos

ups = [2607110]


async def notification():
    for up in ups:
        await get_videos(uid=up)


class Notification(AppCommand):
    trigger = '通知'

    async def func(
        self, session: BaseSession
    ) -> Union[BaseSession, BaseSession.ResultTypes, None]:
        