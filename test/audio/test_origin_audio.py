# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
from moviepy.audio.AudioClip import AudioClip
from src.audio.audio import Audio
from src.audio.origin_audio import OriginAudio


class TestOriginAudio():
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        self.origin_audio = OriginAudio(
            "./resource/audio/test_video/test_video.wav")

    def teardown_method(self, method):
        pass

    def test_subclip(self):
        subclip = self.origin_audio.subclip(0, 20)
        assert isinstance(subclip, AudioClip)
        assert subclip.duration > 0
        print("--- TestOriginAudio.test_subclip, duration:{}".format(
            subclip.duration))

    def test_save_clip(self):
        subclip = self.origin_audio.subclip(0, 20)
        is_success = self.origin_audio.save_clip(subclip)
        assert is_success is True
