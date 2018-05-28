# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
from aip import AipSpeech
from googletrans import Translator
from src.config import AIP_CONFIG


class AipClient():
    def __init__(self):
        APP_ID = AIP_CONFIG['APP_ID']
        API_KEY = AIP_CONFIG['API_KEY']
        SECRET_KEY = AIP_CONFIG['SECRET_KEY']
        self.audio_recognition_client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        self.translation_client = Translator(
            service_urls=['translate.google.cn'])

    def recognize_audio(self, audio_data):
        try:
            response_json = self.audio_recognition_client.asr(
                audio_data, 'wav', 16000, {
                    'dev_pid': 1737
                })
        except Exception as err:
            print("--- AipClient,get_recognition_result,", err)
            raise
        else:
            if response_json['err_no'] == 0:
                result = response_json['result'][0]
                # 返回最佳识别结果的字符串
                return result
            else:
                print("err_no:{}".format(response_json['err_no']))
                return "met error when recognized audio"

    def translate(self, str_to_trans):
        trans_result = self.translation_client.translate(
            str_to_trans, dest='zh-CN').text
        print("translation_result:{}".format(trans_result))
        return trans_result
