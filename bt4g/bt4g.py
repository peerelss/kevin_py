import requests
from bs4 import BeautifulSoup
import os
import pymongo
import libtorrent as lt

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']


def get_album_from_url(keyword, page):
    cookies = {
        'cf_clearance': '.ML4447EfyJB3iYRV57wjd061wnL_ax5qfRo_1Mg0Wo-1679966816-0-150',
        'theme': '',
        'cf_chl_2': 'e9cb53eeb8ed8d6',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://bt4g.org/search/BondageCafe/40',
        # 'Cookie': 'cf_clearance=.ML4447EfyJB3iYRV57wjd061wnL_ax5qfRo_1Mg0Wo-1679966816-0-150; theme=; cf_chl_2=e9cb53eeb8ed8d6',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }
    response = requests.get('https://bt4g.org/search/' + keyword + '/' + str(page), cookies=cookies, headers=headers)
    # 解析 HTML
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if 'magnet' in str(href):
            text = link.text.strip()
            links.append({'href': href, 'text': text, 'keyword': keyword})
    if len(links) > 0:
        collection.insert_many(links)
        for l in links:
            print(l)
    else:
        print('end')


def get_size_from_magnet():
    # 创建一个session对象
    session = lt.session()

    # 添加一个tracker服务器
    session.add_dht_router("router.bittorrent.com", 6881)

    # 创建一个torrent_info对象
    params = {"save_path": ".", "storage_mode": lt.storage_mode_t.storage_mode_sparse}
    torrent_info = lt.torrent_info("magnet:?xt=urn:btih:64f644f11ffc60744cd6b74724198d33f0360f8b&dn=Andrew_Blake_Collection&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=https%3A%2F%2Fopentracker.i2p.rocks%3A443%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2F9.rarbg.com%3A2810%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.com%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=https%3A%2F%2Ftracker.tamersunion.org%3A443%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.moeking.me%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker1.bt.moack.co.kr%3A80%2Fannounce&tr=udp%3A%2F%2Fmovies.zsw.ca%3A6969%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=http%3A%2F%2Fopen.acgnxtracker.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.bitsearch.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.altrosky.nl%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker-udp.gbitt.info%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.bt4g.com%3A2095%2Fannounce",
                                   params)

    # 获取torrent_info对象中的文件信息列表
    file_list = torrent_info.files()

    # 获取第一个文件的大小
    file_size = file_list[0].size

    print("文件大小为：", file_size, "字节")


if __name__ == '__main__':
    # for i in range(1, int(734 / 15) + 2):
    #    get_album_from_url('andrew blake', i)
    get_size_from_magnet()
