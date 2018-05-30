# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180521
'''
import os
from src.media_file import MediaFile


class Audio(MediaFile):
    def __init__(self, file_path):
        MediaFile.__init__(self, file_path)
