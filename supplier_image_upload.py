!/usr/bin/env python3

import os
import requests

source = os.getcwd() + "/supplier-data/images"

def get_files_from_dir(direc):
        return os.listdir(direc)

def get_files_by_extension(files, extension):
        fileret = []
        for file in files:
                if extension in file:
                        fileret += [source + "/" + file]
        print(fileret)
        return fileret

def upload(files):
        url = "http://localhost/upload/"
        for file in files:
                print(file)
                with open(file, 'rb') as opened:
                        r = requests.post(url, files={'file': opened})

if __name__ == "__main__":
        files = get_files_from_dir(source)
        jpegs = get_files_by_extension(files, ".jpeg")
        upload(jpegs)


