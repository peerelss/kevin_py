from datetime import datetime

import requests
from bs4 import BeautifulSoup
import os

link_set = {}


def get_image_from_link(album_link):
    folder_path = str(album_link).split('/')[-1]
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    soup = BeautifulSoup(requests.get(album_link).text, "html.parser")
    links = soup.find_all("a")
    links_str = list(map(lambda x: str(x.get('href')), links))
    links_jpg = list(filter(lambda x: 'big.jpg' in x, links_str))
    for img_url in links_jpg:
        print(img_url)
        response = requests.get(img_url)
        img_name = img_url.split("/")[-1]
        img_path = os.path.join(folder_path, img_name)
        with open(img_path, "wb") as f:
            f.write(response.content)


def get_album_from_url():
    url = 'https://www.xvideos.com/amateur-channels/sexymuslima#_tabPhotos'

    # 解析 HTML
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    links = soup.find_all("a")
    list_1 = list(map(lambda x: 'https://www.xvideos.com' + str(x.get("href")), links))
    list_1_unique = list(set(list_1))
    list_filter = list(filter(lambda x: 'sexymuslima/photos' in x, list_1_unique))
    for li in list_filter:
        # get_image_from_link(li)
        print(li)


if __name__ == '__main__':
    get_image_from_link('https://www.xvideos.com/amateur-channels/sexymuslima/photos/7443261/large_hanches_de_musulmane')
