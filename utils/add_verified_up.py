from bilibili_api import user
import sys
sys.path.append('.')

from models import VerifiedUp

# ups = VerifiedUp.objects(tag='video', priority=1)
# print(ups)

bilibili_id = 67674065
kaiheila_id = 2771269656
live = False
priority = -1  # -1, 0, 1 low->high

u = user.get_user_info(int(bilibili_id))
up = VerifiedUp(uid=u['mid'],
                roomid=u['live_room']['roomid'],
                avatar=u['face'],
                nickname=u['name'],
                sign=u['sign'],
                priority=priority,
                tag=['video'] if not live else ['video', 'live'])
up.kid = str(kaiheila_id)
up.save()
print(up.to_mongo())
