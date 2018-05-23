# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
import os
import ffmpy3
from src.audio.audio import Audio


class VideoToAudio():
    def __init__(self, video):
        self.video = video
        self.audio_output_dir = "./resource/audio/" + video.shortname + '/'
        if not self.is_dir_exist():
            self.create_dir()

    def gen_audio(self):
        ''' 使用ffmpeg提取视频文件的音频
        '''
        input_path = self.video.file_path
        output_path = self.audio_output_dir + self.video.shortname + '.wav'
        ffmpeg_command = ffmpy3.FFmpeg(
            inputs={input_path: None},
            outputs={
                output_path: '-vn -y -acodec pcm_s16le'
            })
        ffmpeg_command.run()
        return Audio(output_path).audio_clip

    def is_dir_exist(self):
        is_exist = os.path.exists(self.audio_output_dir)
        return is_exist

    def create_dir(self):
        try:
            os.makedirs(self.audio_output_dir)
        except FileExistsError:
            return
