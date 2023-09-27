# -*- coding: utf-8 -*-
import json
import sys
import requests
import os
from bs4 import BeautifulSoup
import pymongo
import redis

r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_file_from_url = 'redis_set_jav_land_url_thumbs_en'  # 保存所有已被下载的url
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["av_db"]
mycol_en = mydb['av_items_thumb_en']
mycol = mydb['av_items_thumb']


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


def get_jpg_list_from_url(url):
    print(url)
    is_going = False  # 是否继续
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all('a', href=True)
    for p in pic_soup:
        href = p['href']
        if str(href).startswith('/ja/movie'):
            is_going = True
            get_jpg_from_dmm('https://jav.land' + p['href'])
    return is_going


def get_jpg_from_dmm(url):
    pic_content = BeautifulSoup(requests.get(url).content, 'lxml')
    av_title = (pic_content.find('title').string.replace("- JAV.Land", ''))
    av_id = av_title.split(" ")[0]
    soup_jpg = pic_content.find_all('img')[0]['src']
    print(soup_jpg)


def get_jpg_url_from_url(url):
    if r_redis.sismember(redis_tumblr_dir_file_from_url, url):
        # 已经下载过
        print(url + "   已经被下载过")
        return
    print(url)
    pic_content = BeautifulSoup(requests.get(url).content, 'lxml')
    pic_soup = pic_content.find_all('a', href=True)
    if len(pic_soup) < 1:
        return
    av_tags = []
    av_star = []
    av_maker = ""
    av_thumbs = []
    av_series = ''
    for p in pic_soup:
        href = p['href']
        if str(href).startswith('../genre/'):
            av_tags.append(p.text)
        if str(href).startswith('../maker/'):
            av_maker = p.text
        if str(href).startswith('../star/'):
            av_star.append(p.text)
        if str(href).startswith('https://pics.vpdmm.'):
            av_thumbs.append(str(href))
        if str(href).startswith("../series/"):
            av_series = p.text
    av_title = (pic_content.find('title').string.replace("- JAV.Land", ''))
    av_id = av_title.split(" ")[0]
    soup_jpg = pic_content.find_all('img')[0]['src']
    av_item = AvItem(av_star, av_maker, av_tags, soup_jpg, av_title, av_id, av_thumbs, av_series)
    x = mycol.insert_one(av_item.__dict__)
    r_redis.sadd(redis_tumblr_dir_file_from_url, url)


def search_av_item():
    myquery = {"av_star": '松下紗栄子'}
    result_x = mycol.find(myquery)
    for x in result_x:
        print(x)


def get_image_from_index_page(url, max_index):
    for i in range(1, max_index + 1):
        pic_content = BeautifulSoup(requests.get(url + str(i)).content, 'lxml')
        img_tags = pic_content.find_all('img')
        for img in img_tags:
            src = img.get('src')
            print(src)


if __name__ == "__main__":
    ''' url_begin = 'https://jav.land/ja/star/7mkg2x.html'
     if True:
         index = 1
         while get_jpg_list_from_url(url_begin + '?page=' + str(index)):
             index = index + 1
             '''
    # get_jpg_url_from_url("https://jav.land/ja/movie/javzpj15ldp.html")
    # if r_redis.sismember(redis_tumblr_dir_file_from_url,'https://jav.land/en/movie/jav8wvxv14p.html'):
    #    print('  exist url')
    get_image_from_index_page('https://jav.land/en/maker/vdyxkl.html?page=', 176)
