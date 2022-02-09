#!/usr/bin/env python3

import os, sys
from PIL import Image

source = os.getcwd() + "/supplier-data/images"
destination = os.getcwd() + "/supplier-data/images"

def get_source_files():
        source_files = os.listdir(source)
        source_files.remove("LICENSE")
        source_files.remove("README")
        print(source_files)
        return source_files

def process_img(file):
        path = source + "/" + file
        im = Image.open(path)
        im = im.resize((600,400))
        im = im.convert("RGB")
        save_file = file.replace("tiff","jpeg")
        im.save(destination + "/" + save_file, format = "jpeg")

if __name__ == "__main__":
        source_files = get_source_files()
        for file in source_files:
                process_img(file)


