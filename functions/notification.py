from __future__ import annotations
import logging
import configs
from typing import TYPE_CHECKING
from core import polling
from ._instance import bot
import json
from models import Video

if TYPE_CHECKING:
    from core.types import LiveInfo


async def live_notif(living: LiveInfo):
    logging.info('received live start event')
    card = living.to_card()
    logging.info(await bot.send(configs.channel.notif,
                                json.dumps(card),
                                type=10))


async def video_notif(video: Video):
    card = video.to_card()
    await bot.send(configs.channel.notif, json.dumps(card), type=10)


polling.on('live_start', live_notif)
polling.on('video_update', video_notif)

if len(polling.listeners('live_start')):
    logging.info('[init success] live start sender')
else:
    logging.exception('[init failed] live start sender')