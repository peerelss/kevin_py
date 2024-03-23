import pymongo
import redis
import requests
from bs4 import BeautifulSoup
import re
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["t66y_av_rm"]
mycol = mydb['t66y_av_rm']


def get_magnet_by_page(url):
    cookies = {
        '227c9_lastvisit': '0^%^091695778407^%^09^%^2Fthread0806.php^%^3Ffid^%^3D28^%^26search^%^3D^%^26page^%^3D55',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.t66y.com/thread0806.php?fid=28&search=&page=3',
        'Connection': 'keep-alive',
        # 'Cookie': '227c9_lastvisit=0^%^091695778407^%^09^%^2Fthread0806.php^%^3Ffid^%^3D28^%^26search^%^3D^%^26page^%^3D55',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'If-Modified-Since': 'Sun, 24 Sep 2023 13:03:04 GMT',
        'If-None-Match': '328d-6061a764eddcd-gzip',
    }

    response = requests.get(url, cookies=cookies, headers=headers)
    html_content = response.text
    # print(html_content)
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取所有的链接和文字
    links = []
    title = soup.title.string
    print(title)
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.text.strip()
        links.append((text, href))

    # 打印链接和文字
    for text, href in links:
        if 'link.php?hash=' in str(href):
            print(href)
            if '=233' in str(href):
                print('magnet:?xt=urn:btih:' + str(href).split('=233')[1])


def href_and_text_by_page(page):
    print(page)
    cookies = {
        '227c9_lastvisit': '0^%^091695778407^%^09^%^2Fthread0806.php^%^3Ffid^%^3D28^%^26search^%^3D^%^26page^%^3D55',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.t66y.com/thread0806.php?fid=28&search=&page=2',
        # 'Cookie': '227c9_lastvisit=0^%^091695778407^%^09^%^2Fthread0806.php^%^3Ffid^%^3D28^%^26search^%^3D^%^26page^%^3D55',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }

    params = {
        'fid': '28',
        'search': '',
        'page': str(page),
    }

    response = requests.get('https://www.t66y.com/thread0806.php', params=params, cookies=cookies, headers=headers)
    html_content = response.text
    # print(html_content)
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取所有的链接和文字
    links = []

    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.text.strip()
        links.append((text, href))

    # 打印链接和文字
    for text, href in links:
        if 'htm_data' in str(href):
            # print(f'Text: {text}, Link: {href}')
            print(href)
            get_magnet_by_page('https://www.t66y.com/' + href)


def get_magnet_from_rmdown(hash):
    import requests

    cookies = {
        'PHPSESSID': '6aqri7278bae3pokb3g9v71dp7',
        'ses': 'df3b2e2cd295afc95c0863b389ce86fa',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',
        # 'Cookie': 'PHPSESSID=6aqri7278bae3pokb3g9v71dp7; ses=df3b2e2cd295afc95c0863b389ce86fa',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
    }

    params = {
        'hash': hash,
    }

    response = requests.get('https://www.rmdown.com/link.php', params=params, cookies=cookies, headers=headers)
    html_content = response.text
    match = re.search(r'Code: ([a-f0-9]+)', html_content)

    if match:
        code_value = match.group(1)
        print('magnet:?xt=urn:btih:' + code_value)
    else:
        print('未找到匹配的 Code 值')


# magnet:?xt=urn:btih:3c233f700f4339e4ab703c27d47efd0306f6d23d&dn=MDYD-797-U&tr=http://sukebei.tracker.wf:8888/announce&tr=udp://tracker.archlinux.org.theoks.net:6969/announce&tr=udp://tracker.openbittorrent.com:6969&tr=http://tracker.tasvideos.org:6969/announce&tr=udp://tracker.leech.ie:1337/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://tracker.coppersurfer.tk:6969/announce&tr=udp://tracker.internetwarriors.net:1337&tr=udp://tracker.internetwarriors.net:1337/announce&tr=udp://open.stealth.si:80/announce&tr=udp://9.rarbg.me:2710/announce&tr=udp://9.rarbg.me:2710&tr=http://anidex.moe:6969/announce&tr=http://freerainbowtables.com:6969/announce&tr=http://www.freerainbowtables.com:6969/announce&tr=udp://9.rarbg.com:2830/announce&tr=http://tracker2.itzmx.com:6961/announce&tr=http://tracker.etree.org:6969/announce&tr=http://www.thetradersden.org/forums/tracker:80/announce.php&tr=udp://udp-tracker.shittyurl.org:6969/announce&tr=https://tracker.shittyurl.org/announce&tr=http://tracker.shittyurl.org/announce&tr=udp://bt.firebit.org:2710/announce&tr=http://bt.firebit.org:2710/announce&tr=udp://exodus.desync.com:6969/announce&tr=udp://tracker.torrent.eu.org:451/announce&tr=http://sukebei.tracker.wf:8888/announce

if __name__ == '__main__':
    for i in range(1, 61 + 1):
        href_and_text_by_page(str(i))
    # get_magnet_from_rmdown()
