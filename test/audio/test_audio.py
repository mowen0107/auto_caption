# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
import pytest
from moviepy.audio.AudioClip import AudioClip
from src.audio.audio import Audio


class TestAudio():
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_get_file_dir(self):
        right_file_path = "./resource/audio/test_video/test_video.wav"
        audio = Audio(right_file_path)
        file_dir = audio.get_file_dir()
        assert file_dir == "./resource/audio/test_video"

    def test_get_right_audioclip(self):
        right_file_path = "./resource/audio/test_video/test_video.wav"
        audio = Audio(right_file_path)
        assert isinstance(audio.audio_clip, AudioClip)

    def test_get_wrong_audioclip(self):
        wrong_file_path = "./resource/audio/test_audio_wrong.wav"
        with pytest.raises(OSError):
            audio = Audio(wrong_file_path)

    def test_get_duration(self):
        right_file_path = "./resource/audio/test_video/test_video.wav"
        audio = Audio(right_file_path)
        duration = audio.get_duration(audio.audio_clip)
        print("--- TestAudio.test_get_duration, duration:{}".format(duration))
        assert duration > 0
