# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180524
'''
import os


class MediaFile():
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_dir = self.get_file_dir()
        fullname = self.get_fullname()
        self.fullname = fullname
        self.shortname = self.get_shortname(fullname)
        self.filetype = self.get_extension(fullname)

    def get_file_dir(self):
        file_dir = os.path.split(self.file_path)[0]
        return file_dir

    def get_fullname(self):
        ''' 获取带后缀的文件名
        '''
        (file_dir, fullname) = os.path.split(self.file_path)
        print("--- Video.get_file_name, file_dir:{}, fullname:{}".format(
            file_dir, fullname))
        return fullname

    def get_shortname(self, fullname):
        ''' 由带后缀的文件名获取不带后缀的文件名
        '''
        last_do_index = fullname.rindex(".")
        shortname = fullname[:last_do_index]
        return shortname

    def get_extension(self, fullname):
        ''' 获取文件后缀
        '''
        last_do_index = fullname.rindex(".")
        extension = fullname[last_do_index + 1:]
        return extension