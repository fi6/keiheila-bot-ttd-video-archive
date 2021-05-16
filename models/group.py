from enum import Enum
from mongoengine import Document
from mongoengine.fields import BooleanField, EnumField, StringField
from .__event import _Address


class GroupType(Enum):
    WECHAT = 1
    QQ = 2
    KHL = 3
    OTHER = 4


class Group(Document):
    name = StringField(required=True)
    offline = BooleanField(required=True)
    type = EnumField(GroupType, required=True)
    contact = StringField(required=True)
    remark = StringField()
    address = _Address()

    def to_card(self):
        return [{}]