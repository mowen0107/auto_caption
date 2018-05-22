# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180521
'''
import os
from moviepy.editor import AudioFileClip


class Audio():
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_dir = self.get_file_dir()
        audio_clip = self.get_audio_clip()
        self.audio_clip = audio_clip
        self.duration = self.get_duration(audio_clip)

    def get_file_dir(self):
        file_dir = os.path.split(self.file_path)[0]
        return file_dir

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
