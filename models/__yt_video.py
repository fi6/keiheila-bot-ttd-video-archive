from datetime import datetime
from enum import unique
from mongoengine import Document
from mongoengine.fields import DateTimeField, DynamicField, StringField
from pyyoutube.models.video import Video


class YTVideo(Document):
    _raw = DynamicField()
    vid = StringField(required=True, unique=True)
    title = StringField(required=True)
    publish = DateTimeField(required=True)
    desc = StringField()
    channel_id = StringField(db_field='channelId')
    thumbnails: dict = DynamicField()
    channel_title = StringField(db_field='channelTitle')

    @property
    def pic(self) -> str:
        return self.thumbnails['standard']['url']

    @classmethod
    def from_item(cls, item: Video):
        new_doc = cls()
        new_doc._raw = item.to_dict()
        new_doc.vid = item.id
        new_doc.title = item.snippet.title
        new_doc.publish = item.snippet.publishedAt
        new_doc.desc = item.snippet.description
        new_doc.channel_id = item.snippet.channelId
        new_doc.thumbnails = item.snippet.thumbnails.to_dict()
        new_doc.channel_title = item.snippet.channelTitle
        return new_doc

    def update_from_item(self, item: Video):
        self._raw = item.to_dict()
        self.vid = item.id
        self.title = item.snippet.title
        self.publish = item.snippet.publishedAt
        self.desc = item.snippet.description
        self.channel_id = item.snippet.channelId
        self.thumbnails = item.snippet.thumbnails.to_dict()
        self.channel_title = item.snippet.channelTitle
        return self
