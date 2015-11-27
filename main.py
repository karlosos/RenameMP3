#!/usr/bin/python

import os
import eyed3

def change_file_name(directory):
    for file_name in os.listdir(directory):
        file_path = directory + "/" + file_name
        audiofile = eyed3.load(file_path)
        if audiofile is not None:
            artist =  audiofile.tag.artist
            title = audiofile.tag.title
            print artist + "-" + title + ".mp3"
            new_file_name = artist + "-" + title + ".mp3"
            new_file_path = directory + "/" + new_file_name

            if (artist != "" and title != ""):
                os.rename(file_name, new_file_path)


PATH = os.getcwd()
change_file_name(PATH)
