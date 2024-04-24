import sys
import requests
import os
from bs4 import BeautifulSoup
import redis
import time

file_str_list = []
url_resource = '/media/kevin/Backup/MP4/'


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
            # print(strs[2])
            if (strs[2] + '.mp4' in file_str_list):
                pass
            else:
                print('https://hd.reflectivedesire.com/' + strs[2] + '.mp4')
        # get_pic_from_link('https://reflectivedesire.com' + p['href'])


def get_pic_from_link(url):
    print("photo url :" + url)
    pic_soup = BeautifulSoup(requests.get(url).content, "lxml").find_all('img')
    for p in pic_soup:
        result_str = (str(p['src']).replace('small', 'xl'))
        print(result_str)


def get_mp4_from_link():
    pass


def get_photo_set_from_url(page):
    cookies = {
        'session8': 'eyJpZCI6IjA3MmZjMzkxNzhiM2MiLCJwYXNzcG9ydCI6eyJ1c2VyIjp7InRyaWFsIjpmYWxzZSwiZXRpY2tldGlkIjoiMjAyMDAwOjMyMzExIiwiZW1haWwiOiJ4aWVwZWVybGVzc0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6InhpZXBlZXJsZXNzQGdtYWlsLmNvbSIsImFjdGl2ZSI6dHJ1ZSwiZXhwaXJlZCI6ZmFsc2UsImNhbmNlbGxlZCI6ZmFsc2UsInN0YXR1cyI6MiwidHJhbnNndWlkIjoiM2FmYjI5NzEtMDNjOS00MTE0LWE5NWItYjE0ZjAxMDhiMDlhIiwiaXNBZG1pbiI6ZmFsc2V9fX0=',
        'session8.sig': 'R7_MII6iW_oCpC8cYdGBCHheKMI',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Alt-Used': 'reflectivedesire.com',
        'Connection': 'keep-alive',
        'Referer': 'https://reflectivedesire.com/photos/all/',
        # 'Cookie': 'session8=eyJpZCI6IjA3MmZjMzkxNzhiM2MiLCJwYXNzcG9ydCI6eyJ1c2VyIjp7InRyaWFsIjpmYWxzZSwiZXRpY2tldGlkIjoiMjAyMDAwOjMyMzExIiwiZW1haWwiOiJ4aWVwZWVybGVzc0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6InhpZXBlZXJsZXNzQGdtYWlsLmNvbSIsImFjdGl2ZSI6dHJ1ZSwiZXhwaXJlZCI6ZmFsc2UsImNhbmNlbGxlZCI6ZmFsc2UsInN0YXR1cyI6MiwidHJhbnNndWlkIjoiM2FmYjI5NzEtMDNjOS00MTE0LWE5NWItYjE0ZjAxMDhiMDlhIiwiaXNBZG1pbiI6ZmFsc2V9fX0=; session8.sig=R7_MII6iW_oCpC8cYdGBCHheKMI',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    params = {
        'sort': 'special-blend',
        'page': page,
    }

    response = requests.get('https://reflectivedesire.com/photos/', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    # 查找所有的<a>标签
    for link in soup.find_all('a'):
        title = link.get('title')
        href = link.get('href')
        links.append({'title': title, 'href': href})
    return links


if __name__ == "__main__":
    for i in range(0, 11):
        print(i)
        links = get_photo_set_from_url(i)
        for link in links:
            time.sleep(2)
            get_pic_from_link('https://reflectivedesire.com' + link['href'])
