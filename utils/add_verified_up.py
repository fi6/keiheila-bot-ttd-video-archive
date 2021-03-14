from bilibili_api import user, live
import sys
sys.path.append('.')

from models import VerifiedUp

# ups = VerifiedUp.objects(tag='video', priority=1)
# print(ups)

u = user.get_user_info(330364988)
up = VerifiedUp(uid=u['mid'],
                roomid=u['live_room']['roomid'],
                avatar=u['face'],
                nickname=u['name'],
                sign=u['sign'],
                priority=-1,
                tag=['video'])
up.kid = '3961957847'
up.save()
print(up.to_json())
