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
mycol_giga = mydb['av_items_thumb_giga']
# ，翔田千里，北条麻妃，白石さゆり,里美ゆりあ，小泉彩,澤村レイコ（高坂保奈美、高坂ますみ）, JULIA，村上里沙，竹内紗里奈 ，mdyd,
f_name = '松下紗栄子'
f_dir = r'C:\Users\kevin\Documents\jpg\\' + f_name
av_id = 'Jukujo-' + str(7578)


def search_by_id(av_id):
    myquery = {"av_id": av_id}
    result_x = mycol.find(myquery)
    for x in result_x:
        # save_jpg(x['av_id'], x['av_jpg'])
        print(x)
        print((x['av_star']))


def search_by_series(av_series):
    myquery = {"av_series": av_series}
    result_x = mycol.find(myquery)
    count = mycol.count_documents(myquery)
    print(str(count))
    for x in result_x:
        # save_jpg(x['av_id'], x['av_jpg'])
        print(x)
        # print((x['av_star']))


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
    name = 'SHKD'
    myquery = {'av_title': {'$regex': name}}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, 'av_title': 1, '_id': 0}).limit(30)
    for x in result_x:
        search_every_thing_if_file_exist(x)


def search_by_if_exist(name):
    myquery = {"av_star": name}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, "_id": 0, 'av_star': 1, 'av_maker': 1})
    for x in result_x:
        # save_jpg(x['av_id'], x['av_jpg'])
        if 0 < len(x['av_star']) < 6:
            search_every_thing_if_file_exist(x['av_id'])


str_jukujo = r'7352 7351 7349 7345 7343 7341 7335 7332 7331 7329 7323 7316 7311 7310 7306 7305 7303 7209 7298 7295 7293 7292' \
             r' 7291 7281 7280 7276 7275 7274 7273 7265 7180 7179 7140 7137 7134 7130 7125 7116 7009 6934 6928 6917 6916 6854 6827' \
             r' 6767 6779 6778 6746 6678 6438 6415 6405 6402 6388 6370 6369 6285 6284 6276 6275 6271 6264 6231 6210 6198 6183 6095 6088' \
             r' 5752 5713 5711 5703 5696 5695 5294 5680 5662 5647 5645 5643 5587 5582 5574 5570 5563 5541 5486 5484 5298 5277 5270 5254 5252' \
             r' 5246 5229 5226 5221 5109 5074 5039 5030 5016 4996 4974 4971 4928 4553 4896 4894 4891 4721 4655 4606 4601 4574 4547 4309 4304 4300' \
             r' 4297 4296 4287 4283 4277 4270 4225 4167 4180 4105 4100 4099 4097 4041 4037 4026 3997 3995 3987 3986 3985 3979 3953 3950 3947 3935 3903' \
             r' 3900 3949 3827 3811 3810 3809 3797 '

if __name__ == '__main__':
    if os.path.exists(f_dir):
        pass
    else:
        os.makedirs(f_dir)
    l_jukujo = str_jukujo.split(' ')
    for l in l_jukujo:
        search_every_thing_if_file_exist('jukujo ' + l)
    # search_by_name_page(f_name, 20, 1)
    # search_by_id('SHKD-744')
    # search_by_series('○○の湿ったパンスト')
    # search_name('吉沢明歩')
    # search_aggregate_by_maker()
    # search_by_id('JBD-240')
    # save_jpg('ghnu84', 'https://www.giga-web.jp/db_titles/ghnu/ghnu84/pac_l.jpg')
    # index_str = ""
    # for i in range(1, 1000):
    #     if i < 10:
    #         index_str = '00' + str(i)
    #     elif 9 < i < 100:
    #         index_str = '0' + str(i)
    #     else:
    #         index_str = str(i)
    #     av_id = 'JUFD-' + index_str
    #     #save_jpg(av_id, url_temp.replace('INDEX', index_str))

    # search_by_if_exist('Hitomi（田中瞳）')
