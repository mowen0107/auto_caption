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

    def gen_fragment_index(self):
        ''' 生成一个fragment的索引文件
        '''
        csv_path = self.file_dir + '/' + 'fragment_index.csv'
        columns = ['file_path', 'start_second', 'end_second']
        fragment_index_df = pd.DataFrame(
            data=self.fragment_info, columns=columns)
        fragment_index_df.to_csv(
            csv_path, sep=',', index=True, columns=columns)
        return fragment_index_df

    def gen_all_fragment(self):
        ''' 由停顿点位置把origin_audio切割成一个个的fragment
        '''
        breakpoint_list = self.get_all_breakpoint()
        for i in range(0, len(breakpoint_list)):
            start_second = breakpoint_list[i]
            if i == len(breakpoint_list) - 1:
                end_second = self.duration
            else:
                end_second = breakpoint_list[i + 1]
            fragment_path = self.file_dir + '/fragment_{}.wav'.format(
                self.order)
            self.fragment_info.append(
                [fragment_path, start_second, end_second])
            subclip = self.subclip(start_second, end_second)
            self.save_clip(subclip, fragment_path)
            self.order += 1
        return self.fragment_info

    def get_all_breakpoint(self):
        ''' 获得这段audio中所有停顿对应的时间轴位置(second)
        '''
        threshold = 0.1
        breakpoint_list = []
        energe_list = self.get_energe_list(0.4, 0.45)
        is_above = True
        for point in energe_list:
            the_time = point['time']
            energe = point['energe']
            if energe < threshold and is_above:
                breakpoint_list.append(the_time)
                is_above = False
            elif energe < threshold and not is_above:
                continue
            else:
                is_above = True
        return breakpoint_list

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
