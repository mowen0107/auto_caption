# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
from src.audio.audio import Audio


class FragmentAudio(Audio):
    def __init__(self, order, file_path, start_second, end_second):
        Audio.__init__(self, file_path)
        self.order = order
        self.start_second = start_second
        self.end_second = end_second
        self.audio_content = self.get_audio_content()

    def get_audio_content(self):
        with open(self.file_path, 'rb') as fp:
            audio_content = fp.read()
            return audio_content
