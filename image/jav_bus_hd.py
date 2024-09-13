import os.path
import time
from bs4 import BeautifulSoup
from image.sdk_every_thing_http import if_file_exist_with_size
from bt4g.juanzi import print_progress_bar
import requests

cookies = {
    'existmag': 'all',
    'starinfo': 'glyphicon^%^20glyphicon-plus',
    '4fJN_2132_ulastactivity': 'be1abgGNbN^%^2B^%^2FsZdspwvm2^%^2BGexcVVVTiY^%^2BRkYdONGqgyPofgiW6KI',
    '4fJN_2132_auth': 'fa1advZoxV0HKIY511Na2A14UuVPkEGextzkNEf3LTmYZNsVPWnPfpvE53q91E0HtOyeOzFvIoDUgoM0BFfdfgLImuY',
    '4fJN_2132_lastcheckfeed': '360788^%^7C1720277707',
    '4fJN_2132_nofavfid': '1',
    'dv': '1',
    '4fJN_2132_visitedfid': '36D2D37',
    '4fJN_2132_saltkey': 'gfT2Y2T6',
    '4fJN_2132_lastvisit': '1722823124',
    '4fJN_2132_forum_lastvisit': 'D_2_1724517854D_36_1724525009',
    'PHPSESSID': 'fs6m69p7u0nkh24i2bou0pfd94',
    '4fJN_2132_st_t': '0^%^7C1724525009^%^7C4464e74bf651602a334b6e1693abf1a0',
    '4fJN_2132_home_diymode': '1',
    '4fJN_2132_seccodecSAfHzXCFY1W': '33649.aec41f6f4462d73c7a',
    '4fJN_2132_st_p': '0^%^7C1724524948^%^7C28c512a60741f151a2f2f3ac21e00a93',
    '4fJN_2132_viewid': 'tid_140950',
    '4fJN_2132_seccodecSe66M04': '4590.8f6d9638130ea6aa17',
    '4fJN_2132_seccodecSS0E0vU': '14021.67b9051126fe9ff19c',
    '4fJN_2132_seccodecSn0GiA0': '54384.39bc15625c62e758ad',
    '4fJN_2132_lip': '98.97.91.9^%^2C1722643381',
    'bus_auth': '1edafav4s3jAboxGlFgPe3ukZ^%^2F3UF0ndKEyDvg4qd^%^2B^%^2Bfwd447jVKwwzeys8',
    '4fJN_2132_seccodecSAdw3uaiuLy': '2058.0c94c479f516006adb',
    '4fJN_2132_seccodecSAL97a2btdZ': '32216.f7ef2171d96b9a533b',
    '4fJN_2132_seccodecSARr7SkqEnK': '32559.3750609d5e1345401c',
    '4fJN_2132__refer': '^%^252Fforum^%^252Fhome.php^%^253Fmod^%^253Dspacecp^%^2526ac^%^253Dsearch^%^2526username^%^253Dbecks2002^%^2526searchsubmit^%^253Dyes',
    '4fJN_2132_seccodecSAMJ7CwFn2b': '33021.6b8079d6ffada97765',
    '4fJN_2132_seccodecSAQxRkynn6i': '1951.cdafb31f3eea26a7f3',
    '4fJN_2132_seccodecSAMAQppbbt7': '16808.02c2f2ff5f6f4dd39a',
    '4fJN_2132_seccodecSAZ25aiRGU4': '23836.e064403d105d18bcc5',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    'Referer': 'https://www.javbus.com/star/300',
    # 'Cookie': 'existmag=all; starinfo=glyphicon^%^20glyphicon-plus; 4fJN_2132_ulastactivity=be1abgGNbN^%^2B^%^2FsZdspwvm2^%^2BGexcVVVTiY^%^2BRkYdONGqgyPofgiW6KI; 4fJN_2132_auth=fa1advZoxV0HKIY511Na2A14UuVPkEGextzkNEf3LTmYZNsVPWnPfpvE53q91E0HtOyeOzFvIoDUgoM0BFfdfgLImuY; 4fJN_2132_lastcheckfeed=360788^%^7C1720277707; 4fJN_2132_nofavfid=1; dv=1; 4fJN_2132_visitedfid=36D2D37; 4fJN_2132_saltkey=gfT2Y2T6; 4fJN_2132_lastvisit=1722823124; 4fJN_2132_forum_lastvisit=D_2_1724517854D_36_1724525009; PHPSESSID=fs6m69p7u0nkh24i2bou0pfd94; 4fJN_2132_st_t=0^%^7C1724525009^%^7C4464e74bf651602a334b6e1693abf1a0; 4fJN_2132_home_diymode=1; 4fJN_2132_seccodecSAfHzXCFY1W=33649.aec41f6f4462d73c7a; 4fJN_2132_st_p=0^%^7C1724524948^%^7C28c512a60741f151a2f2f3ac21e00a93; 4fJN_2132_viewid=tid_140950; 4fJN_2132_seccodecSe66M04=4590.8f6d9638130ea6aa17; 4fJN_2132_seccodecSS0E0vU=14021.67b9051126fe9ff19c; 4fJN_2132_seccodecSn0GiA0=54384.39bc15625c62e758ad; 4fJN_2132_lip=98.97.91.9^%^2C1722643381; bus_auth=1edafav4s3jAboxGlFgPe3ukZ^%^2F3UF0ndKEyDvg4qd^%^2B^%^2Bfwd447jVKwwzeys8; 4fJN_2132_seccodecSAdw3uaiuLy=2058.0c94c479f516006adb; 4fJN_2132_seccodecSAL97a2btdZ=32216.f7ef2171d96b9a533b; 4fJN_2132_seccodecSARr7SkqEnK=32559.3750609d5e1345401c; 4fJN_2132__refer=^%^252Fforum^%^252Fhome.php^%^253Fmod^%^253Dspacecp^%^2526ac^%^253Dsearch^%^2526username^%^253Dbecks2002^%^2526searchsubmit^%^253Dyes; 4fJN_2132_seccodecSAMJ7CwFn2b=33021.6b8079d6ffada97765; 4fJN_2132_seccodecSAQxRkynn6i=1951.cdafb31f3eea26a7f3; 4fJN_2132_seccodecSAMAQppbbt7=16808.02c2f2ff5f6f4dd39a; 4fJN_2132_seccodecSAZ25aiRGU4=23836.e064403d105d18bcc5',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
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
        av_id = (str(h['href']).split('/')[-1]).replace("-", ' ')
        if not if_file_exist_with_size(av_id, 200) and find_stars(h['href']):
            print(av_id)
            with open('av_id_hd.txt', 'a', encoding='utf-8') as file:  # 使用追加模式'a'
                file.write(av_id + '\n')


dir = r'F:\after\image\アイデアポケット\\' + ''


def find_image_url_from_href(href):
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
        {'url': '3', 'len': 69, 'name': '優木明日花'}
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
    get_star()
