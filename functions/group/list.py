from models.group import GroupType
from typing import Dict, List, Tuple
from models import Group


def get_group_card():
    (offline_group_dict, char_group_list, general_group_list,
     other_group_list) = get_groups()
    modules = []
    for key, item in offline_group_dict.items():
        modules.append({
            "type": "header",
            "text": {
                "type": "plain-text",
                "content": key
            }
        })
        for group in item:
            modules.append({
                "type": "section",
                "text": {
                    "type": "kmarkdown",
                    "content": '{name}\n'
                }
            })
    return [{
        "type": "card",
        "theme": "secondary",
        "size": "lg",
        "modules": modules
    }]


def get_groups(
) -> Tuple[Dict[str, List[Group]], List[Group], List[Group], List[Group]]:
    groups: List[Group] = Group.objects().order_by('address.code')
    offline_group_dict = {}
    char_group_list = []
    general_group_list = []
    other_group_list = []
    for group in groups:
        if group.type == GroupType.OFFLINE:
            greater_area = group.address._greater_admin_area
            if offline_group_dict.get(greater_area):
                offline_group_dict[greater_area] = [
                    *offline_group_dict[greater_area], group
                ]
            else:
                offline_group_dict[greater_area] = [group]
        elif group.type == GroupType.CHARACTER:
            char_group_list.append(group)
        elif group.type == GroupType.GENERAL:
            general_group_list.append(group)
        elif group.type == GroupType.OTHER:
            other_group_list.append(group)
    return (offline_group_dict, char_group_list, general_group_list,
            other_group_list)
