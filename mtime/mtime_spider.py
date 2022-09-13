# -*- coding: utf-8 -*-

'''
用来爬时光网的影片的数据，
对于影片，获取名字，封面，主演，系列，截图，发行公司，
'''
import os
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://film.mtime.com',
    'Connection': 'keep-alive',
    'Referer': 'http://film.mtime.com/search/movies/movies?type=area&word=%E4%B8%AD%E5%9B%BD%E9%A6%99%E6%B8%AF',
}


def get_mtime_movie_by_page(index):
    data = 'keyword=&pageIndex=' + str(index) + '&pageSize=20&searchType=0&locationId=290&genreTypes=&area=中国香港&year='
    response = requests.post('http://front-gateway.mtime.com/mtime-search/search/unionSearch2', headers=headers,
                             data=data.encode('utf-8'))
    movies = (response.json()['data']['movies'])
    print(movies[0])


if __name__ == '__main__':
    get_mtime_movie_by_page(1)
