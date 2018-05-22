# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
from src.video.source_video import SourceVideo
from src.video_to_audio import VideoToAudio


class TestVideoToAudio():
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        video_clip = SourceVideo("./resource/video/test_video.flv")
        self.video_to_audio = VideoToAudio(video_clip)

    def teardown_method(self, method):
        pass

    # def test_is_dir_exist(self):
    #     is_exist = self.video_to_audio.is_dir_exist()
    #     assert is_exist is True
