from typing import List
from models import Group


def get_group_dict():
    groups: List[Group] = Group.objects()
    group_dict = {}
    for group in groups:
        greater_area = group.address._greater_admin_area
        if group_dict.get(greater_area):
            group_dict[greater_area] = [*group_dict[greater_area], group]
        else:
            group_dict[greater_area] = [group]
    return group_dict