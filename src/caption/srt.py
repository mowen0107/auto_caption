# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180524
'''
from src.caption.caption import Caption


class Srt():
    def __init__(self):
        self.caption_list = []

    def add_caption(self, caption):
        self.caption_list.append(caption.to_string())

    def save_srt(self, file_path):
        print(self.caption_list)
        with open(file_path, 'w') as srt_file:
            srt_file.writelines(self.caption_list)