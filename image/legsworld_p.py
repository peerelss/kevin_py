import os.path
import argparse
from bs4 import BeautifulSoup
import requests

cookies = {
    'LW_lang': 'en',
    'pjAcceptCookie': 'YES',
    'BasicMail': 'xiepeerless^@gmail.com',
    'BasicUser': 'peerelss',
    'BasicPass': 'peerless',
    'ExpirationDate': '2023-12-20 02:37:45',
    'logged_in_as_member': '1',
    'BasicIdNr': '308',
    'Prem': '1',
    'lang': 'en',
    'PHPSESSID': '6635529e5f4b61392140a98911af36b9',
    'windowWidth': '1957',
    'windowHeight': '1037',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://legsworld.net/CSS_Version/MyGalleryDisplay.php?serno=0601',
    # 'Cookie': 'LW_lang=en; pjAcceptCookie=YES; BasicMail=xiepeerless^@gmail.com; BasicUser=peerelss; BasicPass=peerless; ExpirationDate=2023-12-20 02:37:45; logged_in_as_member=1; BasicIdNr=308; Prem=1; lang=en; PHPSESSID=6635529e5f4b61392140a98911af36b9; windowWidth=1957; windowHeight=1037',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'serno': '0606',
}


def download_img_from_url(url):
    s_url = str(url)
    if 'jpg' in s_url:
        print(s_url)
        dir_ = r'C:\Users\kevin\Downloads\legsworld\\' + s_url.split('/')[5] + '\\'
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
                if os.path.exists(dir_ + s_url[s_url.rfind('/'): s_url.index('jpg') + 3]):
                    print(dir_ + s_url[s_url.rfind('/'): s_url.index('jpg') + 3] + ' exist')
                else:
                    with open(dir_ + s_url[s_url.rfind('/'): s_url.index('jpg') + 3], "wb") as file:
                        file.write(response.content)


def get_name_from_url(url):
    filename = url.split('store=')[-1].split('&')[0]
    return filename


def download_video_from_url(s_url):
    file_dir = s_url.split('serno=')[-1].split('&')[0]
    dir_ = r'C:\Users\kevin\Downloads\legsworld\\' + file_dir + '\\'
    if os.path.exists(dir_):
        pass
    else:
        os.mkdir(dir_)

    if os.path.exists(dir_ + get_name_from_url(s_url)):
        print(dir_ + get_name_from_url(s_url) + " exist")
    else:
        response = requests.get(s_url, params=params, cookies=cookies,
                                headers=headers)
        with open(dir_ + get_name_from_url(s_url), "wb") as file:
            file.write(response.content)


def find_jpg_from_url(url):
    response = requests.get(url, params=params, cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    a_soup = soup.find_all('a', href=True)
    for a in a_soup:
        if 'MyGalleryDownload' in (a['href']):
            download_video_from_url('https://legsworld.net/CSS_Version/' + a['href'])
    '''tag = soup.find_all('img')
    for t in tag:
        ts = str(t['src']).replace('..', "")
        if '.jpg' in ts:
            #  download_img_from_url('https://legsworld.net' + ts)
            print('https://legsworld.net' + ts)
'''


def get_image_from_url(index):
    params['serno'] = str(index)
    if index < 1000:
        params['serno'] = '0' + str(index)

    response = requests.get('https://legsworld.net/CSS_Version/MyGallery.php', params=params, cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(response.content, "lxml")

    a_soup = soup.find_all('a', href=True)
    for a in a_soup:
        if 'MyGalleryDisplay.php' in a['href']:
            find_jpg_from_url('https://legsworld.net/CSS_Version/' + a['href'])
            print('https://legsworld.net/CSS_Version/' + a['href'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='示例脚本')
    parser.add_argument('--param', type=int, help='一个整数参数')

    args = parser.parse_args()
    print(f"接收到的参数：{args.param}")
    for i in (range(args.param, 7229)):
        print(str(i))
        get_image_from_url(i)
