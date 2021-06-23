from typing import List
from mongoengine import Document
from mongoengine.fields import IntField, ListField, StringField


class Up(Document):
    uid: int = IntField(required=True, unique=True)
    roomid: int = IntField(db_field='room')
    avatar: str = StringField()
    nickname: str = StringField()
    sign: str = StringField()
    meta = {'allow_inheritance': True, 'collection': 'ups'}


class VerifiedUp(Up):
    follower_role: str = IntField(db_field='follower')
    kid: str = StringField()
    # 0: normal, -1: below, 1: high
    priority: int = IntField()
    tag: List[str] = ListField(StringField())
