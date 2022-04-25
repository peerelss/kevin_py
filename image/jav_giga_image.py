# -*- coding: utf-8 -*-
import json
import sys
import requests
import os
from bs4 import BeautifulSoup
import pymongo
import redis
from urllib.parse import urljoin

r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_file_from_url_giga = 'redis_set_jav_land_url_thumbs_giga_jp'  # 保存所有已被下载的url
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["av_db"]
mycol = mydb['av_items_thumb_giga_jp']


class AvItem:
    def __init__(self, av_star, av_maker, av_tags, av_jpg, av_title, av_id, av_thumbs, av_series):
        self.av_id = av_id
        self.av_star = av_star
        self.av_maker = av_maker
        self.av_tags = av_tags
        self.av_jpg = av_jpg
        self.av_title = av_title
        self.av_thumbs = av_thumbs
        self.av_series = av_series


cookies = {
    'WSLB': 'www1',
    'PHPSESSID': 'is6j7nst0pp470tae8n69aaoet',
    'old_check': 'yes',
    'layout': 'jpn',
    'giga_footstamp': '6824',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Referer': 'https://www.giga-web.jp/search/index.php?count=2&year=&month=&day=&narrow=&salesform_id=&tag_id=&actor_id=&series_id=&label_id=&sort=1&s_type=&keyword=',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'WSLB=www1; PHPSESSID=is6j7nst0pp470tae8n69aaoet; old_check=yes; layout=jpn; giga_footstamp=6824',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}

params = {
    'count': '1',
    'year': '',
    'month': '',
    'day': '',
    'narrow': '',
    'salesform_id': '',
    'tag_id': '',
    'actor_id': '',
    'series_id': '',
    'label_id': '',
    'sort': '1',
    's_type': '',
    'keyword': '',
}


def get_movie_from_url(url):
    print(url)
    response = requests.get(url, headers=headers, params=params,
                            cookies=cookies).content
    pic_content = BeautifulSoup(response, 'lxml')
    pic_soup = pic_content.find_all('a', href=True)
    for p in pic_soup:
        p_h = p['href']
        if 'index.php?product_id' in p_h:
            get_movie_detail_from_url(urljoin('https://www.giga-web.jp/', p_h))


def get_movie_detail_from_url(url):
    if r_redis.sismember(redis_tumblr_dir_file_from_url_giga, url):
        # 已经下载过
        print(url + "   已经被下载过")
        return
    response = requests.get(url, headers=headers, params=params,
                            cookies=cookies).content
    pic_content = BeautifulSoup(response, 'lxml')
    av_title = av_title = pic_content.find('title').string
    pic_soup = pic_content.findAll('img')
    av_jpg = ''
    av_id = ''
    av_star = ''
    av_series = ''
    av_maker = 'giga_jp'
    av_tags = []
    av_thumbs = []
    for p in pic_soup:
        p_s = str(p['src'])
        if 'db_titles' in p_s:
            if 'sample' in p_s:
                av_thumbs.append('https://www.giga-web.jp/' + p_s)
            else:
                av_jpg = (p_s.replace('ss.jpg', 'l.jpg').replace('s.jpg', 'l.jpg'))
    if av_jpg:
        av_id = av_jpg.split('/')[-2]
    a_soup = pic_content.find_all('a', href=True)
    for a in a_soup:
        a_h = a['href']
        if 'actor_id' in a_h:
            av_star = a.text
        if 'series_id' in a_h:
            av_series = a.txt
    av_item = AvItem(av_star, av_maker, av_tags, av_jpg, av_title, av_id, av_thumbs, av_series)
    print(av_item.__dict__)
    mycol.insert_one(av_item.__dict__)
    r_redis.sadd(redis_tumblr_dir_file_from_url_giga, url)


def save_av_item(content):
    pass


if __name__ == '__main__':
    if True:
        for i in range(1, 190):  # 190
            params['count'] = i
            get_movie_from_url('https://www.giga-web.jp/search/index.php')
    # get_movie_detail_from_url('https://www.akiba-web.com/product/index.php?product_id=1379')
