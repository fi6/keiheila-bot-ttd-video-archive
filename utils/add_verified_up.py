from bilibili_api import user, live
import sys
sys.path.append('.')

from models import VerifiedUp

# ups = VerifiedUp.objects(tag='video', priority=1)
# print(ups)

bilibili_id = 307889
kaiheila_id = 1409695807

u = user.get_user_info(int(bilibili_id))
up = VerifiedUp(
    uid=u['mid'],
    roomid=u['live_room']['roomid'],
    avatar=u['face'],
    nickname=u['name'],
    sign=u['sign'],
    priority=-1,  # -1, 0, 1 low->high
    tag=['video'])
up.kid = str(kaiheila_id)
up.save()
print(up.to_mongo())
