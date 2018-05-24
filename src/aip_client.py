# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
from aip import AipSpeech
from src.config import AIP_CONFIG


class AipClient():
    def __init__(self):
        APP_ID = AIP_CONFIG['APP_ID']
        API_KEY = AIP_CONFIG['API_KEY']
        SECRET_KEY = AIP_CONFIG['SECRET_KEY']
        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def recognize_audio(self, audio_data):
        try:
            response_json = self.client.asr(audio_data, 'wav', 16000, {
                'dev_pid': 1737
            })
        except Exception as err:
            print("--- AipClient,get_recognition_result,", err)
            raise
        else:
            if response_json['err_no'] == 0:
                result = response_json['result'][0]
                return result
            else:
                print("err_no:{}".format(response_json['err_no']))
                return "met error when recognized audio"
