# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180521
'''
import os
from src.media_file import MediaFile
from moviepy.editor import AudioFileClip


class Audio(MediaFile):
    def __init__(self, file_path):
        MediaFile.__init__(self, file_path)
        audio_clip = self.get_audio_clip()
        self.audio_clip = audio_clip
        self.duration = self.get_duration(audio_clip)

    def get_audio_clip(self):
        try:
            audio_clip = AudioFileClip(self.file_path)
        except OSError as err:
            raise
        else:
            return audio_clip

    def get_duration(self, audio_clip):
        duration = audio_clip.duration
        return duration
