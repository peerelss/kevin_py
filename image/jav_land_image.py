# -*- coding: utf-8 -*-
import sys
import requests
import os
from bs4 import BeautifulSoup


def get_jpg_list_from_url(url):
    print(url)
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all('a', href=True)
    for p in pic_soup:
        href = p['href']
        if str(href).startswith('/ja/movie'):
            # print(p['href'])
            get_jpg_url_from_url('https://jav.land' + p['href'])


def get_jpg_url_from_url(url):
    u = requests.get(url).content
    soup_jpg = BeautifulSoup(u, 'lxml').find_all('img')
    print(soup_jpg[0]['src'])


if __name__ == "__main__":
    for i in range(1, 61):
        get_jpg_list_from_url('https://jav.land/ja/maker/zlwjqp.html?page=' + str(61 - i))
