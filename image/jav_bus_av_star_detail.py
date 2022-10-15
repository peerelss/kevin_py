'''
下载无码的
'''
# -*- coding: utf-8 -*-
import json
import sys
import requests
import os
from bs4 import BeautifulSoup


def get_jpg_list_from_url(url):
    print(url)
    is_going = False  # 是否继续
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all('img')
    for p in pic_soup:
        print(p['src'])
        is_going = True
    return is_going


if __name__ == "__main__":
    url_begin = 'https://jav.land/ja/star/7mkg2x.html'
    if True:
        index = 1
        while get_jpg_list_from_url(url_begin + '?page=' + str(index)):
            index = index + 1
