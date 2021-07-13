"""
Author: Konstantin (k0nze) Lübeck
License: BSD 3-Clause License
Copyright (c) 2020 Konstantin (k0nze) Lübeck
"""

import json
import os

from consts import *
from pathlib import Path


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


