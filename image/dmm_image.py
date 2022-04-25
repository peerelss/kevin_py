# 下载冷僻的番号
# -*- coding: utf-8 -*-
import json
import sys
import requests
import os
from bs4 import BeautifulSoup
import pymongo
import redis

import requests

r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_file_from_url_luxu = 'redis_set_jav_bus_url_thumbs_luxu'  # 保存所有已被下载的url
redis_tumblr_dir_file_from_url_jav_bus_error = 'redis_set_jav_bus_url_error'  # 保存所有已被下载的url
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["av_db"]
mycol = mydb['av_items_thumb_jav_luxu']

cookies = {
    'coc': '1',
    'PHPSESSID': 'ld30ndg3rfihgrmisvgcvtb994',
    'uuid': '580a6ca5c7a06734b159cf6d3ffaed43',
    'adc': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.mgstage.com/search/cSearch.php?maker[]=%E3%83%A9%E3%82%B0%E3%82%B8%E3%83%A5TV_0&type=top',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'coc=1; PHPSESSID=ld30ndg3rfihgrmisvgcvtb994; uuid=580a6ca5c7a06734b159cf6d3ffaed43; adc=1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
}


# 女优，厂商，图片地址，名称，番号

class AvItem:
    def __init__(self, av_jpg, av_id, av_thumbs):
        self.av_id = av_id
        self.av_jpg = av_jpg
        self.av_thumbs = av_thumbs


def get_detail_from_url(url):
    if r_redis.sismember(redis_tumblr_dir_file_from_url_luxu, url):
        print(url + '  已经被下载过')
        return
    response = requests.get(url, headers=headers, cookies=cookies)
    av_id = url.split('/')[-2]
    soup = BeautifulSoup(response.content, "lxml")
    class_soup = soup.find_all(class_='link_magnify')
    av_jpg = ''
    if len(class_soup) > 0:
        av_jpg = class_soup[0]['href']
    a_soup = soup.find_all('a', href=True)
    av_thumbs = []
    for a in a_soup:
        a_h = a['href']
        if 'image' in a_h:
            av_thumbs.append(a_h)
    av_item = AvItem(av_jpg, av_id, av_thumbs)
    print(av_item.__dict__)
    mycol.insert_one(av_item.__dict__)
    r_redis.sadd(redis_tumblr_dir_file_from_url_luxu, url)


def get_url_from_maker(url):
    response = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.content, "lxml")
    a_soup = soup.find_all('a', href=True)
    for a in a_soup:
        a_h = a['href']
        if a_h.startswith('/product/product_detail'):
            get_detail_from_url('https://www.mgstage.com' + a_h)


if __name__ == '__main__':
    for i in range(1, 14):
        get_url_from_maker(
            "https://www.mgstage.com/search/cSearch.php?maker[]=ラグジュTV_0&search_word=&type=top&page=" + str(i))
