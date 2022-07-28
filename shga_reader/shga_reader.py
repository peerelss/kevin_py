# -*- coding: utf-8 -*-
import json
import os

dir = r'C:\Users\kevin\Downloads\shga_sample_750k\p.json'

f = open(dir, encoding="utf8")
line = f.readline()
while line:
    print(line)
    json_d = json.loads(line)
    line = f.readline()

f.close()
