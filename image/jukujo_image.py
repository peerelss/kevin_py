# -*- coding: utf-8 -*-
import json
import sys
import requests
import os
from bs4 import BeautifulSoup

url = r'https://image.jukujo-club.com/image/INDEX/movie_main.jpg'
dir = r'C:\Users\kevin\Documents\jpg\\'

for i in range(1, 100):
    html = requests.get(url.replace('INDEX', str(i)))
    with open(dir + str(i) + '_jukujo.jpg', "wb") as file:
        file.write(html.content)
