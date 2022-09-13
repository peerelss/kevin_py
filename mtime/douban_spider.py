# -*- coding: utf-8 -*-

'''
用来爬  豆瓣网  的影片的数据，
对于影片，获取名字，封面，主演，系列，截图，发行公司，
'''
import os
from bs4 import BeautifulSoup
import requests

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["av_db"]
mycol_douban = mydb['av_movies_douban_test']
cookies = {
    'bid': 'V6czckBkod8',
    'll': '108258',
    'viewed': '35456112',
    '__utmc': '30149280',
    'ap_v': '0,6.0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'bid=V6czckBkod8; ll=108258; viewed=35456112; __utmc=30149280; ap_v=0,6.0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

params = {
    'type': '11',
    'interval_id': '10:0',
    'action': '',
    'start': '0',
    'limit': '20',
}


def get_douban_movies(p):
    response = requests.get('https://movie.douban.com/j/chart/top_list', params=params, cookies=cookies,
                            headers=headers)
    movies = (response.json())
    mycol_douban.insert_many(movies)
    print(movies[0])


if __name__ == '__main__':
    for i in range(0, 44):
        params['start'] = str(20 * i)
        get_douban_movies(params)
