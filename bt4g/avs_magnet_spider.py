import requests
from bs4 import BeautifulSoup
import time
from juanzi import print_progress_bar
from image.sdk_every_thing_http import if_file_exist_with_size

cookies = {
    'existmag': 'mag',
    'starinfo': 'glyphicon^%^20glyphicon-plus',
    '4fJN_2132_ulastactivity': 'ce7ehrRkSv1dhxLb1H4AULx3geEYlXcGi9JwS2dbZOiibkQkpOtc',
    '4fJN_2132_auth': 'c86eNEVgbUfFuUm8uba8QRsf9nt3AGNzOM6AEKqn2bqipi^%^2B2vfy5EAkD7TzdFZReyDu8dy8CjJsO4sUB5cb83zw6Em0',
    '4fJN_2132_lastcheckfeed': '360788^%^7C1712523398',
    '4fJN_2132_nofavfid': '1',
    'dv': '1',
    '4fJN_2132_visitedfid': '2D36',
    '4fJN_2132_saltkey': 'xiBBVZGk',
    '4fJN_2132_lastvisit': '1714937377',
    '4fJN_2132_forum_lastvisit': 'D_2_1714941677D_36_1714942829',
    'PHPSESSID': 'fs6m69p7u0nkh24i2bou0pfd94',
    '4fJN_2132_st_t': '0^%^7C1714942829^%^7Ce63d7ba7c5be3326970bebfbd7797270',
    '4fJN_2132_home_diymode': '1',
    '4fJN_2132_seccodecSAfHzXCFY1W': '33649.aec41f6f4462d73c7a',
    '4fJN_2132_st_p': '0^%^7C1715136014^%^7Cab45fed048c5e2e1a25eedf2ffca2b47',
    '4fJN_2132_viewid': 'tid_136547',
    '4fJN_2132_seccodecSe66M04': '4590.8f6d9638130ea6aa17',
    '4fJN_2132_seccodecSS0E0vU': '14021.67b9051126fe9ff19c',
    '4fJN_2132_seccodecSn0GiA0': '54384.39bc15625c62e758ad',
    '4fJN_2132_lip': '47.153.82.31^%^2C1712813361',
    'bus_auth': 'cd0b7^%^2BQZENfAavhbLcSZt7Aa^%^2BDEGQCQxTyoLMMgVGPlLO0W6TQBOtZ7IQmI',
    '4fJN_2132_seccodecSAdw3uaiuLy': '2058.0c94c479f516006adb',
    '4fJN_2132_seccodecSAL97a2btdZ': '32216.f7ef2171d96b9a533b',
    '4fJN_2132_seccodecSARr7SkqEnK': '32559.3750609d5e1345401c',
    '4fJN_2132__refer': '^%^252Fforum^%^252Fhome.php^%^253Fmod^%^253Dspacecp^%^2526ac^%^253Dsearch^%^2526username^%^253Dbecks2002^%^2526searchsubmit^%^253Dyes',
    '4fJN_2132_seccodecSAMJ7CwFn2b': '33021.6b8079d6ffada97765',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.javbus.com/JUKD-846',
    'Connection': 'keep-alive',
    # 'Cookie': 'existmag=mag; starinfo=glyphicon^%^20glyphicon-plus; 4fJN_2132_ulastactivity=ce7ehrRkSv1dhxLb1H4AULx3geEYlXcGi9JwS2dbZOiibkQkpOtc; 4fJN_2132_auth=c86eNEVgbUfFuUm8uba8QRsf9nt3AGNzOM6AEKqn2bqipi^%^2B2vfy5EAkD7TzdFZReyDu8dy8CjJsO4sUB5cb83zw6Em0; 4fJN_2132_lastcheckfeed=360788^%^7C1712523398; 4fJN_2132_nofavfid=1; dv=1; 4fJN_2132_visitedfid=2D36; 4fJN_2132_saltkey=xiBBVZGk; 4fJN_2132_lastvisit=1714937377; 4fJN_2132_forum_lastvisit=D_2_1714941677D_36_1714942829; PHPSESSID=fs6m69p7u0nkh24i2bou0pfd94; 4fJN_2132_st_t=0^%^7C1714942829^%^7Ce63d7ba7c5be3326970bebfbd7797270; 4fJN_2132_home_diymode=1; 4fJN_2132_seccodecSAfHzXCFY1W=33649.aec41f6f4462d73c7a; 4fJN_2132_st_p=0^%^7C1715136014^%^7Cab45fed048c5e2e1a25eedf2ffca2b47; 4fJN_2132_viewid=tid_136547; 4fJN_2132_seccodecSe66M04=4590.8f6d9638130ea6aa17; 4fJN_2132_seccodecSS0E0vU=14021.67b9051126fe9ff19c; 4fJN_2132_seccodecSn0GiA0=54384.39bc15625c62e758ad; 4fJN_2132_lip=47.153.82.31^%^2C1712813361; bus_auth=cd0b7^%^2BQZENfAavhbLcSZt7Aa^%^2BDEGQCQxTyoLMMgVGPlLO0W6TQBOtZ7IQmI; 4fJN_2132_seccodecSAdw3uaiuLy=2058.0c94c479f516006adb; 4fJN_2132_seccodecSAL97a2btdZ=32216.f7ef2171d96b9a533b; 4fJN_2132_seccodecSARr7SkqEnK=32559.3750609d5e1345401c; 4fJN_2132__refer=^%^252Fforum^%^252Fhome.php^%^253Fmod^%^253Dspacecp^%^2526ac^%^253Dsearch^%^2526username^%^253Dbecks2002^%^2526searchsubmit^%^253Dyes; 4fJN_2132_seccodecSAMJ7CwFn2b=33021.6b8079d6ffada97765',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}
import time
import re


def get_script(av_id):
    # Fetch the webpage
    id = str(av_id).replace('\n', '').replace(' ', '-'),
    if len(str(av_id)) > 5:
        print(id)
        response = requests.get('https://www.javbus.com/' + id[0], cookies=cookies,
                                headers=headers)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract <script> tags
        script_tags = soup.find_all('script')
        if len(soup.find_all(class_='star-name')) <= 3:
            for script in script_tags:
                if script.string is not None and 'var gid' in script.string:  # This checks if the script tag contains anything
                    values_69 = re.findall(r'=\s*([^;]+);', script.string)
                    print(values_69)
                    return values_69
        else:
            print('人太多')


def get_magnet_by_gid(value):
    if len(value) > 2:
        time.sleep(1)
        response = requests.get(
            'https://www.javbus.com/ajax/uncledatoolsbyajax.php?gid=' + value[0] + '&lang=zh&img=' + value[
                2] + '&uc=0&floor=969',
            cookies=cookies,
            headers=headers,
        )
        html_content = response.content
        # Parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        script_tags = soup.find_all('a', href=True)
        magnet_length = int(len(script_tags) / 3)
        if magnet_length > 0:
            for i in range(0, magnet_length):
                print(script_tags[i * 3 + 1]['href'])
                print(script_tags[i * 3 + 1].text)
            with open('magnet_av_id0510.txt', 'a', encoding='utf-8') as file:  # 使用追加模式'a'
                file.write(script_tags[0]['href'] + '\n')
                file.write(script_tags[0].text + '\n')


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


def k_test():
    readlines = open(r'C:\Users\kevin\PycharmProjects\kevin_py\image\風間ゆみ.txt').readlines()
    for line in readlines:
        if len(line) > 5:
            print_progress_bar(readlines.index(line) + 1, len(readlines), prefix='Progress:',
                               suffix='Complete ',
                               length=100)
            key_world = (str(line).split('_')[0])
            print(key_world)
            content = get_magnet_by_key(key_world, 1)
            ref_soup = BeautifulSoup(content, "lxml").find_all(class_='lightColor')
            if len(ref_soup) >= 1:
                if ref_soup[0].text.endswith('GB') or ref_soup[0].text.endswith('MB'):
                    print(line)
                    with open('風間ゆみ_id.txt', 'a', encoding='utf-8') as file:  # 使用追加模式'a'
                        file.write(line + '\n')


def get_id():
    read_lines = open(r'C:\Users\kevin\Documents\av_id_hd.txt', 'r', encoding='utf-8').readlines()
    for line in read_lines:
        if len(line) > 5 and 'VR' not in line:
            if not if_file_exist_with_size(line, 700):
                time.sleep(3)
                content = get_magnet_by_key(str(line), 1)
                ref_soup = BeautifulSoup(content, "lxml").find_all(class_='lightColor')
                if len(ref_soup) >= 1:
                    if ref_soup[0].text.endswith('GB') or ref_soup[0].text.endswith('MB'):
                        # print(line)
                        values = get_script(str(line))
                        if values:
                            get_magnet_by_gid(values)


def get_magnet_by_id(av_id):
    time.sleep(3)
    response = requests.get('https://www.javbus.com/' + av_id, cookies=cookies,
                            headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract <script> tags
    script_tags = soup.find_all('script')

    for script in script_tags:
        if script.string is not None and 'var gid' in script.string:  # This checks if the script tag contains anything
            values_69 = re.findall(r'=\s*([^;]+);', script.string)
            print(values_69)
            if values_69:
                get_magnet_by_gid(values_69)


if __name__ == "__main__":
    for i in range(1, 1000):
        id_str = ''
        if i < 10:
            id_str = '00' + str(i)
        elif i < 100:
            id_str = '0' + str(i)
        else:
            id_str = str(i)
        key_world = 'juc-' + id_str
        if not if_file_exist_with_size(key_world, 300):
            get_magnet_by_id('juc-' + id_str)
