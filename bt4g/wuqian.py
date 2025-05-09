import time

import requests
from bs4 import BeautifulSoup

cookies = {
    'JSESSIONID': '4C17632D5941ECA7E6E5266C864E3E3D',
    'aywcUid': '2TmHTTIKTc_20250508085320',
    'fct': 'dHYyfFY0fDJUbUhUVElLVGNfMjAyNTA1MDgwODUzMjB8MTc0NjcxNjAwMDY2NnxDN0Y3OA==',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    'Referer': 'https://wuqianso.top/search?keyword=artofgloss&sos=length&sofs=all&sot=all&soft=all&som=auto&p=24',
    # 'Cookie': 'JSESSIONID=4C17632D5941ECA7E6E5266C864E3E3D; aywcUid=2TmHTTIKTc_20250508085320; fct=dHYyfFY0fDJUbUhUVElLVGNfMjAyNTA1MDgwODUzMjB8MTc0NjcxNjAwMDY2NnxDN0Y3OA==',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}


def get_link_by_page_and_key(keyworld, page):
    params = {
        'keyword': keyworld,
        'sos': 'length',
        'sofs': 'all',
        'sot': 'all',
        'soft': 'all',
        'som': 'auto',
        'p': page,
    }

    response = requests.get('https://wuqianso.top/search', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    hrefs = []

    for a_tag in soup.find_all('a', href=True):
        if 'detail' in a_tag['href']:
            hrefs.append(a_tag['href'])

    return hrefs


def get_magnet_by_link(url):
    response = requests.get(url, cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    hrefs = []

    for a_tag in soup.find_all('a', href=True):
        if 'magnet' in a_tag['href']:
            hrefs.append(a_tag['href'])
    for h in hrefs:
        print(h)


def get_all_magnet():
    for i in range(1, 25):
        print(str(i))
        magnet_href = get_link_by_page_and_key("artofgloss", str(i))
        for m in magnet_href:
            url_l = 'https://wuqianso.top' + m
            get_magnet_by_link(url_l)
        time.sleep(4)


if __name__ == "__main__":
    get_all_magnet()
