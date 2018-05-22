# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
from moviepy.editor import VideoFileClip


class Video():
    def __init__(self, file_path):
        self.file_path = file_path
        video_clip = self._get_video_clip()
        self.video_clip = video_clip
        self.duration = self._get_duration(video_clip)

    def _get_video_clip(self):
        try:
            video_clip = VideoFileClip(self.file_path)
        except OSError as err:
            print("--- Video.get_video_clip", err)
            raise
        else:
            return video_clip

    def _get_duration(self, video_clip):
        duration = video_clip.duration
        return duration
