# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
import pandas as pd
import numpy as np
import moviepy
from moviepy.editor import AudioFileClip
from src.audio.audio import Audio


class OriginAudio(Audio):
    def __init__(self, file_path):
        Audio.__init__(self, file_path)
        self.order = 0
        self.fragment_info = []
        audio_clip = self.get_audio_clip()
        self.audio_clip = audio_clip
        self.duration = self.get_duration(audio_clip)

    def get_audio_clip(self):
        try:
            audio_clip = AudioFileClip(self.file_path)
        except OSError as err:
            raise
        else:
            return audio_clip

    def get_duration(self, audio_clip):
        duration = audio_clip.duration
        return duration

    def gen_all_fragment(self):
        ''' 由停顿点位置把origin_audio切割成一个个的fragment
        '''
        fragment_period_list = self.get_fragment_period()

        for fragment_period in fragment_period_list:
            start_second = fragment_period[0]
            end_second = fragment_period[1]
            fragment_path = self.file_dir + '/fragment_{}.wav'.format(
                self.order)
            self.fragment_info.append(
                [fragment_path, start_second, end_second])
            subclip = self.subclip(start_second, end_second)
            self.save_clip(subclip, fragment_path)
            self.order += 1
        return self.fragment_info

    def get_fragment_period(self):
        threshold = 0.1
        period_list = []
        period = []
        energe_list = self.get_energe_list(0.4, 0.45)
        for point in energe_list:
            the_time = point['time']
            is_start = self.is_start_point(point, energe_list, threshold)
            is_end = self.is_end_point(point, energe_list, threshold)
            if is_end:
                print("end", the_time)
                period.append(the_time)
                period_list.append(period)
                period = []
            if is_start:
                print("start", the_time)
                period.append(the_time)
        return period_list

    def is_start_point(self, point, energe_list, threshold):
        index = energe_list.index(point)
        energe = point['energe']

        if energe > threshold and index == 0:
            return True
        elif energe < threshold and index == len(energe_list) - 1:
            return False
        elif energe < threshold and energe_list[index
                                                + 1]['energe'] > threshold:
            return True
        else:
            return False

    def is_end_point(self, point, energe_list, threshold):
        index = energe_list.index(point)
        energe = point['energe']

        if energe > threshold and index == len(energe_list) - 1:
            return True
        elif energe < threshold and index == 0:
            return False
        elif energe < threshold and energe_list[index
                                                - 1]['energe'] > threshold:
            return True
        else:
            return False

    def get_energe_list(self, step_time, duration):
        energe_list = []
        for t in np.arange(0, self.duration, step_time):
            energe = self.count_energe(t, duration)
            energe_list.append({'time': t, 'energe': energe})
        return energe_list

    def count_energe(self, start_time, duration):
        energe = 0
        end_time = start_time + duration
        if start_time >= self.duration:
            return 0
        elif end_time > self.duration:
            end_time = self.duration
        for i in np.arange(start_time, end_time, 0.01):
            wav_value = self.audio_clip.get_frame(i)[0]
            energe += wav_value * wav_value
        return energe

    def get_frames(self):
        frame_list = []
        for i in range(0, int(self.duration)):
            frame_list.append(self.audio_clip.get_frame(i)[0])
        return frame_list

    def subclip(self, start_second, end_second):
        if end_second > self.duration:
            end_second = self.duration
        subclip = self.audio_clip.subclip(start_second, end_second)
        return subclip

    def save_clip(self, subclip, fragment_path):
        try:
            subclip.write_audiofile(
                fragment_path,
                fps=16000,
                codec='pcm_s16le',
                ffmpeg_params=['-f', 's16le', '-ac', '1', '-y'])
        except Exception as err:
            raise
        else:
            return True
