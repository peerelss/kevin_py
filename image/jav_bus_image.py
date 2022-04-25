'''
下载无码的
'''
# -*- coding: utf-8 -*-
import json
import sys
import requests
import os
from bs4 import BeautifulSoup
import pymongo
import redis

r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_file_from_url_jav_bus = 'redis_set_jav_bus_url_thumbs'  # 保存所有已被下载的url
redis_tumblr_dir_file_from_url_jav_bus_error = 'redis_set_jav_bus_url_error'  # 保存所有已被下载的url
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["av_db"]
mycol = mydb['av_items_thumb_jav_bus']
cookies_dict = {
    "existmag": "all"
}


# 女优，厂商，图片地址，名称，番号

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


def get_movie_from_url(url):
    if r_redis.sismember(redis_tumblr_dir_file_from_url_jav_bus, url):
        # 已经下载过
        print(url + "   已经被下载过")
        return
    print(url)
    try:
        soup = BeautifulSoup(requests.get(url, cookies=cookies_dict).content, "lxml")
        av_title_string = soup.find('title')
        if len(av_title_string) == 0:
            r_redis.sadd(redis_tumblr_dir_file_from_url_jav_bus_error, url)
            print(url + '  出现问题')
            return
        av_title = soup.find('title').string.replace(" - JavBus", '')
        av_id = url.split('/')[-1]
        class_soup = soup.find_all(class_='bigImage')
        av_jpg = 'https://www.javbus.com' + class_soup[0]['href']
        av_star = []
        av_maker = ''
        av_thumbs = []
        av_series = ''
        av_tags = []
        star_soup = soup.find_all(class_='star-name')
        for s in star_soup:
            av_star.append(s.text)
        href_soup = soup.find_all('a', href=True)
        for h in href_soup:
            h_href = h['href']
            if 'studio' in h_href:
                av_maker = h.text
            if 'bigsample' in h_href:
                av_thumbs.append('https://www.javbus.com' + h_href)
            if 'series' in h_href:
                av_series = h.text
            if 'genre' in h_href:
                if h.text in av_tags:
                    pass
                else:
                    av_tags.append(h.text)

        av_item = AvItem(av_star, av_maker, av_tags, av_jpg, av_title, av_id, av_thumbs, av_series)
        print(av_item.__dict__)
        mycol.insert_one(av_item.__dict__)
        r_redis.sadd(redis_tumblr_dir_file_from_url_jav_bus, url)
    except:
        r_redis.sadd(redis_tumblr_dir_file_from_url_jav_bus_error, url)
        print(url + '  出现问题')


# 从厂商或者女优获取影片链接
def get_url_from_maker(url):
    print(url)
    soup = BeautifulSoup(requests.get(url, cookies=cookies_dict).content, "lxml")
    class_soup = soup.find_all(class_='movie-box')
    for p in class_soup:
        get_movie_from_url(p['href'])
    id_soup = soup.find_all(id='next')
    return len(id_soup)


def search_jav_bus():
    myquery = {"av_star": '長月ラム'}
    result_x = mycol.find(myquery)
    for x in result_x:
        print(x)


if __name__ == '__main__':
    i = 1
    while get_url_from_maker('https://www.javbus.com/uncensored/studio/3x/' + str(i)):
        i = i + 1
    # get_movie_from_url('https://www.javbus.com/HEY-021')
    # search_jav_bus()
