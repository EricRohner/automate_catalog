#! /usr/bin/env python3

import os
import requests

source = os.getcwd() + "/supplier-data/descriptions"

def get_files(direc):
        return os.listdir(direc)

def process_files(files):
        json = {}
        return json

def upload_json():
        #do the thing
        pass

if __name__ == "__main__":
        files = get_files(source)
        print(files)
        json = process_files(files)
