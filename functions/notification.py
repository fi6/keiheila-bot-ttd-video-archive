from __future__ import annotations
import configs
from typing import TYPE_CHECKING
from core import polling
from ._instance import bot
import json

if TYPE_CHECKING:
    from core.types import LiveInfo


@polling.on('live_start')
async def live_notif(living: LiveInfo):
    card = living.to_card()
    await bot.send(configs.channel.notif, json.dumps(card))
