import os.path

from bs4 import BeautifulSoup
import re
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
    'windowWidth': '1809',
    'windowHeight': '1103',
    'PHPSESSID': '6635529e5f4b61392140a98911af36b9',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://legsworld.net/CSS_Version/start.php?update=7058&lang=en&direct=',
    'Connection': 'keep-alive',
    # 'Cookie': 'LW_lang=en; pjAcceptCookie=YES; BasicMail=xiepeerless^@gmail.com; BasicUser=peerelss; BasicPass=peerless; ExpirationDate=2023-12-20 02:37:45; logged_in_as_member=1; BasicIdNr=308; Prem=1; lang=en; windowWidth=1809; windowHeight=1103; PHPSESSID=6635529e5f4b61392140a98911af36b9',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'serno': '7058',
    'speed': '3',
    'direct': '',
}

response = requests.get('https://legsworld.net/CSS_Version/MyGallery.php', params=params, cookies=cookies,
                        headers=headers)


def find_window_location_href(index):
    params['serno'] = str(index)
    if index < 1000:
        params['serno'] = '0' + str(index)
    response = requests.get('https://legsworld.net/CSS_Version/MyGallery.php', params=params, cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    scripts = soup.find_all('script')
    for script in scripts:
        if script.string:
            match = re.search(r'window\.self\.location\.href\s*=\s*["\'](.*?)["\']', script.string)
            if match:
                print(match.group(1))
                return match.group(1)

    return None


def down_mp4_from_url(url):
    print(url)
    filename = url.split('store=')[-1].split('&')[0]
    print(filename)
    dir_name = r'C:\Users\kevin\Downloads\legsworld\\' + filename
    if os.path.exists(dir_name):
        print(dir_name + " exist")
    else:
        response = requests.get(url, cookies=cookies,
                                headers=headers)
        with open(dir_name, "wb") as file:
            file.write(response.content)


def get_mp4_from(url):
    response = requests.get(url, cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    a_soup = soup.find_all('a', href=True)
    for a in a_soup:
        if 'store=Legsworld' in a['href'] and 'mp4' in a['href']:
            mp4_url = 'https://legsworld.net/CSS_Version/' + a['href']
            down_mp4_from_url(mp4_url)


def get_image_from_url(index):
    params['serno'] = str(index)
    if index < 1000:
        params['serno'] = '0' + str(index)
    response = requests.get('https://legsworld.net/CSS_Version/MyGallery.php', params=params, cookies=cookies,
                            headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    print(soup)


if __name__ == '__main__':
    for i in reversed(range(4681, 6703)):
        get_mp4_from('https://legsworld.net/CSS_Version/MyGalleryDisplay.php?serno=' + str(i) + '&pic=0')
