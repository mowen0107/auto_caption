# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180524
'''
from src.media_file import MediaFile


class TestMediaFile():
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        self.media_file = MediaFile("./resource/video/test_video.flv")

    def teardown_method(self, method):
        pass

    def test_get_file_dir(self):
        file_dir = self.media_file.get_file_dir()
        assert file_dir == "./resource/video"

    def test_get_fullname(self):
        fullname = self.media_file.get_fullname()
        assert fullname == "test_video.flv"

    def test_get_shortname(self):
        shortname = self.media_file.get_shortname("test_video.flv")
        assert shortname == "test_video"

    def test_get_extension(self):
        extension = self.media_file.get_extension("test_video.flv")
        assert extension == "flv"
        extension = self.media_file.get_extension("test.io.flv")
        assert extension == "flv"
