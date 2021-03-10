from datetime import datetime, tzinfo
import pytz

tz_cn = pytz.timezone('Asia/Shanghai')


def get_cn_time():
    """
    return cn time now
    """
    return datetime.now().astimezone(tz_cn)
