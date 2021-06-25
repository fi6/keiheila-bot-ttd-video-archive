import sys
sys.path.append('.')
import re
from typing import List
from urllib.parse import parse_qs, urlparse

from models import VerifiedUp, _Video

ups: List[VerifiedUp] = VerifiedUp.objects()
for up in ups:
    if 'live' in up.tag:
        print(up.nickname, up.tag)

for video in _Video.objects():
    if not video.original:
        result = urlparse(video.source)
        print(video.source)
        if result:
            id = re.match(
                r'.*(?:youtu.be\/|v\/|u\/\w\/|embed\/|watch\?(?:.*)v=)([^#\&\?]*).*',
                video.source)
            print(id.group(1) if id and r'/' not in id.group(1) else None)
    # if video._raw['copyright'] == 1:
    #     video.original = True
    # else:
    #     video.original = False
    #     source = re.search(r'^http.+?(?:$|\n)', video.desc)
    #     if not source:
    #         source = re.search(r'^.+?(?:$|\n)', video.desc)
    #     video.source = source.group(0).strip() if source else ''
    # if not video.original:
    #     print(video._raw)
    #     print(video.source)
    #     print(video.original)
    # video.save()
