# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
import pytest
from moviepy.video.VideoClip import VideoClip
from src.video.video import Video


class TestVideo():
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        self.video = Video("./resource/video/test_video.flv")

    def teardown_method(self, method):
        pass

    def test_get_right_videoclip(self):
        video_clip = self.video._get_video_clip()
        assert isinstance(video_clip, VideoClip)

    def test_get_wrong_videoclip(self):
        self.video.file_path = "wrong_file_path.flv"
        with pytest.raises(OSError):
            video_clip = self.video._get_video_clip()

    def test_get_duration(self):
        video_clip = self.video.video_clip
        duration = self.video._get_duration(video_clip)
        print("--- TestVideo.test_get_duration, duration:{}".format(duration))
        assert duration > 0
