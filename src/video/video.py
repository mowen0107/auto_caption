# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
import os
from moviepy.editor import VideoFileClip


class Video():
    def __init__(self, file_path):
        self.file_path = file_path
        fullname = self.get_fullname()
        self.fullname = fullname
        self.shortname = self.get_shortname(fullname)
        self.filetype = self.get_extension(fullname)
        video_clip = self.get_video_clip()
        self.video_clip = video_clip
        self.duration = self.get_duration(video_clip)

    def get_fullname(self):
        ''' 获取带后缀的文件名
        '''
        (file_dir, fullname) = os.path.split(self.file_path)
        print("--- Video.get_file_name, file_dir:{}, fullname:{}".format(
            file_dir, fullname))
        return fullname

    def get_shortname(self, fullname):
        ''' 由带后缀的文件名获取不带后缀的文件名
        '''
        last_do_index = fullname.rindex(".")
        file_shortname = fullname[:last_do_index]
        return file_shortname

    def get_extension(self, fullname):
        ''' 获取文件后缀
        '''
        last_do_index = fullname.rindex(".")
        extension = fullname[last_do_index + 1:]
        return extension

    def get_video_clip(self):
        try:
            video_clip = VideoFileClip(self.file_path)
        except OSError as err:
            print("--- Video.get_video_clip", err)
            raise
        else:
            return video_clip

    def get_duration(self, video_clip):
        duration = video_clip.duration
        return duration
