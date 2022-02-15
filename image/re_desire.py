import sys
import requests
import os
from bs4 import BeautifulSoup

index_url = 'https://reflectivedesire.com/videos/categories/scenes/'
de_url1 = 'https://reflectivedesire.com/photos/desert-varnish/'
file_x = 'result_1130.txt'


def find_jpg_doll(url):
    print("photo url :" + url)
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all('img')
    for p in pic_soup:
        result_str = (str(p['src']).replace('small', 'xl'))
        print(result_str)
        #f.write(result_str + '\n')


def find_jpg(de_url):
    print("photo index :" + de_url)
    pic_soup = BeautifulSoup(requests.get(de_url).content, "lxml").select('.responsive-image')
    for p in pic_soup:
        # print(p)
        if 'data-srcset' in str(p):
            r = str(p['data-srcset'])
            print(r[0:r.index('xl.jpg') + 6])


def find_jpg_index(url):
    pic_link = BeautifulSoup(requests.get(url).content, "lxml").find_all('a')
    for link in pic_link:
        link_str = str(link.get('href'))
        if 'videos' in link_str and 'sort=chrono' in link_str:
            print(link_str)
            find_jpg('https://reflectivedesire.com' + link_str)


def find_video_index(url):
    pic_link = BeautifulSoup(requests.get(url).content, "lxml").find_all('a')
    for link in pic_link:
        link_str = str(link.get('href'))
        if 'videos' in link_str:
            print(link_str)
        # find_jpg('https://reflectivedesire.com' + link_str)


'''从主页里拉去详细页的地址'''


def find_jpg_index_2(url_48):
    pic_link = BeautifulSoup(requests.get(url_48).content, "lxml").find_all('a')
    for link in pic_link:
        link_str = str(link.get('href'))
        if 'photos' in link_str:
            find_jpg_doll('https://reflectivedesire.com' + link_str)


# find_video_index(index_url)
find_jpg_doll('https://reflectivedesire.com/photos/red-filter/')
'''f = open(file_x, 'a')
for i in range(1, 9):
    index_str = str(i)
    url = 'https://reflectivedesire.com/photos/?sort=special-blend&page=INDEX&as-fragment=true'
    find_jpg_index_2(url.replace("INDEX", index_str))
f.close()'''
