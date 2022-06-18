#! /usr/bin/env python3

import os
import requests

#location of the files
data = "/data/feedback/"

files = os.listdir(data)

#function to open files as list
def readlines(file):
 with open(data + file) as f:
  lines = f.read().splitlines()
 return lines

#going through the files and colect the data
feedback = []
keys = ["title", "name", "date", "feedback"]
for file in files:
 lines = readlines(file)
 feedback.append(dict(zip(keys, lines)))

#link to the feedbackform to entry the data
url = "http://35.222.196.219/feedback/"

#entering the data and getting answer back if complete or failed
for entry in feedback:
 response = requests.post(url, data=entry)
 if response.ok:
  print("complete")
 else:
  print("load error: {response.status_code}")
