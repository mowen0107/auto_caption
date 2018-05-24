# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180524
'''
import time
import math


class Caption():
    def __init__(self, order, start_second, end_second, text):
        self.order = order
        self.start_time = self.format_time(start_second)
        self.end_time = self.format_time(end_second)
        self.text = text

    def format_time(self, seconds):
        (millisec, second_num) = math.modf(seconds)
        millisec = round(millisec * 1000)
        hour_num = int(second_num / 3600)
        second_num -= hour_num * 3600
        minute_num = int(second_num / 60)
        second_num -= minute_num * 60
        time_str = "{}:{}:{},{}".format('%02d' % hour_num, '%02d' % minute_num,
                                        '%02d' % second_num, '%03d' % millisec)
        return time_str

    def to_string(self):
        caption_str = "{}\n\n{} --> {}\n\n{}\n\n".format(
            self.order, self.start_time, self.end_time, self.text)
        return caption_str

    def __repr__(self):
        repr_str = "order:{},start:{},end:{},text:{}".format(
            self.order, self.start_time, self.end_time, self.text)
        return repr_str
