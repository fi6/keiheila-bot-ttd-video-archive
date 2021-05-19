from enum import Enum
from mongoengine import Document
from mongoengine.fields import BooleanField, EmbeddedDocumentField, EnumField, StringField
from .__event import _Address


class GroupType(Enum):
    OFFLINE = 1
    CHARACTER = 2
    GENERAL = 3
    OTHER = 4


class JoinType(Enum):
    WECHAT = 1
    QQ = 2
    KHL = 3
    OTHER = 4


class Group(Document):
    name = StringField(required=True)
    type = EnumField(GroupType, required=True)
    join = EnumField(JoinType, required=True)
    contact = StringField(required=True)
    remark = StringField()
    address = EmbeddedDocumentField(_Address)
    char = StringField()

    def to_card(self):
        return [{}]