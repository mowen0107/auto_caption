# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
from src.audio.audio import Audio


class FragmentAudio(Audio):
    def __init__(self, file_path):
        Audio.__init__(self, file_path)

    def set_order(self, order):
        ''' order代表了这个fragment的序号，从0开始
        '''
        self.order = order

    def set_begin_end_time(self, begin_end_time):
        pass

    def get_recognition_result(self):
        ''' 由百度api获得语音识别的结果
        '''
        pass
