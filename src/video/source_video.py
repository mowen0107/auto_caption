# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180521
'''
from src.video.video import Video


class SourceVideo(Video):
    def __init__(self, file_path):
        Video.__init__(self, file_path)
