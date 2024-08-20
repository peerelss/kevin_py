import os.path
import time
import requests
from bs4 import BeautifulSoup
from image.sdk_every_thing_http import if_file_exist_with_size
from bt4g.juanzi import print_progress_bar
import requests

cookies = {
    'existmag': 'all',
    'starinfo': 'glyphicon^%^20glyphicon-plus',
    '4fJN_2132_ulastactivity': 'ce7ehrRkSv1dhxLb1H4AULx3geEYlXcGi9JwS2dbZOiibkQkpOtc',
    '4fJN_2132_auth': 'c86eNEVgbUfFuUm8uba8QRsf9nt3AGNzOM6AEKqn2bqipi^%^2B2vfy5EAkD7TzdFZReyDu8dy8CjJsO4sUB5cb83zw6Em0',
    '4fJN_2132_lastcheckfeed': '360788^%^7C1712523398',
    '4fJN_2132_nofavfid': '1',
    'dv': '1',
    '4fJN_2132_visitedfid': '36D2',
    '4fJN_2132_saltkey': 'KsQ0La8i',
    '4fJN_2132_lastvisit': '1712274955',
    'PHPSESSID': 'fs6m69p7u0nkh24i2bou0pfd94',
    '4fJN_2132_st_t': '0^%^7C1712522614^%^7C77143bfb9ee2fd87952d093ed5c68cb8',
    '4fJN_2132_home_diymode': '1',
    '4fJN_2132_seccodecSAfHzXCFY1W': '33649.aec41f6f4462d73c7a',
    '4fJN_2132_st_p': '360788^%^7C1714547485^%^7C2e8bc3a17fc46cecbec094480006a211',
    '4fJN_2132_viewid': 'tid_133058',
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
    'Referer': 'https://www.javbus.com/PPPD-568',
    'Connection': 'keep-alive',
    # 'Cookie': 'existmag=all; starinfo=glyphicon^%^20glyphicon-plus; 4fJN_2132_ulastactivity=ce7ehrRkSv1dhxLb1H4AULx3geEYlXcGi9JwS2dbZOiibkQkpOtc; 4fJN_2132_auth=c86eNEVgbUfFuUm8uba8QRsf9nt3AGNzOM6AEKqn2bqipi^%^2B2vfy5EAkD7TzdFZReyDu8dy8CjJsO4sUB5cb83zw6Em0; 4fJN_2132_lastcheckfeed=360788^%^7C1712523398; 4fJN_2132_nofavfid=1; dv=1; 4fJN_2132_visitedfid=36D2; 4fJN_2132_saltkey=KsQ0La8i; 4fJN_2132_lastvisit=1712274955; PHPSESSID=fs6m69p7u0nkh24i2bou0pfd94; 4fJN_2132_st_t=0^%^7C1712522614^%^7C77143bfb9ee2fd87952d093ed5c68cb8; 4fJN_2132_home_diymode=1; 4fJN_2132_seccodecSAfHzXCFY1W=33649.aec41f6f4462d73c7a; 4fJN_2132_st_p=360788^%^7C1714547485^%^7C2e8bc3a17fc46cecbec094480006a211; 4fJN_2132_viewid=tid_133058; 4fJN_2132_seccodecSe66M04=4590.8f6d9638130ea6aa17; 4fJN_2132_seccodecSS0E0vU=14021.67b9051126fe9ff19c; 4fJN_2132_seccodecSn0GiA0=54384.39bc15625c62e758ad; 4fJN_2132_lip=47.153.82.31^%^2C1712813361; bus_auth=cd0b7^%^2BQZENfAavhbLcSZt7Aa^%^2BDEGQCQxTyoLMMgVGPlLO0W6TQBOtZ7IQmI; 4fJN_2132_seccodecSAdw3uaiuLy=2058.0c94c479f516006adb; 4fJN_2132_seccodecSAL97a2btdZ=32216.f7ef2171d96b9a533b; 4fJN_2132_seccodecSARr7SkqEnK=32559.3750609d5e1345401c; 4fJN_2132__refer=^%^252Fforum^%^252Fhome.php^%^253Fmod^%^253Dspacecp^%^2526ac^%^253Dsearch^%^2526username^%^253Dbecks2002^%^2526searchsubmit^%^253Dyes; 4fJN_2132_seccodecSAMJ7CwFn2b=33021.6b8079d6ffada97765',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


def find_stars(av_url):
    response = requests.get(av_url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    href_soup = soup.find_all(class_='star-box')
    return len(href_soup) <= 3


def get_response_from_page(page_url):
    print(page_url)
    response = requests.get(page_url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    href_soup = soup.find_all(class_='movie-box')
    for h in href_soup:
        if '高清' in h.text:
            av_id = (str(h['href']).split('/')[-1]).replace("-", ' ')
            if not if_file_exist_with_size(av_id, 3000) and find_stars(h['href']):
                print(av_id)
                with open('av_id_hd.txt', 'a', encoding='utf-8') as file:  # 使用追加模式'a'
                    file.write(av_id + '\n')


dir = r'F:\after\image\アイデアポケット\\' + ''


def find_image_url_from_href(href):
    cookies = {
        'existmag': 'all',
        'starinfo': 'glyphicon^%^20glyphicon-plus',
        '4fJN_2132_ulastactivity': 'd125rizbgt88p4h4AOp^%^2BNc6E^%^2Fqh8zvyy701Ie68XPPKrskB81xNG',
        '4fJN_2132_auth': 'c86eNEVgbUfFuUm8uba8QRsf9nt3AGNzOM6AEKqn2bqipi^%^2B2vfy5EAkD7TzdFZReyDu8dy8CjJsO4sUB5cb83zw6Em0',
        '4fJN_2132_lastcheckfeed': '360788^%^7C1712523398',
        '4fJN_2132_nofavfid': '1',
        'dv': '1',
        '4fJN_2132_visitedfid': '2D36',
        '4fJN_2132_saltkey': 'KsQ0La8i',
        '4fJN_2132_lastvisit': '1712274955',
        'PHPSESSID': 'fs6m69p7u0nkh24i2bou0pfd94',
        '4fJN_2132_st_t': '0^%^7C1712522614^%^7C77143bfb9ee2fd87952d093ed5c68cb8',
        '4fJN_2132_home_diymode': '1',
        '4fJN_2132_seccodecSAfHzXCFY1W': '33649.aec41f6f4462d73c7a',
        '4fJN_2132_st_p': '360788^%^7C1712813995^%^7Cc21bf0d00943b7859f1b6539c20e9f34',
        '4fJN_2132_viewid': 'tid_121781',
        '4fJN_2132_seccodecSe66M04': '4590.8f6d9638130ea6aa17',
        '4fJN_2132_seccodecSS0E0vU': '14021.67b9051126fe9ff19c',
        '4fJN_2132_seccodecSn0GiA0': '54384.39bc15625c62e758ad',
        '4fJN_2132_lip': '47.153.82.31^%^2C1712554989',
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
        'Referer': 'https://www.javbus.com/series/one',
        'Connection': 'keep-alive',
        # 'Cookie': 'existmag=all; starinfo=glyphicon^%^20glyphicon-plus; 4fJN_2132_ulastactivity=d125rizbgt88p4h4AOp^%^2BNc6E^%^2Fqh8zvyy701Ie68XPPKrskB81xNG; 4fJN_2132_auth=c86eNEVgbUfFuUm8uba8QRsf9nt3AGNzOM6AEKqn2bqipi^%^2B2vfy5EAkD7TzdFZReyDu8dy8CjJsO4sUB5cb83zw6Em0; 4fJN_2132_lastcheckfeed=360788^%^7C1712523398; 4fJN_2132_nofavfid=1; dv=1; 4fJN_2132_visitedfid=2D36; 4fJN_2132_saltkey=KsQ0La8i; 4fJN_2132_lastvisit=1712274955; PHPSESSID=fs6m69p7u0nkh24i2bou0pfd94; 4fJN_2132_st_t=0^%^7C1712522614^%^7C77143bfb9ee2fd87952d093ed5c68cb8; 4fJN_2132_home_diymode=1; 4fJN_2132_seccodecSAfHzXCFY1W=33649.aec41f6f4462d73c7a; 4fJN_2132_st_p=360788^%^7C1712813995^%^7Cc21bf0d00943b7859f1b6539c20e9f34; 4fJN_2132_viewid=tid_121781; 4fJN_2132_seccodecSe66M04=4590.8f6d9638130ea6aa17; 4fJN_2132_seccodecSS0E0vU=14021.67b9051126fe9ff19c; 4fJN_2132_seccodecSn0GiA0=54384.39bc15625c62e758ad; 4fJN_2132_lip=47.153.82.31^%^2C1712554989; bus_auth=cd0b7^%^2BQZENfAavhbLcSZt7Aa^%^2BDEGQCQxTyoLMMgVGPlLO0W6TQBOtZ7IQmI; 4fJN_2132_seccodecSAdw3uaiuLy=2058.0c94c479f516006adb; 4fJN_2132_seccodecSAL97a2btdZ=32216.f7ef2171d96b9a533b; 4fJN_2132_seccodecSARr7SkqEnK=32559.3750609d5e1345401c; 4fJN_2132__refer=^%^252Fforum^%^252Fhome.php^%^253Fmod^%^253Dspacecp^%^2526ac^%^253Dsearch^%^2526username^%^253Dbecks2002^%^2526searchsubmit^%^253Dyes; 4fJN_2132_seccodecSAMJ7CwFn2b=33021.6b8079d6ffada97765',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }
    print(href)
    file_name = dir + str(href).split('/')[-1] + '.jpg'
    if os.path.exists(file_name):
        print(file_name + ' exist')
    else:
        soup = BeautifulSoup(requests.get(href, cookies=cookies, headers=headers).content,
                             "lxml")
        class_soup = soup.find_all(class_='bigImage')
        if len(class_soup) > 0:
            av_jpg = 'https://www.javbus.com' + class_soup[0]['href']
            print(av_jpg)
            try:
                html = requests.get(av_jpg).content
                print(file_name)
                with open(file_name, "wb") as file:
                    file.write(html)
            except Exception as e:
                print(av_jpg + str(e))


def download_factory_image():
    list_factory = [
        {'url': 'mz', 'len': 487, 'name': 'gas'}
    ]
    for star in list_factory:
        movie_account = star['len']
        for i in range(1, int(movie_account / 30) + 2):
            url = 'https://www.javbus.com/studio/' + star['url'] + '/' + str(i)
            print(url)
            response = requests.get(url, cookies=cookies, headers=headers)
            soup = BeautifulSoup(response.content, "lxml")
            href_soup = soup.find_all(class_='movie-box')
            for href in href_soup:
                find_image_url_from_href(href['href'])
                time.sleep(1)


def get_star():
    list_star = [
        {'url': '2de', 'len': 1372, 'name': 'JULIA '}
    ]
    list_factory = [
        {'url': 'mz', 'len': 487, 'name': 'gas'}
    ]
    for star in list_star:
        with open('av_id_hd.txt', 'a', encoding='utf-8') as file:  # 使用追加模式'a'
            file.write(star['name'] + '\n')
        movie_account = star['len']
        url = 'https://www.javbus.com/star/' + star['url'] + '/'
        for i in range(1, int(movie_account / 30) + 2):
            get_response_from_page(url + str(i))
            print_progress_bar(i, int(movie_account / 30) + 1, prefix='Progress:',
                               suffix='Complete ',
                               length=100)


if __name__ == "__main__":
    for i in range(1, 1000):
        if i <10:
            if not if_file_exist_with_size("jukd 00" + str(i),200):
                print('jukd 00' + str(i))
        elif i <100:
            if not if_file_exist_with_size("jukd 0" + str(i),200):
                print('jukd 0' + str(i))
        else:
            if not if_file_exist_with_size("jukd "+str(i),200):
                print('jukd '+str(i))
