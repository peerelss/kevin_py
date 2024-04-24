import requests
from bs4 import BeautifulSoup
import time


def get_magnet_by_key(key_world, page):
    cookies = {
        'theme': '',
        'cf_clearance': '3A4M6TihyFF7yGuhYDU73unRTJZ.OL68HvHrI7NJZY4-1688622856-0-250',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://bt4gprx.com/search?q=harmony^%^20concepts^%^20&orderby=size&p=15',
        'Connection': 'keep-alive',
        # 'Cookie': 'theme=; cf_clearance=3A4M6TihyFF7yGuhYDU73unRTJZ.OL68HvHrI7NJZY4-1688622856-0-250',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'q': key_world,
        'orderby': 'size',
        'p': page,
    }

    response = requests.get('https://bt4gprx.com/search', params=params, cookies=cookies, headers=headers)
    return response.content


def get_href_from_url(content):
    soup = BeautifulSoup(content, 'html.parser')
    links = []

    # 查找所有的<a>标签
    for link in soup.find_all('a'):
        title = link.get('title')
        href = link.get('href')

        # 确保href存在
        if href and title:
            if 'magnet' in href:
                links.append({'title': title, 'href': href})
    print(len(links))
    return links


def get_magnet_from_href(href):
    cookies = {
        'theme': '',
        'cf_clearance': '3A4M6TihyFF7yGuhYDU73unRTJZ.OL68HvHrI7NJZY4-1688622856-0-250',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://bt4gprx.com/search?q=avs-museum&orderby=size&p=47',
        'Connection': 'keep-alive',
        # 'Cookie': 'theme=; cf_clearance=3A4M6TihyFF7yGuhYDU73unRTJZ.OL68HvHrI7NJZY4-1688622856-0-250',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    file_name = ''
    file_magnet = ""
    file_size = ''
    response = requests.get('https://bt4gprx.com' + href, cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.get_text(strip=True)
        if 'link' in text:
            links.append({'href': href, 'text': text})
            file_name = str(href).split('name=')[1]
           # print(file_name)
            file_magnet = str(href).replace('//downloadtorrentfile.com/hash/', 'magnet:?xt=urn:btih:')
    tbody = soup.find('tbody')
    if tbody:
        # 获取<tbody>内的所有<tr>
        rows = tbody.find_all('tr')
        if rows and len(rows) > 0:
            # 从第一个<tr>中获取所有<td>
            tds = rows[0].find_all('td')
            if tds and len(tds) >= 3:
                # 返回第三个<td>的文本内容
                file_size = (tds[2].text)
    result_100 = [file_name, file_magnet, file_size]
    return result_100


def write_links_to_file(links, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:  # 使用追加模式'a'
        for link in links:
            file.write(link + '\n')


def write_links_to_file_wuqian(links, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:  # 使用追加模式'a'
        for link in links:
            file.write(link + ',')
        file.write('\n')


def wuqian_magnet(key_world, page):
    cookies = {
        'aywcUid': 'f9bBYPN9U3_20240407154209',
        'aywcUid': 'WMOQETR3Om_20240407223227',
        'tet': '1713763956569',
        'tetm': 'E6452',
        'tcv': 'V2',
        'JSESSIONID': '46421D7F538D59527B95F63D1BCC07CD',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://wuqianun.top/search?keyword=bondagecafe',
        # 'Cookie': 'aywcUid=f9bBYPN9U3_20240407154209; aywcUid=WMOQETR3Om_20240407223227; tet=1713763956569; tetm=E6452; tcv=V2; JSESSIONID=46421D7F538D59527B95F63D1BCC07CD',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'keyword': key_world,
        'sos': 'relevance',
        'sofs': 'all',
        'sot': 'all',
        'soft': 'all',
        'som': 'exact',
        'p': page,
    }

    response = requests.get('https://wuqianun.top/search', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    # 查找所有的<a>标签
    for link in soup.find_all('a'):
        title = link.get('title')
        href = link.get('href')

        # 确保href存在
        if href and title:
            if 'detail' in href:
                links.append({'title': title, 'href': href})
    print(len(links))
    return links


def wuqian_get_magnet_from_href(href):
    cookies = {
        'aywcUid': 'f9bBYPN9U3_20240407154209',
        'aywcUid': 'WMOQETR3Om_20240407223227',
        'tet': '1713763956569',
        'tetm': 'E6452',
        'tcv': 'V2',
        'JSESSIONID': '46421D7F538D59527B95F63D1BCC07CD',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://wuqianun.top/search?keyword=bondagecafe&sos=relevance&sofs=all&sot=all&soft=all&som=exact&p=2',
        'Connection': 'keep-alive',
        # 'Cookie': 'aywcUid=f9bBYPN9U3_20240407154209; aywcUid=WMOQETR3Om_20240407223227; tet=1713763956569; tetm=E6452; tcv=V2; JSESSIONID=46421D7F538D59527B95F63D1BCC07CD',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }
    response = requests.get('https://wuqianun.top' + href, cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(href)
    title_tag = soup.find('title').text.replace(' - 磁力链接与种子下载', '')
    magnet_tag = ''
    size_tag = ''
    soup.find('title')
    tbody = soup.find('ul')
    if tbody:
        rows = tbody.find_all('li')
        if len(rows) == 4:
            magnet_tag = rows[3].text.replace("种子哈希：", 'magnet:?xt=urn:btih:')
            size_tag = rows[1].text.replace('文件大小：', "")
    return [title_tag, magnet_tag, size_tag]


if __name__ == "__main__":
    key_world = 'harmony concepts'
    for i in range(1, 10):
        result_2 = get_magnet_by_key(key_world, i)
        links = get_href_from_url(result_2)
        for link in links:
            result = get_magnet_from_href(link['href'])
            print(result[1])
            write_links_to_file_wuqian(result, key_world + '.txt')
