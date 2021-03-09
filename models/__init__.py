import mongoengine as __mongo
from configs import auth

from .__video import Video  # noqa
from .__up import Up, VerifiedUp  # noqa

__mongo.connect(db='ttd', authentication_source='admin', host=auth.mongo_url)
