# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
from moviepy.audio.AudioClip import AudioClip
from src.audio.audio import Audio
from src.audio.origin_audio import OriginAudio
from src.plot_img import PlotImg


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

    def test_get_energe_list(self):
        energe_list = self.origin_audio.get_energe_list(0.1, 0.1)
        PlotImg.plot_energe_list(energe_list)
        assert energe_list != [] and energe_list is not None

    def test_count_energe(self):
        energe = self.origin_audio.count_energe(0, 1)
        print("energe:{}".format(energe))
        assert energe > 0
        assert self.origin_audio.count_energe(self.origin_audio.duration,
                                              1) == 0
        assert self.origin_audio.count_energe(self.origin_audio.duration + 1,
                                              1) == 0

    def test_get_frames(self):
        frame_list = self.origin_audio.get_frames()
        assert frame_list != [] and frame_list is not None
        print("frame_list:{}".format(frame_list))

    def test_subclip(self):
        subclip = self.origin_audio.subclip(0, 20)
        assert isinstance(subclip, AudioClip)
        assert subclip.duration > 0
        print("duration:{}".format(subclip.duration))

    def test_save_clip(self):
        subclip = self.origin_audio.subclip(0, 20)
        is_success = self.origin_audio.save_clip(subclip)
        assert is_success is True
