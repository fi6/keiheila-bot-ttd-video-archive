from mongoengine import Document
from mongoengine.fields import IntField


class Up(Document):
    meta = {'allow_inheritance': True, 'collection': 'ups'}


class VerifiedUp(Up):
    follower_role = IntField(db_field='role')
    mid = IntField()
