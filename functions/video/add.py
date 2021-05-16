from typing import Any, Dict, List
from utils import link_parser
from khl.message import Msg
from core.__video import add_video_archive
import json
from models import VideoTypes


async def add(msg: Msg, args: List[str]):
    # args: ['GUIDE']
    if not len(args):
        await msg.ctx.send_card_temp(json.dumps(add_start_card()))

    category = args[0]

    await msg.ctx.send_temp(
        '你即将添加`{category}`分类的视频。\n请在30秒内输入视频链接，目前仅支持b站视频'.format(
            category=VideoTypes.get_str(category)))
    input = await msg.ctx.wait_user(msg.ctx.user_id)
    if not input.content:
        raise ValueError('没有收到输入。如需添加视频，请重新开始。')

    bvid = link_parser(input.content)

    if not bvid:
        await msg.reply_temp('不是有效的b站链接，请检查。如果这是一个误报，请在反馈频道描述问题。')
        return

    vid_doc = add_video_archive(bvid)
    await msg.reply('档案已添加')


def add_start_card():
    return [{
        "type":
        "card",
        "theme":
        "secondary",
        "size":
        "lg",
        "modules": [{
            "type": "header",
            "text": {
                "type": "plain-text",
                "content": "添加视频到档案库"
            }
        }, {
            "type": "section",
            "text": {
                "type": "kmarkdown",
                "content": "请复制视频链接，并点击视频分类以开始添加"
            }
        }, {
            "type":
            "action-group",
            "elements": [{
                "type": "button",
                "click": "return-val",
                "theme": "primary",
                "value": ".视频 添加 GUIDE",
                "text": {
                    "type": "plain-text",
                    "content": "通用攻略"
                }
            }, {
                "type": "button",
                "click": "return-val",
                "theme": "primary",
                "value": ".视频 添加 CHARGUIDE",
                "text": {
                    "type": "plain-text",
                    "content": "角色攻略"
                }
            }, {
                "type": "button",
                "click": "return-val",
                "theme": "primary",
                "value": ".视频 添加 REPLAY",
                "text": {
                    "type": "plain-text",
                    "content": "比赛录像"
                }
            }, {
                "type": "button",
                "click": "return-val",
                "theme": "primary",
                "value": ".视频 添加 COMP",
                "text": {
                    "type": "plain-text",
                    "content": "精彩集锦"
                }
            }]
        }, {
            "type":
            "action-group",
            "elements": [{
                "type": "button",
                "click": "return-val",
                "theme": "primary",
                "value": ".视频 添加 FUN",
                "text": {
                    "type": "plain-text",
                    "content": "趣味视频"
                }
            }, {
                "type": "button",
                "click": "return-val",
                "theme": "primary",
                "value": ".视频 添加 INTRO",
                "text": {
                    "type": "plain-text",
                    "content": "背景知识"
                }
            }, {
                "type": "button",
                "click": "return-val",
                "theme": "primary",
                "value": ".视频 添加 OTHER",
                "text": {
                    "type": "plain-text",
                    "content": "其他"
                }
            }]
        }]
    }]
