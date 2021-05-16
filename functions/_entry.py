from typing import Set
from ._command import MyCommand
from khl.message import Msg


class BotEntry(MyCommand):
    trigger = ['菜单']
    name = 'entry'
    _sub_commands: Set[MyCommand] = set()

    def __init__(self, *sub_commands: MyCommand):
        for command in sub_commands:
            self.add_subcommand(command)

    async def execute(self, msg: Msg, *args: str):
        if not len(args):
            return await self.menu(msg)

        for app in self._sub_commands:
            if args[0] in app.trigger:
                args = args[1:]
                await app.execute(msg, *args)

    def add_subcommand(self, cmd: MyCommand):
        self._sub_commands.add(cmd)

    async def menu(self, msg: Msg):
        await msg.ctx.send_temp('添加视频\n---\n添加活动')
