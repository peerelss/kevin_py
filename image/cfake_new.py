# -*- coding: utf-8 -*-
import sys
import requests
import os
from bs4 import BeautifulSoup

is_end = False

file_target = '/media/kevin/Backup/cfake/'
file_resource = "/media/kevin/Backup/cfake/cfake_url_list.txt"


def init_cfake_url(url):
    index = 0
    while get_jpg_url_from_url(url + '/p' + str(index)):
        index = index + 30


def get_jpg_url_from_url(url):
    print(url)
    u = requests.get(url).content
    soup_jpg = BeautifulSoup(u, 'lxml').find_all('img')
    for s in soup_jpg:
        src = str(s['src'])
        if 'thumbs' in src:
            urls = 'http://cfake.com/' + src.replace('thumbs', 'photos')
            print(urls)
    soup = BeautifulSoup(u, 'lxml').find_all("div", {"class": "thumb_show"})
    return len(soup) == 30


def init_list(file_name):
    a_file = open(file_name, "r")
    print(file_name)
    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        if stripped_line:
            list_of_lists.append(stripped_line)
    a_file.close()
    return list_of_lists


if __name__ == "__main__":
    # file_name_txt = (get_file_name_from_url('http://cfake.com/picture/Facial/25/3/p'))
    for i in range(0, 7):
        get_jpg_url_from_url('https://cfake.com/images/categories/Bukkake/107/3/p' + str(i))
