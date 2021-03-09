import sys
sys.path.append('.')

from core.__polling import check_video

for video in check_video():
    print(video.to_json())
