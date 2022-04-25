'''
下载无码的 tokyo_hot
'''
# -*- coding: utf-8 -*-
import json
import sys
import requests
import os
from bs4 import BeautifulSoup
import pymongo
import redis


def get_movie_from_url(url):
    print(url)


# 从厂商或者女优获取影片链接
def get_url_from_maker(url):
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all('a', href=True)
    for p in pic_soup:
        print(p)


if __name__ == '__main__':
    get_url_from_maker('https://my.tokyo-hot.com/product/?page=2&vendor=Tokyo-Hot')
