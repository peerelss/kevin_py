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
import unicodedata as ucd
import sdk_every_thing_http

r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_file_from_url = 'redis_set_jav_land_url_thumbs'  # 保存所有已被下载的url
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["av_db"]
mycol = mydb['av_items_thumb']
mycol2 = mydb['av_items_thumb_jav_bus']
mycol3 = mydb['av_items_thumb_jav_luxu']
mycol_en = mydb['av_items_thumb_en']
mycol_giga = mydb['av_items_thumb_giga']
# ，翔田千里，北条麻妃，白石さゆり,里美ゆりあ，小泉彩,澤村レイコ（高坂保奈美、高坂ますみ）, JULIA，村上里沙，竹内紗里奈 ，mdyd,
f_name = '吉沢明歩'
f_dir = r'C:\Users\kevin\Documents\jpg\\' + f_name
av_id = 'Jukujo-' + str(7578)


def search_by_id(av_id):
    search_every_thing_if_file_exist(av_id)
    myquery = {"av_id": av_id}
    result_x = mycol.find(myquery)
    for x in result_x:
        print(x)
        return x


def search_by_series(av_series):
    myquery = {"av_series": av_series}
    result_x = mycol.find(myquery)
    count = mycol.count_documents(myquery)
    print(str(count))
    for x in result_x:
        # save_jpg(x['av_id'], x['av_jpg'])
        if 0 < len(x['av_star']) < 6:
            search_every_thing_if_file_exist(x['av_id'])


def search_every_thing_if_file_exist(av_id):
    av_id = str(av_id).replace('-', ' ')
    if sdk_every_thing_http.if_file_exist(av_id):
        pass
    else:
        print(av_id)


def search_by_name_page(av_name, page_size=20, page_no=1):
    skip = page_size * (page_no - 1)
    myquery = {"av_star": av_name}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, "_id": 0, 'av_star': 1, 'av_maker': 1})
    for x in result_x:
        # save_jpg(x['av_id'], x['av_jpg'])
        if len(x['av_star']) > 0:
            print(x)


def save_jpg(av_id, av_jpg):
    file_name = f_dir + '\\' + av_id + '.jpg'
    ucd.normalize('NFKC', file_name).replace(' ', '')
    print(av_jpg)
    if os.path.exists(file_name):
        print(av_jpg + "  已存在")
    else:
        try:
            html = requests.get(av_jpg).content
            with open(file_name, "wb") as file:
                file.write(html)
        except Exception as e:
            print(av_jpg + "  " + e)


url_temp = 'https://pics.dmm.co.jp/mono/movie/adult/jufdINDEX/jufdINDEXpl.jpg'


def search_aggregate_by_maker():
    page_skip = 20
    page_no = 2
    pipeline = [{'$group': {'_id': "$av_star", 'num_maker': {'$sum': 1}}},
                {'$sort': {'num_maker': -1}},
                {'$match': {'num_maker': {'$gt': 2}}},
                {'$skip': page_skip * page_no},
                {'$limit': page_skip}
                ]

    result_x = mycol.aggregate(pipeline)
    for x in result_x:
        print(x)


def search_name(name):
    myquery = {'av_star': name}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, 'av_title': 1, '_id': 0})
    for x in result_x:
        search_by_if_exist_av_id(x['av_id'])


def search_by_if_exist(name):
    myquery = {"av_star": name}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, "_id": 0, 'av_star': 1, 'av_maker': 1})
    for x in result_x:
        # save_jpg(x['av_id'], x['av_jpg'])
        if 0 < len(x['av_star']) < 6:
            search_every_thing_if_file_exist(x['av_id'])


def search_by_if_exist_by_maker(name):
    myquery = {"av_maker": name}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, "_id": 0, 'av_star': 1, 'av_maker': 1})
    for x in result_x:
        # save_jpg(x['av_id'], x['av_jpg'])
        # if 0 < len(x['av_star']) < 6:
        search_every_thing_if_file_exist(x['av_id'])


def search_by_if_exist_av_id(av_id):
    search_every_thing_if_file_exist(av_id)


def t():
    pass


if __name__ == '__main__':
    search_name('小早川怜子')

    # all = search_by_id('MDYD-239')
    # print(all)
    # search_by_series(series)
    # search_by_if_exist(all['av_star'])
    #  search_by_if_exist_by_maker('シネマジック')

    # search_aggregate_by_maker()
    # search_by_id('JBD-240')
    # save_jpg('ghnu84', 'https://www.giga-web.jp/db_titles/ghnu/ghnu84/pac_l.jpg')
    # index_str = ""

# search_by_if_exist('澤村レイコ（高坂保奈美、高坂ますみ）')
