# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180524
'''
import pytest
from src.caption.srt import Srt, Caption


class TestSrt():
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

    def test_add_caption(self):
        srt = Srt()
        cap1 = Caption(1, 12.23, 14.42, "test1")
        cap2 = Caption(2, 23.34, 25.22, "test2")
        srt.add_caption(cap1)
        srt.add_caption(cap2)
        assert len(srt.caption_list) == 2

    @pytest.mark.skip(reason='写文件耗时')
    def test_save_srt(self):
        file_path = './resource/output/test_srt.srt'
        cap1 = Caption(1, 12.23, 14.42, "test1")
        cap2 = Caption(2, 23.34, 25.22, "test2")
        srt = Srt()
        srt.add_caption(cap1)
        srt.add_caption(cap2)
        srt.save_srt(file_path)
