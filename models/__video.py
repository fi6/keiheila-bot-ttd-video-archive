from mongoengine import Document
from mongoengine.fields import IntField, ListField, StringField
from enum import Enum
from datetime import datetime


class VideoTypes(Enum):
    GUIDE = 'GUIDE'


class Video(Document):
    bvid = StringField(required=True)
    aid = IntField()
    title = StringField(required=True)
    typeid = IntField()
    pic = StringField()
    desc = StringField(required=True)
    author = StringField()
    pubdate = IntField()
    ctime = IntField()
    duration = IntField()
    mid = IntField(required=True)
    dynamic = StringField()
    tags = ListField(StringField(), default=[])
    meta = {'collection': 'videos'}

    @property
    def publish_date(self) -> datetime:
        return datetime.fromtimestamp(self.pubdate)