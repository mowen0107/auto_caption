# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
import pytest
from moviepy.audio.AudioClip import AudioClip
from src.audio.audio import Audio
from src.audio.origin_audio import OriginAudio
from src.plot_img import PlotImg


@pytest.mark.skip(reason="none")
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

    def test_get_right_audioclip(self):
        right_file_path = "./resource/audio/test_video/test_video.wav"
        audio = OriginAudio(right_file_path)
        assert isinstance(audio.audio_clip, AudioClip)

    def test_get_wrong_audioclip(self):
        wrong_file_path = "./resource/audio/test_audio_wrong.wav"
        with pytest.raises(OSError):
            audio = OriginAudio(wrong_file_path)

    def test_get_duration(self):
        right_file_path = "./resource/audio/test_video/test_video.wav"
        audio = OriginAudio(right_file_path)
        duration = audio.get_duration(audio.audio_clip)
        print("--- TestAudio.test_get_duration, duration:{}".format(duration))
        assert duration > 0

    def test_gen_fragment_index(self):
        self.origin_audio.gen_all_fragment()
        fragment_index_df = self.origin_audio.gen_fragment_index()
        print("fragment_index_df:{}".format(fragment_index_df))

    def test_gen_all_fragment(self):
        self.origin_audio.gen_all_fragment()

    def test_all_breakpoint(self):
        breakpoint_list = self.origin_audio.get_all_breakpoint()
        print("breakpoint_list:{}".format(breakpoint_list))
        assert breakpoint_list != [] and breakpoint_list is not None

    def test_get_energe_list(self):
        energe_list = self.origin_audio.get_energe_list(0.4, 0.45)
        # PlotImg.plot_energe_list(energe_list)
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

    @pytest.mark.skip(reason='会覆盖掉原来的文件')
    def test_save_clip(self):
        subclip = self.origin_audio.subclip(0, 20)
        is_success = self.origin_audio.save_clip(subclip)
        assert is_success is True
