# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
from moviepy.audio.AudioClip import AudioClip
from src.video.source_video import SourceVideo
from src.audio.origin_audio import OriginAudio
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

    def test_gen_audio(self):
        audio = self.video_to_audio.gen_audio()
        assert isinstance(audio, OriginAudio)

    def test_is_dir_exist(self):
        assert self.video_to_audio.is_dir_exist() is True
        self.video_to_audio.audio_output_dir = "wrong_path"
        assert self.video_to_audio.is_dir_exist() is False

    def test_create_dir(self):
        self.video_to_audio.create_dir()
        assert self.video_to_audio.is_dir_exist() is True
