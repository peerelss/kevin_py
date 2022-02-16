import sys
import requests
import os
from bs4 import BeautifulSoup
import redis

file_x = 'result_1130.txt'


def get_pic_link_from_begin():
    for i in range(0, 10):
        url = 'https://reflectivedesire.com/photos/?sort=special-blend&page=' + str(i) + '&as-fragment=true'
        pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all('a', href=True)
        for p in pic_soup:
            href = p['href']
            if str(href).startswith('/photos/'):
                print(p['href'])
                get_pic_from_link('https://reflectivedesire.com' + p['href'])


def get_mp4_link_from_begin(url):
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all('a', href=True)
    for p in pic_soup:
        href = str(p['href'])
        if href.startswith('/videos/'):
            strs = href.split('/')
            #print(strs[2])
            print('https://4k.reflectivedesire.com/' + strs[2] + '.mp4')
            # get_pic_from_link('https://reflectivedesire.com' + p['href'])


def get_pic_from_link(url):
    print("photo url :" + url)
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all('img')
    for p in pic_soup:
        result_str = (str(p['src']).replace('small', 'xl'))
        print(result_str)


def get_mp4_from_link():
    pass


if __name__ == "__main__":
    # get_pic_link_from_begin()
    #get_mp4_link_from_begin('https://reflectivedesire.com/videos/categories/shorts/')
    get_mp4_link_from_begin('https://reflectivedesire.com/videos/categories/scenes/')
