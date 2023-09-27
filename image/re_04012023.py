from bs4 import BeautifulSoup
import time
import os
import requests

cookies = {
    'session7': 'eyJpZCI6IjJjNzJmZTEzYWY3ZDUifQ==',
    'session7.sig': 'ueYcxZ9N5OjJLXZcW4gULyJwU_Q',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://reflectivedesire.com/photos/',
    # 'Cookie': 'session7=eyJpZCI6IjJjNzJmZTEzYWY3ZDUifQ==; session7.sig=ueYcxZ9N5OjJLXZcW4gULyJwU_Q',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'If-None-Match': 'W/a965-Ia7bt90rst6ER/UGiZj3s1wTKLA',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


def get_image_from_page(page_url):
    # 使用 Beautiful Soup 解析网页内容
    soup = BeautifulSoup(requests.get(page_url).text, 'html.parser')
    pictures = soup.find_all('picture')
    for picture in pictures:
        sources = picture.find_all('source')
        if len(sources) > 1:
            print(str(sources[0]['srcset']).split(' ')[0])
            print(str(sources[1]['srcset']).split(' ')[0])


def get_page_by_index(index):
    params = {
        'sort': 'special-blend',
        'page': str(index),
    }

    response = requests.get('https://reflectivedesire.com/photos/', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")
    for link in links:
        get_image_from_page('https://reflectivedesire.com' + link.get("href"))


file_path = 'D:\\image'


def download_image(image_url):
    dir_name = file_path + '\\' + image_url.split("/")[-2]
    if os.path.exists(dir_name):
        pass
    else:
        os.mkdir(dir_name)

    image_name = dir_name + '\\' + image_url.split("/")[-1]
    print(image_name)
    if os.path.exists(image_name):
        print(image_name + " exist ")
    else:
        print(image_name + " downing ")
        response_image = requests.get(image_url)
        with open(image_name, "wb") as img_file:
            img_file.write(response_image.content)


if __name__ == '__main__':
    filename = "C:\\Users\\kevin\\Desktop\\re.txt"
    with open(filename, "r") as f:
        for url in f:
            url = url.strip()  # 去除每行URL末尾的换行符
            if url.startswith('http'):
                download_image(url)
