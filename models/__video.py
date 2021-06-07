from datetime import datetime
from enum import Enum
from typing import Any, List

from mongoengine import Document
from mongoengine.fields import (DateTimeField, DynamicField, EnumField,
                                IntField, ListField, ReferenceField,
                                StringField)
from utils.date import get_time_str

__code_dict = {
    'GUIDE': '通用攻略',
    'CHARGUIDE': '角色攻略',
    'REPLAY': '比赛录像',
    'COMP': '精彩集锦',
    'FUN': '趣味视频',
    'INTRO': '背景知识'
}


class VideoTypes(Enum):
    GUIDE = 'GUIDE'
    CHAR_GUIDE = 'CHARGUIDE'
    REPLAY = 'REPLAY'
    COMPILATION = 'COMP'
    FUN = 'FUN'
    INTRO = 'INTRO'
    OTEHR = 'OTHER'

    @staticmethod
    def get_str(code) -> str:
        result = __code_dict.get(code)
        return result if result else '其他'

    def get_code(string) -> str:
        for code, cn in __code_dict:
            if string == cn:
                return code
        return 'OTHER'


class _Video(Document):
    # _cls = StringField()
    _raw = DynamicField()
    bvid = StringField(required=True, unique=True)
    title = StringField(required=True)
    pic = StringField()
    desc = StringField(required=True)
    author = StringField()
    publish = DateTimeField()
    duration = IntField()
    uid = IntField(required=True, db_field='uid')
    up_ref = ReferenceField('VerifiedUp', db_field='up')
    dynamic = StringField()
    tags = ListField(StringField(), default=[])
    remark = StringField()
    meta = {'collection': 'videos', 'allow_inheritance': True}

    # meta = {'collection': 'videos'}

    # @property
    # def uid(self) -> int:
    #     return self.mid

    def to_card(self) -> List[Any]:
        raise NotImplementedError()


class VideoUpdate(_Video):
    char = ListField(StringField())
    category = EnumField(VideoTypes)
    msg = StringField()

    def to_card(self) -> List[Any]:
        khl_id = None
        try:
            khl_id = self.up_ref.kid
        except Exception:
            pass
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
                    "content": "视频更新"
                }
            }, {
                "type": "image-group",
                "elements": [{
                    "type": "image",
                    "src": self.pic,
                }]
            }, {
                "type": "section",
                "text": {
                    "type":
                    "kmarkdown",
                    "content":
                    "**[{title}]({url})**\n作者: {author}".format(
                        url=f'https://www.bilibili.com/video/{self.bvid}',
                        title=self.title,
                        author=f'(met){khl_id}(met)'
                        if khl_id else self.author,
                    )
                }
            }, {
                "type": "divider"
            }, {
                "type": "section",
                "text": {
                    "type":
                    "kmarkdown",
                    "content":
                    "{desc}".format(desc=self.desc if len(self.desc) <= 152
                                    else self.desc[:150] + '...', )
                }
            }, {
                "type":
                "context",
                "elements": [{
                    "type":
                    "kmarkdown",
                    "content":
                    "发布于：{pubdate}".format(pubdate=get_time_str(self.publish))
                }]
            }]
        }]


class VideoArchive(_Video):
    category = EnumField(VideoTypes, required=True)
    char = ListField(StringField())
    referrer = StringField()
    msg = StringField()

    def to_card(self) -> List[Any]:
        # if self.up_ref and self.up_ref.kid:
        #     khl_id = self.up_ref.kid
        khl_id = None
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
                    "content": "视频档案库新增"
                }
            }, {
                "type": "image-group",
                "elements": [{
                    "type": "image",
                    "src": self.pic
                }]
            }, {
                "type": "section",
                "text": {
                    "type":
                    "kmarkdown",
                    "content":
                    "**[{title}]({url})**\n作者: {author}".format(
                        url=f'https://www.bilibili.com/video/{self.bvid}',
                        title=self.title,
                        author=f'(met){khl_id}(met)'
                        if khl_id else self.author,
                    )
                }
            }]
        }, {
            "type":
            "card",
            "theme":
            "secondary",
            "size":
            "lg",
            "modules": [{
                "type": "section",
                "text": {
                    "type":
                    "kmarkdown",
                    "content":
                    "{desc}".format(desc=self.desc if len(self.desc) <= 152
                                    else self.desc[:150] + '...', ) +
                    "\n发布于：{pubdate}".format(
                        pubdate=get_time_str(self.publish))
                }
            }, {
                "type": "divider"
            }, {
                "type": "section",
                "text": {
                    "type":
                    "kmarkdown",
                    "content":
                    "由(met){user}(met)推荐".format(user=self.referrer) +
                    '\n推荐语：{remark}'.format(remark=self.remark)
                }
            }]
        }]