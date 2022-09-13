# -*- coding: utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup

url = r'http://127.0.0.1:258/?search='
url_end = r'&sort=size&ascending=0'


def if_file_exist(av_id):
    pic_soup = BeautifulSoup(requests.get(url + str(av_id).replace('-', ' ') + url_end).content, "lxml")
    sizes = pic_soup.find_all("td", class_="sizedata")
    if len(sizes) < 1:
        return False
    return len((sizes[0].getText())) > 8

