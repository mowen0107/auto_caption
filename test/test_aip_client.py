# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
import pytest
from src.aip_client import AipClient


class TestAipClient():
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        self.aip_client = AipClient()

    def teardown_method(self, method):
        pass

    @pytest.mark.skip(reason="很耗时间，需要使用百度api")
    def test_get_recognition_result(self):
        result_list = []
        for i in range(0, 17):
            audio_path = "./resource/audio/test_video/fragment_{}.wav".format(
                i)
            with open(audio_path, 'rb') as fp:
                audio_data = fp.read()
            result = self.aip_client.recognize_audio(audio_data)
            print("--- TestAipClient,test_get_recognition_result, result:{}".
                  format(result))
            result_list.append(result)
        print("result_list:{}".format(result_list))

    def test_translate(self):
        trans_str = self.aip_client.translate("hello world")
        assert trans_str == "你好，世界"
