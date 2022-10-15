import os.path

import requests
from bs4 import BeautifulSoup
import pymongo
import redis

cookies = {
    'LW_lang': 'uk',
    'pjAcceptCookie': 'YES',
    'VerotelUser': 'peerelss',
    'VerotelPass': 'Peerless123',
    'VerotelChecked': 'checked',
    'windowWidth': '1398',
    'windowHeight': '712',
    'PHPSESSID': '6635529e5f4b61392140a98911af36b9',
    'VerotelLoggedin': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://legsworld.net/CSS_Version/start.php?update=6794&lang=de&direct=',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'LW_lang=uk; pjAcceptCookie=YES; VerotelUser=peerelss; VerotelPass=Peerless123; VerotelChecked=checked; windowWidth=1398; windowHeight=712; PHPSESSID=6635529e5f4b61392140a98911af36b9; VerotelLoggedin=1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'serno': '6794',
    'lang': 'de',
    'speed': '3',
    'direct': '',
}


def get_img_from_index(index):
    params['serno'] = str(index)
    response = requests.get('https://legsworld.net/CSS_Version/MyGallery.php', params=params, cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(response.content, "lxml")

    a_soup = soup.find_all('a', href=True)
    for a in a_soup:
        find_jpg_from_url('https://legsworld.net/CSS_Version/' + a['href'])


def find_jpg_from_url(url):
    response = requests.get(url, params=params, cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    tag = soup.find_all('img')
    for t in tag:
        ts = str(t['src']).replace('..', "")
        if 'Updates' in ts:
            if 'Thumbs' in ts:
                pass
            else:
                download_img_from_url('https://legsworld.net' + ts)


# https://legsworld.net/Members/Updates/6794/2013-08591.jpg?1660131733

def download_img_from_url(url):
    s_url = str(url)
    if 'jpg' in s_url:
        print(s_url)
        dir_ = r'C:\Users\kevin\legsworld\\' + s_url.split('/')[5] + '\\'
        if os.path.exists(dir_):
            pass
        else:
            os.mkdir(dir_)
        if 'Thumbs' in url:
            pass
        else:
            response = requests.get(url, params=params, cookies=cookies,
                                    headers=headers)
            str_jpg = dir_ + s_url[s_url.rfind('/'): s_url.index('jpg') + 3]
            if os.path.exists(str_jpg):
                pass
            else:
                with open(dir_ + s_url[s_url.rfind('/'): s_url.index('jpg') + 3], "wb") as file:
                    file.write(response.content)


if __name__ == '__main__':
    for i in reversed(range(6813, 6826)):
        get_img_from_index(i)
    # download_img_from_url('https://legsworld.net/Members/Updates/6794/2013-08591.jpg?1660131733')
    # find_jpg_from_url('https://legsworld.net/CSS_Version/MyGalleryDisplay.php?serno=6794&lang=de&pic=14&FreeUpdate=')
