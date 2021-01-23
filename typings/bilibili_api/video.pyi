"""
This type stub file was generated by pyright.
"""

import datetime
from . import utils

r"""
模块：video
功能：获取视频各种信息以及操作视频
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
def get_video_info(bvid: str = ..., aid: int = ..., is_simple: bool = ..., verify: utils.Verify = ...):
    """
    获取视频信息
    :param aid:
    :param bvid:
    :param is_simple: 简易信息（另一个API）
    :param verify:
    :return:
    """
    ...

def get_tags(bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    获取视频标签
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def get_chargers(bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    获取视频充电用户
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def get_pages(bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    获取视频分P情况
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def get_download_url(bvid: str = ..., aid: int = ..., page: int = ..., verify: utils.Verify = ...):
    """
    获取视频下载链接
    :param aid:
    :param bvid:
    :param page:
    :param verify:
    :return:
    """
    ...

def get_related(bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    获取该视频相关推荐
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def get_added_coins(bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    投币数量
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def get_favorite_list(bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    获取收藏夹列表供收藏操作用
    :param bvid: 
    :param aid: 
    :param verify: 
    :return: 
    """
    ...

def is_liked(bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    是否点赞视频
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def is_favoured(bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    是否收藏过
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def set_like(status: bool = ..., bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    点赞
    :param status: True点赞False取消点赞
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def add_coins(num: int = ..., like: bool = ..., bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    投币
    :param num: 1或2个
    :param like: 是否同时点赞
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def operate_favorite(bvid: str = ..., aid: int = ..., add_media_ids: list = ..., del_media_ids: list = ..., verify: utils.Verify = ...):
    """
    操作音频收藏夹
    :param aid:
    :param bvid:
    :param add_media_ids:
    :param del_media_ids:
    :param verify:
    :return:
    """
    ...

def get_danmaku(bvid: str = ..., aid: int = ..., page: int = ..., verify: utils.Verify = ..., date: datetime.date = ...):
    """
    获取弹幕
    :param aid:
    :param bvid:
    :param page: 分p数
    :param verify: date不为None时需要SESSDATA验证
    :param date: 为None时获取最新弹幕，为datetime.date时获取历史弹幕
    """
    ...

def get_history_danmaku_index(bvid: str = ..., aid: int = ..., page: int = ..., date: datetime.date = ..., verify: utils.Verify = ...):
    """
    获取历史弹幕索引
    :param aid:
    :param bvid:
    :param page:
    :param date: 默认为这个月
    :param verify:
    :return:
    """
    ...

def like_danmaku(dmid: int, oid: int, is_like: bool = ..., verify: utils.Verify = ...):
    """
    点赞弹幕
    :param dmid: 弹幕ID
    :param oid: 分P id，又称cid
    :param is_like: 点赞/取消点赞
    :param verify:
    :return:
    """
    ...

def has_liked_danmaku(dmid, oid: int, verify: utils.Verify = ...):
    """
    是否已点赞弹幕
    :param dmid: 弹幕id，为list时同时查询多个弹幕，为int时只查询一条弹幕
    :param oid: 分P id，又称cid
    :param verify:
    :return:
    """
    ...

def send_danmaku(danmaku: utils.Danmaku, page: int = ..., bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    发送弹幕
    :param danmaku: Danmaku类
    :param page: 分p号
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def get_comments_g(bvid: str = ..., aid: int = ..., order: str = ..., verify: utils.Verify = ...):
    """
    获取评论
    :param order:
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def get_sub_comments_g(root: int, bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    获取评论下的评论
    :param root: 根评论ID
    :param bvid:
    :param aid:
    :param verify:
    :return:
    """
    ...

def send_comment(text: str, root: int = ..., parent: int = ..., bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    发送评论
    :param parent: 回复谁的评论的rpid（若不填则对方无法收到回复消息提醒）
    :param root: 根评论rpid，即在哪个评论下面回复
    :param text: 评论内容，为回复评论时不会自动使用`回复 @%用户名%：%回复内容%`这种格式，目前没有发现根据rpid获取评论信息的API
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def set_like_comment(rpid: int, status: bool = ..., bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    设置评论点赞状态
    :param rpid:
    :param status: 状态
    :param bvid:
    :param aid:
    :param verify:
    :return:
    """
    ...

def set_hate_comment(rpid: int, status: bool = ..., bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    设置评论点踩状态
    :param rpid:
    :param status: 状态
    :param bvid:
    :param aid:
    :param verify:
    :return:
    """
    ...

def set_top_comment(rpid: int, status: bool = ..., bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    设置评论置顶状态
    :param rpid:
    :param status: 状态
    :param bvid:
    :param aid:
    :param verify:
    :return:
    """
    ...

def del_comment(rpid: int, bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    删除评论
    :param rpid:
    :param bvid:
    :param aid:
    :param verify:
    :return:
    """
    ...

def add_tag(tag_name: str, bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    添加标签
    :param tag_name: 标签名
    :param aid:
    :param bvid:
    :param verify:
    :return:
    """
    ...

def del_tag(tag_id: int, bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    ...

def share_to_dynamic(content: str, bvid: str = ..., aid: int = ..., verify: utils.Verify = ...):
    """
    视频分享到动态
    :param aid:
    :param bvid:
    :param content:
    :param verify:
    :return:
    """
    ...

def video_upload(path: str, verify: utils.Verify, on_progress=...):
    """
    上传视频
    :param on_progress: 进度回调，数据格式：{"event": "事件名", "ok": "是否成功", "data": "附加数据"}
                        事件名：PRE_UPLOAD，GET_UPLOAD_ID，UPLOAD_CHUNK，VERIFY
    :param path: 视频路径
    :param verify:
    :return: 该视频的filename，用于后续提交投稿用
    """
    ...

def video_cover_upload(path, verify: utils.Verify):
    """
    封面上传
    :param path:
    :param verify:
    :return: 封面URL，用于提交投稿信息用
    """
    ...

def video_submit(data: dict, verify: utils.Verify):
    """
    提交投稿信息
    :param data: 投稿信息
    {
        "copyright": 1自制2转载,
        "source": "类型为转载时注明来源",
        "cover": "封面URL",
        "desc": "简介",
        "desc_format_id": 0,
        "dynamic": "动态信息",
        "interactive": 0,
        "no_reprint": 1为显示禁止转载,
        "subtitles": {
            // 字幕格式，请自行研究
            "lan": "语言",
            "open": 0
        },
        "tag": "标签1,标签2,标签3（英文半角逗号分隔）",
        "tid": 分区ID,
        "title": "标题",
        "videos": [
            {
                "desc": "描述",
                "filename": "video_upload(返回值)",
                "title": "分P标题"
            }
        ]
    }
    :param verify:
    :return:
    """
    ...

def connect_all_VideoOnlineMonitor(*args):
    ...

class VideoOnlineMonitor:
    DATAPACK_CLIENT_VERIFY = ...
    DATAPACK_SERVER_VERIFY = ...
    DATAPACK_CLIENT_HEARTBEAT = ...
    DATAPACK_SERVER_HEARTBEAT = ...
    DATAPACK_DANMAKU = ...
    def __init__(self, bvid: str = ..., aid: int = ..., page: int = ..., event_handler=..., debug: bool = ..., should_reconnect: bool = ...) -> None:
        ...
    
    def connect(self, return_coroutine: bool = ...):
        ...
    
    def disconnect(self):
        ...
    
    def get_connect_status(self):
        ...
    


