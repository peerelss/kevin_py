'''
下载无码的
'''
# -*- coding: utf-8 -*-
import json
import sys
import requests
import os
from bs4 import BeautifulSoup

cookies_dict = {
    "existmag": "all"
}


def get_url_from_maker(url):
    print(url)
    soup = BeautifulSoup(requests.get(url, cookies=cookies_dict).content, "lxml")
    class_soup = soup.find_all(class_='movie-box')
    for p in class_soup:
        print(p['href'])


for i in range(1, 11):
    get_url_from_maker("https://www.javbus.com/label/1fd/" + str(i))
