# -*- coding: utf-8 -*-

'''
用来爬imdb的影片的数据，
对于影片，获取名字，封面，主演，系列，截图，发行公司，
'''
import os
from bs4 import BeautifulSoup
import requests

import pymongo


class douban_item:
    def __init__(self, av_id, av_thumbs):
        self.av_id = av_id
        self.av_thumbs = av_thumbs


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["av_db"]
mycol_douban = mydb['av_movies_douban_test']
mycol_douban_jpg = mydb['av_movies_douban_jpgs_test']
cookies = {
    'bid': 'V6czckBkod8',
    'll': '108258',
    'viewed': '35456112',
    '__utmc': '30149280',
    'ap_v': '0,6.0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://movie.douban.com/subject/20470260/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
}


def get_imdb_movies(index):
    response = requests.get('https://movie.douban.com/subject/' + str(index) + '/all_photos', cookies=cookies,
                            headers=headers)
    # print(response.content)
    pic_content = BeautifulSoup(response.content, 'lxml')
    print(pic_content)
    soup_jpg = pic_content.find_all('img')
    jpgs = []
    for s in soup_jpg:
        src = str(s['src'])
        if src.endswith('webp'):
            jpgs.append(src)
    douban_item_ = douban_item(index, jpgs)
    # mycol_douban_jpg.insert_one(douban_item_.__dict__)
    print(douban_item_.__dict__)


def find_all_jpg():
    myquery = {}
    result_x = mycol_douban.find(myquery, {}).limit(30)
    for x in result_x:
        get_imdb_movies(x['id'])


def find_jpg_by_id(id):
    myquery = {'av_id': id}
    result_x = mycol_douban_jpg.find_one(myquery)
    print(result_x)


if __name__ == '__main__':
    myquery = {}
    result_x = mycol_douban.find(myquery, {}).limit(30)
    for x in result_x:
        find_jpg_by_id(x['id'])
