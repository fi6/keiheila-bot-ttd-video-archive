"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod
from enum import Enum
from khl.Bot import Bot
from khl.Message import Msg
from typing import Any, Optional, Sequence

class CommandType(Enum):
    MENU = ...
    APP = ...


class BaseSession(ABC):
    class ResultTypes(Enum):
        SUCCESS = ...
        FAIL = ...
        ERROR = ...
        HELP = ...
    
    
    command: Any
    command_str: str
    args: Sequence[str]
    msg: Msg
    bot: Bot
    result_type: ResultTypes
    detail: Any
    @abstractmethod
    def __init__(self, command: Any, command_str: str, args: Sequence[str], msg: Msg, bot: Optional[Bot] = ...) -> None:
        ...
    
    @abstractmethod
    async def reply(self, content: str, message_type: Msg.Types = ..., result_type: ResultTypes = ...):
        ...
    
    @abstractmethod
    async def reply_only(self, content: str, message_type: Msg.Types = ..., result_type: ResultTypes = ...):
        ...
    
    @abstractmethod
    async def mention(self, content: str, message_type: Msg.Types = ..., result_type: ResultTypes = ...):
        ...
    
    @abstractmethod
    async def send(self, content: str, message_type: Msg.Types = ..., result_type: ResultTypes = ..., mention: bool = ..., reply: bool = ...):
        ...
    


