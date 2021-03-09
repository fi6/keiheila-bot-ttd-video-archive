import mongoengine as __mongo
from configs import auth
import logging

from .__video import Video  # noqa
from .__up import Up, VerifiedUp  # noqa

__mongo.connect(db='ttd', authentication_source='admin', host=auth.mongo_url)
logging.info('db connected, models init success')