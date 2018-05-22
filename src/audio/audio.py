# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180521
'''
from moviepy.editor import AudioFileClip


class Audio():
    def __init__(self, file_path):
        self.file_path = file_path
        audio_clip = self._get_audio_clip()
        self.audio_clip = audio_clip
        self.duration = self._get_duration(audio_clip)

    def _get_audio_clip(self):
        try:
            audio_clip = AudioFileClip(self.file_path)
        except OSError as err:
            raise
        else:
            return audio_clip

    def _get_duration(self, audio_clip):
        duration = audio_clip.duration
        return duration
