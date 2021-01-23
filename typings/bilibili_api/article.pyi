"""
This type stub file was generated by pyright.
"""

from . import utils

r"""
模块： article
功能： 专栏各种信息操作
项目GitHub地址：https://github.com/Passkou/bilibili_api
项目主页：https://passkou.com/bilibili_api
   _____                _____    _____   _  __   ____    _    _
 |  __ \      /\      / ____|  / ____| | |/ /  / __ \  | |  | |
 | |__) |    /  \    | (___   | (___   | ' /  | |  | | | |  | |
 |  ___/    / /\ \    \___ \   \___ \  |  <   | |  | | | |  | |
 | |       / ____ \   ____) |  ____) | | . \  | |__| | | |__| |
 |_|      /_/    \_\ |_____/  |_____/  |_|\_\  \____/   \____/

"""
API = utils.get_api()
def get_comments_g(cv: int, order: str = ..., verify: utils.Verify = ...):
    """
    获取评论
    :param cv: cv号
    :param order:
    :param verify:
    :return:
    """
    ...

def get_sub_comments_g(cv: int, root: int, verify: utils.Verify = ...):
    """
    获取评论下的评论
    :param cv:
    :param root: 根评论ID
    :param verify:
    :return:
    """
    ...

def send_comment(text: str, cv: int, root: int = ..., parent: int = ..., verify: utils.Verify = ...):
    """
    发送评论
    :param cv:
    :param parent: 回复谁的评论的rpid（若不填则对方无法收到回复消息提醒）
    :param root: 根评论rpid，即在哪个评论下面回复
    :param text: 评论内容，为回复评论时不会自动使用`回复 @%用户名%：%回复内容%`这种格式，目前没有发现根据rpid获取评论信息的API
    :param verify:
    :return:
    """
    ...

def set_like_comment(rpid: int, cv: int, status: bool = ..., verify: utils.Verify = ...):
    """
    设置评论点赞状态
    :param cv:
    :param rpid:
    :param status: 状态
    :param verify:
    :return:
    """
    ...

def set_hate_comment(rpid: int, cv: int, status: bool = ..., verify: utils.Verify = ...):
    """
    设置评论点踩状态
    :param cv:
    :param rpid:
    :param status: 状态
    :param verify:
    :return:
    """
    ...

def set_top_comment(rpid: int, cv: int, status: bool = ..., verify: utils.Verify = ...):
    """
    设置评论置顶状态
    :param cv:
    :param rpid:
    :param status: 状态
    :param verify:
    :return:
    """
    ...

def del_comment(rpid: int, cv: int, verify: utils.Verify = ...):
    """
    删除评论
    :param cv:
    :param rpid:
    :param verify:
    :return:
    """
    ...

def get_info(cv: int, verify: utils.Verify = ...):
    """
    获取专栏信息
    :param cv:
    :param verify:
    :return:
    """
    ...

def set_like(cv: int, status: bool = ..., verify: utils.Verify = ...):
    """
    设置专栏点赞状态
    :param cv:
    :param status:
    :param verify:
    :return:
    """
    ...

def set_favorite(cv: int, status: bool = ..., verify: utils.Verify = ...):
    """
    设置专栏收藏状态
    :param cv:
    :param status:
    :param verify:
    :return:
    """
    ...

def add_coins(cv: int, num: int = ..., verify: utils.Verify = ...):
    """
    给专栏投币
    :param cv:
    :param num:
    :param verify:
    :return:
    """
    ...

def share_to_dynamic(cv: int, content: str, verify: utils.Verify = ...):
    """
    专栏转发
    :param cv:
    :param content:
    :param verify:
    :return:
    """
    ...

def get_content(cid: int, preview: bool = ..., verify: utils.Verify = ...):
    """
    获取专栏内容
    :param verify:
    :param preview: 是否为草稿ID，调试用
    :param cid:
    :return:
    """
    ...

class Article(object):
    def __init__(self, meta: dict = ..., paragraphs: list = ...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def save_as_markdown(self, path: str):
        ...
    


class Paragraph(object):
    def __init__(self, align: str = ..., node_list: list = ...) -> None:
        ...
    
    def __len__(self):
        ...
    
    def __str__(self) -> str:
        ...
    


class AbstractNode(object):
    def __init__(self, **kwargs) -> None:
        ...
    


class TextNode(AbstractNode):
    def __init__(self, text: str) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __len__(self):
        ...
    


class AbstractListNode(AbstractNode):
    def __init__(self, node_list: list = ..., **kwargs) -> None:
        ...
    
    def __len__(self):
        ...
    
    def __str__(self) -> str:
        ...
    


class StyleNode(AbstractListNode):
    def __init__(self, style: dict = ..., **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class HeadNode(AbstractListNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class ItalicNode(AbstractListNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class BoldNode(AbstractListNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class DelNode(AbstractListNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class BlockquoteNode(AbstractListNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class UlNode(AbstractListNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class OlNode(AbstractListNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class LiNode(AbstractListNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class ImageNode(AbstractNode):
    def __init__(self, url: str, alt: str, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class AbstractCardNode(AbstractNode):
    def __init__(self, id_: str, **kwargs) -> None:
        ...
    


class VideoCardNode(AbstractCardNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class ArticleCardNode(AbstractCardNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class BangumiCardNode(AbstractCardNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class MusicCardNode(AbstractCardNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class ShopCardNode(AbstractCardNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class ComicCardNode(AbstractCardNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class LiveCardNode(AbstractCardNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class VoteNode(AbstractNode):
    def __init__(self, vote_id: int, info: dict, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class UrlNode(AbstractListNode):
    def __init__(self, url: str, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class SeparatorNode(AbstractNode):
    def __init__(self, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


