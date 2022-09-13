# -*- coding: utf-8 -*-

'''
用来爬imdb的影片的数据，
对于影片，获取名字，封面，主演，系列，截图，发行公司，
'''
import os
from bs4 import BeautifulSoup
import requests

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
    for s in soup_jpg:
        src = str(s['src'])
        if src.endswith('webp'):
            print(src)


if __name__ == '__main__':
    get_imdb_movies('20470260')
