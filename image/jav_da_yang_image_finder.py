# -*- coding: utf-8 -*-
import json
import sys
import requests
import os
from bs4 import BeautifulSoup
import pymongo
import redis
import re
from bson.json_util import dumps, loads
import urllib

r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_file_from_url = 'redis_set_jav_land_url_thumbs_da_yang'  # 保存所有已被下载的url
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["av_db"]
mycol = mydb['av_items_thumb']
mycol2 = mydb['av_items_thumb_jav_bus']
mycol3 = mydb['av_items_thumb_jav_luxu']
mycol_giga = mydb['av_items_thumb_giga']


class AvItem:
    def __init__(self, av_maker, av_jpg, av_title, av_id):
        self.av_id = av_id
        self.av_maker = av_maker
        self.av_jpg = av_jpg
        self.av_title = av_title


def find_movie_from_url(url):
    print(url)
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all('a', href=True)
    for p in pic_soup:
        href = p['href']
        if 'sp_artist_product_detail' in href:
            find_detail_from_movie('https://pureadult.co.jp' + href)


def find_detail_from_movie(url):
    if r_redis.sismember(redis_tumblr_dir_file_from_url, url):
        print('exist ' + url)
        return
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml")
    a_soup = pic_soup.find_all('a', href=True)
    av_jpg = ''
    av_title = ''
    av_maker = '大洋図書'
    for p in a_soup:
        href = p['href']
        if 'sp_images' in href:
            av_jpg = ('https://pureadult.co.jp' + href)
    av_title = (pic_soup.find('title').string.split(' ')[-1])
    av_id = av_jpg.split('/')[-1].replace('.jpg', '')
    av_item = AvItem(av_maker, av_jpg, av_title, av_id)
    print(av_item.__dict__)
    mycol.insert_one(av_item.__dict__)
    r_redis.sadd(redis_tumblr_dir_file_from_url, url)


if __name__ == "__main__":
    if True:
        for i in range(1, 14):
            url_begin = 'https://pureadult.co.jp/user_data/sp_artist_product.php?mid=71&pageID=' + str(i)
            find_movie_from_url(url_begin)
    # find_detail_from_movie(
    #  'https://pureadult.co.jp/user_data/sp_artist_product_detail.php?pid=126023773000&mid=71&bck=%2Fuser_data%2Fsp_artist_product.php%3Fmid%3D71%26pageID%3D2')
