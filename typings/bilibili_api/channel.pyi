"""
This type stub file was generated by pyright.
"""

from . import utils

r"""
模块：channel
功能：频道相关
项目GitHub地址：https://github.com/Passkou/bilibili_api
项目主页：https://passkou.com/bilibili_api
   _____                _____    _____   _  __   ____    _    _
 |  __ \      /\      / ____|  / ____| | |/ /  / __ \  | |  | |
 | |__) |    /  \    | (___   | (___   | ' /  | |  | | | |  | |
 |  ___/    / /\ \    \___ \   \___ \  |  <   | |  | | | |  | |
 | |       / ____ \   ____) |  ____) | | . \  | |__| | | |__| |
 |_|      /_/    \_\ |_____/  |_____/  |_|\_\  \____/   \____/4
"""
API = utils.get_api()
def get_channel_info_by_tid(tid: int):
    """
    根据tid获取频道信息
    :param tid:
    :return: 第一个是主分区，第二个是子分区，没有时返回None
    """
    ...

def get_channel_info_by_name(name: str):
    """
    根据名字获取频道信息
    :param name:
    :return: 第一个是主分区，第二个是子分区，没有时返回None
    """
    ...

def get_top10(tid: int, day: int = ..., verify: utils.Verify = ...):
    """
    获取分区前十排行榜
    :param tid: 0为主页
    :param day:
    :param verify:
    :return:
    """
    ...

