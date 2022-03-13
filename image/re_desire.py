# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import time


import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://tumblrgallery.xyz/tumblrblog/gallery/166593/2.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
}

params = (
    ('page', '1'),
    ('action', 'blog_gallery'),
    ('id', '166593'),
)



def get_pic_url_from_url(data):
    print(data['last'] + "   " + str(data['scroll']))
    response = requests.get('https://tumblrgallery.xyz/ajax.php', headers=headers, params=params)
    soup_jpg = BeautifulSoup(response.content, 'lxml').find_all('img')
    f = open('/media/kevin/Backup/bdsmlr/' + 'charlotte-ava22'.replace('-', '_') + '__bdsmlr.txt', 'a')
    f.write(data['last'] + " " + str(data['scroll']) + '\n')
    for s in soup_jpg:
        if 'avatar' in str(s['src']):
            pass
        else:
            f.write(s['src'] + '\n')
            print(s['src'])
    f.close()
    soup = BeautifulSoup(response.content, 'lxml').find_all("div", {"class": "countinf"})
    if len(soup) > 0:
        data['page'] = int(data['scroll']) + 1
        data['last'] = soup[-1]['data-id']
        return True
    else:
        return False


def get_next_page_from_url():
    pass


if __name__ == "__main__":
    while get_pic_url_from_url(params):
        pass
