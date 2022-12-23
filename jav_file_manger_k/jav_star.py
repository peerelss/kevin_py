# -*- coding: utf-8 -*-
'''
搜索女优或者厂商或者特征对应的所有影片，存入数据库
字段为  番号，女优，厂商，名称，图片链接，特征，系列

'''

import pymongo
import redis
import random

r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_file_from_url = 'redis_set_jav_land_url_thumbs'  # 保存所有已被下载的url
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["av_db"]
mycol = mydb['av_items_thumb']
mycol2 = mydb['av_items_thumb_jav_bus']
mycol3 = mydb['av_items_thumb_jav_luxu']
mycol_giga = mydb['av_items_thumb_giga']
mycol_en = mydb['av_items_thumb_en']


def search_id(av_id):
    for i in range(1, 2):
        print(random.randint(0, 3) + 39)
    myquery = {"av_id": av_id}
    result_x = mycol_en.find(myquery, {'av_id': 1, 'av_jpg': 1, 'av_title': 1, "_id": 0})
    for x in result_x:
        print(x)


def search_av_maker(av_maker, page_size, page_no):
    myquery = {"av_maker": av_maker}
    skip = page_size * (page_no - 1)
    result_x = mycol_en.find(myquery, {'av_id': 1, 'av_jpg': 1, 'av_title': 1, "_id": 0}).limit(
        page_size).skip(skip)
    for x in result_x:
        print(x)
    count = mycol_en.count_documents(myquery)
    print(str(count))


if __name__ == '__main__':
    # search_id('CMN-085')
    #search_av_maker('Cine Magic', 20, 72)
    for i in range(1, 2):
        print(random.randint(0, 3) + 39)
