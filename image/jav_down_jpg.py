# -*- coding: utf-8 -*-
import json
import sys
import requests
import os
from bs4 import BeautifulSoup
import pymongo
import redis

r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_file_from_url = 'redis_set_jav_land_url_thumbs'  # 保存所有已被下载的url
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["av_db"]
mycol = mydb['av_items_thumb']
mycol2 = mydb['av_items_thumb_jav_bus']
mycol3 = mydb['av_items_thumb_jav_luxu']
mycol_giga = mydb['av_items_thumb_giga']

f_name = '熟女倶楽部'
f_dir = r'F:\movies\images\jpg\cinemagic'


def search_by_name_page(av_name, page_size=20, page_no=1):
    skip = page_size * (page_no - 1)
    myquery = {"av_maker": 'giga'}
    result_x = mycol_giga.find(myquery, {'av_id': 1, 'av_jpg': 1, "_id": 0})
    for x in result_x:
        save_jpg(x['av_id'], x['av_jpg'])


def save_jpg(av_id, av_jpg):
    file_name = f_dir + av_id + '.jpg'
    print(av_jpg)
    if os.path.exists(file_name):
        print(av_jpg + "  已存在")
    else:
        try:
            html = requests.get(av_jpg).content
            with open(file_name, "wb") as file:
                file.write(html)
        except Exception as e:
            print(av_jpg + str(e))


def search_and_down_by_star(name):
    myquery = {"av_star": name}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, "_id": 0})
    for x in result_x:
        print('av_id')
        save_jpg(x['av_id'], x['av_jpg'])


def search_and_down_by_maker(name):
    myquery = {"av_maker": name}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, 'av_maker': 1, "_id": 0})
    for x in result_x:
        av_id = x['av_id']

        print(x['av_id'] + "   " + x['av_jpg'])
        save_jpg(x['av_id'], x['av_jpg'])


def search_by_id(av_id):
    myquery = {"av_maker": '熟女倶楽部'}
    result_x = mycol2.find(myquery, {'av_id': 1, 'av_jpg': 1, 'av_maker': 1, "_id": 0})
    for x in result_x:
        print(x)


if __name__ == '__main__':
    # search_by_name_page('松下纱荣子', 20, 1)
    # save_jpg('ghnu84', 'https://www.giga-web.jp/db_titles/ghnu/ghnu84/pac_l.jpg')
    if os.path.exists(f_dir):
        pass
    else:
        os.mkdir(f_dir)
    # search_and_down_by_star(f_name)
    search_and_down_by_maker(f_name)
    # search_by_id('Jukujo-7700')
