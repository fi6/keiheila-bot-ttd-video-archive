from mongoengine import Document
from mongoengine.fields import IntField, StringField


class Up(Document):
    uid = IntField(required=True)
    roomid = IntField(db_field='room')
    meta = {'allow_inheritance': True, 'collection': 'ups'}


class VerifiedUp(Up):
    follower_role = IntField(db_field='follower')

    # 0: normal, -1: below, 1: high
    priority = IntField()
    tag = StringField()
