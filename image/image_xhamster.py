# -*- coding: utf-8 -*-
import json
import sys
import requests
import os
from bs4 import BeautifulSoup
import pymongo
import redis
from urllib.parse import urljoin

url = 'https://xhamster.com/photos/gallery/sissy-gifs-i-like-11371035'


def get_image_from_image_url(url):
    pass


def get_images_from_url(url):
    # print(url)
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all(class_='photo-container')
    for p in pic_soup:
        href = p['href']
        if 'gallery' in href:
            get_image_from_image_url(href)


if __name__ == '__main__':
    get_images_from_url(url)
