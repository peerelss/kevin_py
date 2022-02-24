# -*- coding: UTF8 -*-
import sys
import requests
import os
from bs4 import BeautifulSoup


def get_cate_from_url():
    pass


def get_every_movie_from_series(url):
    url = 'https://www.dorcelvision.com/en/series/luxury'
    print(url)
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all(class_="movies")
    for p in pic_soup:
        href = p['href']
        if str(href).startswith('/en/movies/'):
            print(p['href'])
            # get_every_movie_from_series('https://www.dorcelvision.com' + p['href'])


def get_series_from_url(url):
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all(class_="movies")
    for p in pic_soup:
        href = p['href']
        if str(href).startswith('/en/series/'):
            print(p['href'])
        #  get_every_movie_from_series('https://www.dorcelvision.com' + p['href'])


if __name__ == "__main__":
    get_every_movie_from_series('https://www.dorcelvision.com/en/series/')
