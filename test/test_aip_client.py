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

    @pytest.mark.skip(reason="请求百度api很耗时间")
    def test_get_recognition_result(self):
        test_audio_path = "./resource/audio/test_video/fragment_0.wav"
        with open(test_audio_path, 'rb') as fp:
            audio_data = fp.read()
        response_json = self.aip_client.get_recognition_response(audio_data)

        if response_json['err_no'] == 0:
            result = response_json['result'][0]
            print("--- TestAipClient,test_get_recognition_result, result:{}".
                  format(result))
            assert isinstance(result, str)
            assert result != '' and result is not None
