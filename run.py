#! /usr/bin/env python3

import os
import requests
import json
import re

source = os.getcwd() + "/supplier-data/descriptions"
url = ""
post_url = "http://{}/fruits".format(url)

def get_files(direc):
	return os.listdir(direc)

def process_files(files):
	for file in files:
		dict = file_to_dict(file)
		post_json(dict)
		print(dict)

def file_to_dict(file):
	with open(source + "/" + file) as opened:
		lines = opened.read().splitlines()
		dict = {"name": lines[0], "weight": remove_char(lines[1]), "description": lines[2].strip(), "image_name": txt_to_jpeg(file)}
		return json.dumps(dict)

def remove_char(line):
	return int(re.match(r'\d*', line)[0])

def txt_to_jpeg(file):
	return re.match(r'(.*)\.txt', file).group(1) + ".jpeg"

def post_json(json):
	requests.post(post_url, data = json)

if __name__ == "__main__":
	files = get_files(source)
	process_files(files)
