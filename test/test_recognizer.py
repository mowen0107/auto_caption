# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180528
'''

import pytest
from multiprocessing.pool import Pool
from src.audio.fragment_audio import FragmentAudio
from src.recognizer import Recognizer


class TestRecognizer():
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

    def test_recognize(self):
        recognizer = Recognizer()
        fragment = FragmentAudio(
            0, './resource/audio/test_video/fragment_0.wav', 2, 3)
        trans_result = recognizer.recognize(fragment)
        assert trans_result != "" and trans_result is not None
