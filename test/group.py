import sys
sys.path.append('.')

from models.group import Group, GroupType, JoinType
from functions.event.parser import get_address
from functions.group.list import get_group_dict

# group = Group()
# group.name = '北京 BeijingSmash'
# group.type = GroupType.OFFLINE
# group.join = JoinType.WECHAT
# group.contact = '微信vanbuskirkcj'
# group.address = get_address('北京市东城区方家胡同12号野友趣2层')
# group.save()

# print(Group.objects().order_by('address.code'))
# print(get_address('上海'))
print(get_group_dict())