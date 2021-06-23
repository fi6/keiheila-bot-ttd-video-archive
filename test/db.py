import sys
from typing import List
sys.path.append('.')

from models import VerifiedUp

ups: List[VerifiedUp] = VerifiedUp.objects()
for up in ups:
    if 'live' in up.tag:
        print(up.nickname, up.tag)
