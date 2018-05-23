# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
from aip import AipSpeech

AIP_CONFIG = {
    "APP_ID": "11281269",
    "API_KEY": "n5FPdFuzxFqcfn9VdYaHL7AS",
    "SECRET_KEY": "bbFBo7KRMqQweA6EDGKdRbA8G4bScGqK"
}


class AipClient():
    def __init__(self):
        APP_ID = AIP_CONFIG['APP_ID']
        API_KEY = AIP_CONFIG['API_KEY']
        SECRET_KEY = AIP_CONFIG['SECRET_KEY']
        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def get_recognition_response(self, audio_data):
        try:
            response_json = self.client.asr(audio_data, 'wav', 16000, {
                'dev_pid': 1737
            })
        except Exception as err:
            print("--- AipClient,get_recognition_result,", err)
            raise
        else:
            return response_json
