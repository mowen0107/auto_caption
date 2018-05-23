# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180522
'''
import numpy as np
import moviepy
from src.audio.audio import Audio


class OriginAudio(Audio):
    def __init__(self, file_path):
        Audio.__init__(self, file_path)
        self.order = 0

    def get_all_breakpoint(self):
        ''' 获得这段audio中所有停顿对应的时间轴位置(second)
        '''
        pass

    def get_energe_list(self, step_time=0.5, duration=0.5):
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
        subclip = self.audio_clip.subclip(start_second, end_second)
        return subclip

    def save_clip(self, subclip):
        fragment_path = self.file_dir + '/fragment_{}.wav'.format(self.order)
        try:
            subclip.write_audiofile(
                fragment_path,
                fps=16000,
                codec='pcm_s16le',
                ffmpeg_params=['-f', 's16le', '-ac', '1'])
        except Exception as err:
            raise
        else:
            return True
