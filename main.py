# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180521
'''
from src.video.source_video import SourceVideo
from src.video_to_audio import VideoToAudio
from src.audio.fragment_audio import FragmentAudio
from src.recognizer import Recognizer
from src.caption.srt import Srt, Caption


def main():
    srt = Srt()
    recognizer = Recognizer()
    source_video = SourceVideo("./resource/video/test_video.flv")
    origin_audio = VideoToAudio(source_video).gen_audio()
    fragment_info_list = origin_audio.gen_all_fragment()
    for fragment in fragment_info_list:
        order = fragment_info_list.index(fragment)
        file_path = fragment[0]
        start_second = fragment[1]
        end_second = fragment[2]
        fragment_audio = FragmentAudio(order, file_path, start_second,
                                       end_second)
        recog_result = recognizer.recognize(fragment_audio)
        caption = Caption(order, start_second, end_second, recog_result)
        srt.add_caption(caption)
    srt.save_srt("./resource/output/result.srt")


if __name__ == '__main__':
    main()