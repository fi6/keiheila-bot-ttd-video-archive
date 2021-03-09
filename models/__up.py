from mongoengine import Document
from mongoengine.fields import IntField


class Up(Document):
    meta = {'allow_inheritance': True, 'collection': 'ups'}


class VerifiedUp(Up):
    role = IntField()
    mid = IntField()
    