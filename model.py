"""
Author: Konstantin (k0nze) Lübeck
License: BSD 3-Clause License
Copyright (c) 2021 Konstantin (k0nze) Lübeck
"""

import json
import os
import subprocess
import threading
import time
import sys

from consts import *
from pathlib import Path
from subprocess import check_output
from sys import platform

class JsonFileCreateException(Exception):
    """ raised when json model could not be created """
    pass


class JsonFileOpenException(Exception):
    """ raised when json model could not be opened """
    pass


class JsonFileWriteException(Exception):
    """ raised when json model could not be written """
    pass


class DirCreationException(Exception):
    """ raised when """
    pass

class CopyFileException(Exception):
    """ raised when """
    pass


class Model():
    def __init__(self, data_path):

        self.data_path = data_path

        # check if ~/.FILE_NAME exists
        if not self.data_path.is_dir(): 
            # try to create ~/.FILE_NAME dir
            try:
                os.mkdir(self.data_path)
            except Exception as e:
                raise DirCreationException

        self.conversion_finished = True 

        # check if data.json exists
        self.json_path = Path.joinpath(self.data_path, 'data.json') 

        self.data = dict()
        
        if not self.json_path.is_file():
            # try to create the json model
            try:
                with open(self.json_path.resolve(), 'w') as json_file:

                    self.data = { "template": "template" }
                
                    json.dump(self.data, json_file, sort_keys=True, indent=4)

            except Exception as e:
                raise JsonFileCreateException 

        # read config
        else: 
            with open(self.json_path.resolve(), 'r') as json_file:
                self.data = json.load(json_file)

        self.observers = []


    def register_observer(self, observer):
        self.observers.append(observer)


    def __notify_observers(self):
        for observer in self.observers:
            observer.notify()

    def __save_json(self):
        try:
            with open(self.json_path.resolve(), 'w') as json_file:
                json.dump(self.data, json_file, sort_keys=True, indent=4)

        except Exception as e:
            raise JsonFileWriteException

    def get_output_file_path(self, input_file_path_string, output_file_directory_string):
        input_file_name = os.path.basename(input_file_path_string)
        output_file_path_string = os.path.join(output_file_directory_string, os.path.splitext(input_file_name)[0] + ".webm")
        return output_file_path_string

    def convert_to_webm(self, input_file_path_string, output_file_path_string, log):
        self.input_file_path_string = input_file_path_string
        self.output_file_path_string = output_file_path_string
        self.log = log
        self.conversion_finished = False

        ffmpeg_thread = threading.Thread(target=self.start_ffmpeg_conversion)

        ffmpeg_thread.setDaemon(True)
        ffmpeg_thread.start()

        self.log("converting")

        update_log_thread = threading.Thread(target=self.start_update_log)

        update_log_thread.setDaemon(True)
        update_log_thread.start()

    def start_ffmpeg_conversion(self):
        if sys.platform.startswith('win32'):
            process = subprocess.Popen(["ffmpeg.exe\\ffmpeg.exe", "-i", self.input_file_path_string, "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-crf", "15", "-b:v", "2M", self.output_file_path_string])
        elif sys.platform.startswith('linux'):
            process = subprocess.Popen(["ffmpeg", "-i", self.input_file_path_string, "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-crf", "15", "-b:v", "2M", self.output_file_path_string])

        stdout, stderr = process.communicate()
        return_value = process.wait()

        #out, err = process.communicate()

        self.conversion_finished = True

        #print(out)
        #print(err)

        #self.log("\n" + err.decode('utf-8'))
        self.log("\ndone")

    def start_update_log(self):
        while not self.conversion_finished:
            self.log(".")
            time.sleep(1)