# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180528
'''
from src.aip_client import AipClient


class Recognizer():
    def __init__(self):
        self.aip_client = AipClient()

    def recognize(self, fragment):
        audio_content = fragment.audio_content
        audio_recog_result = self.aip_client.recognize_audio(audio_content)
        trans_result = self.aip_client.translate(audio_recog_result)
        return trans_result
