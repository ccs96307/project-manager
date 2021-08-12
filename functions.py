# coding: utf-8
"""
The file contains some important function for recording.
"""
import os
import json


class ProjectManager(object):
    def __init__(self):
        # Load the save file
        self.data =  self.load_file()

    def load_file(self):
        save_file_name = "pm_0.json"

        if os.path.isfile(save_file_name):
            json.load(open(save_file_name, 'r'))
        else:



