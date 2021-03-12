from __future__ import annotations
import logging
import configs
from typing import TYPE_CHECKING
from core import polling
from ._instance import bot
import json

if TYPE_CHECKING:
    from core.types import LiveInfo


async def live_notif(living: LiveInfo):
    logging.info('received live start event')
    card = living.to_card()
    await bot.send(configs.channel.notif, json.dumps(card))


polling.on('live_start', live_notif)

if len(polling.listeners('live_start')):
    logging.info('[init success] live start sender')
else:
    logging.exception('[init failed] live start sender')