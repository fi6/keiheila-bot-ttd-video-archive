from mongoengine import Document
from mongoengine.fields import IntField, ListField, StringField


class Up(Document):
    uid = IntField(required=True, unique=True)
    roomid = IntField(db_field='room')
    avatar = StringField()
    nickname = StringField()
    sign = StringField()
    meta = {'allow_inheritance': True, 'collection': 'ups'}


class VerifiedUp(Up):
    follower_role = IntField(db_field='follower')
    kid = StringField()
    # 0: normal, -1: below, 1: high
    priority = IntField()
    tag = ListField(StringField())
