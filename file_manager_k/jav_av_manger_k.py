# -*- coding: UTF8 -*-
import os

dir_path = r"l:qq"
for i in os.listdir(dir_path):
    str_i = str(i)
    if str_i.startswith("Watch") and str_i.endswith('2.mp4'):
        print(str_i)
