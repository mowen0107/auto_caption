# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
import moviepy
from src.audio.audio import Audio


class OriginAudio(Audio):
    def __init__(self, file_path):
        Audio.__init__(self, file_path)
        self.order = 0

    def subclip(self, start_second, end_second):
        subclip = self.audio_clip.subclip(start_second, end_second)
        return subclip

    def save_clip(self, subclip):
        fragment_path = self.file_dir + '/fragment_{}.aac'.format(self.order)
        try:
            subclip.write_audiofile(fragment_path, codec='aac')
        except Exception as err:
            raise
        else:
            return True
