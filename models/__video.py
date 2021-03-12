from typing import Any, List
from utils.date import get_time_str
from mongoengine import Document
from mongoengine.fields import DateTimeField, DynamicField, IntField, ListField, ReferenceField, StringField
from enum import Enum
from datetime import datetime


class VideoTypes(Enum):
    GUIDE = 'GUIDE'


class Video(Document):
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
    meta = {'collection': 'videos'}

    # @property
    # def uid(self) -> int:
    #     return self.mid

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
