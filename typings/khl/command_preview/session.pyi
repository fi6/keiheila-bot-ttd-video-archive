"""
This type stub file was generated by pyright.
"""

from typing import Optional, Sequence
from khl.Bot import Bot
from khl.Message import Msg
from .typings import BaseSession
from .typings.base_command import BaseCommand

class Session(BaseSession):
    command: BaseCommand
    command_str: str
    args: Sequence[str]
    msg: Msg
    bot: Bot
    def __init__(self, command: BaseCommand, command_str: str, args: Sequence[str], msg: Msg, bot: Optional[Bot] = ...) -> None:
        ...
    
    async def reply(self, content: str, message_type: Msg.Types = ..., result_type: BaseSession.ResultTypes = ...):
        ...
    
    async def reply_only(self, content: str, message_type: Msg.Types = ..., result_type: BaseSession.ResultTypes = ...):
        ...
    
    async def mention(self, content: str, message_type: Msg.Types = ..., result_type: BaseSession.ResultTypes = ...):
        ...
    
    async def send(self, content: str, message_type: Msg.Types = ..., result_type: BaseSession.ResultTypes = ..., mention: bool = ..., reply: bool = ...):
        ...
    


