# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180521
'''
from .video import Video


class SourceVideo(Video):
    def __init__(self, video_name):
        Video.__init__(video_name)
