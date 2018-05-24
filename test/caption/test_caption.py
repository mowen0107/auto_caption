# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180524
'''
from src.caption.caption import Caption


class TestCaption():
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

    def test_format_time(self):
        caption = Caption(0, 12.01, 13.02, "hello")
        time_str = caption.format_time(12.01)
        assert time_str == "00:00:12,010"
        time_str = caption.format_time(62.81)
        assert time_str == "00:01:02,810"
        time_str = caption.format_time(3605.51)
        assert time_str == "01:00:05,510"

    def test_to_string(self):
        caption_str = Caption(0, 12.01, 13.02, "hello").to_string()
        assert caption_str == "0\n\n00:00:12,010 --> 00:00:13,020\n\nhello\n\n"
        print(caption_str)

    def test_repr(self):
        print(Caption(0, 12.01, 13.02, "hello"))
        print(Caption(0, 14.51, 16.72, "world"))
        print(Caption(0, 17.34, 19.23, "and me"))
