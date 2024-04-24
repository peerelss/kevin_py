import requests
from bs4 import BeautifulSoup
import time
import os
from image.sdk_every_thing_http import if_file_exist_with_size
import sys


def read_file_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取所有行到列表
        lines = file.readlines()
    # 移除每行末尾的换行符
    return [line.strip() for line in lines]


def san_model_2():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://tranniesintrouble.com/members/archive.html',
        'Authorization': 'Basic eGllcGVlcmxlc3M6UGVlcmxlc3MxMjM=',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }

    response = requests.get('https://tranniesintrouble.com/members/models_02.html', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    # 查找所有的<a>标签
    for link in soup.find_all('a'):
        href = link.get('href')
        # 确保href存在
        if href and ('photo' in href or 'video' in href) and str(href).endswith('page.html'):
            links.append(href)
    return links


def get_photos_and_videos(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://tranniesintrouble.com/members/models_archive_01.html',
        'Authorization': 'Basic eGllcGVlcmxlc3M6UGVlcmxlc3MxMjM=',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    full_url = 'https://tranniesintrouble.com/members/' + url
    response = requests.get(full_url,
                            headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    # 查找所有的<a>标签
    for link in soup.find_all('a'):
        href = link.get('href')
        # 确保href存在
        if href and (str(href).endswith('.mp4') or str(href).endswith('.zip')):
            d_l = (full_url.replace('page.html', href))
            links.append(d_l)
    return links


# 示例用法
def download_file(url):
    file_name = url.split('/')[-1]
    if if_file_exist_with_size(file_name, 1):
        print(file_name + '   exist')
        return
        # 检查URL是否以.zip或.mp4结尾
    time.sleep(5)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://tranniesintrouble.com/members/models_archive_01.html',
        'Authorization': 'Basic eGllcGVlcmxlc3M6UGVlcmxlc3MxMjM=',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    if url.endswith('.zip') or url.endswith('.mp4'):
        try:
            # 发送GET请求
            response = requests.get(url, headers=headers, stream=True)
            # 确保请求成功
            if response.status_code == 200:
                # 提取文件名
                # 定义下载文件夹的路径
                download_folder = 'downloads'
                # 创建下载文件夹如果不存在
                if not os.path.exists(download_folder):
                    os.makedirs(download_folder)
                # 完整的文件路径
                file_path = os.path.join(download_folder, file_name)
                # 打开一个本地文件用于保存下载的数据
                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        # 将内容写入文件
                        file.write(chunk)
                print(f"文件已保存: {file_name}")
            else:
                print("错误：文件下载失败，响应码", response.status_code)
        except Exception as e:
            print("下载错误：", e)
    else:
        print("错误：URL不指向.zip或.mp4文件")


def get_href():
    cookies = {
        'aywcUid': 'f9bBYPN9U3_20240407154209',
        'aywcUid': 'f9bBYPN9U3_20240407154209',
        'tet': '1712548820089',
        'tetm': '1605A',
        'tcv': 'V4',
        'JSESSIONID': '6A6327B39C9A0012F43ACC2D663A98AF',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://wuqianun.top/search?keyword=Christina+Bound&sos=relevance&sofs=all&sot=all&soft=all&som=exact&p=4',
        # 'Cookie': 'aywcUid=f9bBYPN9U3_20240407154209; aywcUid=f9bBYPN9U3_20240407154209; tet=1712548820089; tetm=1605A; tcv=V4; JSESSIONID=6A6327B39C9A0012F43ACC2D663A98AF',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'keyword': 'Christina Bound',
        'sos': 'relevance',
        'sofs': 'all',
        'sot': 'all',
        'soft': 'all',
        'som': 'exact',
        'p': '3',
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


def get_magent():
    cookies = {
        'aywcUid': 'f9bBYPN9U3_20240407154209',
        'aywcUid': 'f9bBYPN9U3_20240407154209',
        'tet': '1712548820089',
        'tetm': '1605A',
        'tcv': 'V4',
        'JSESSIONID': '6A6327B39C9A0012F43ACC2D663A98AF',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://wuqianun.top/search?keyword=avs_museum-100342',
        'Connection': 'keep-alive',
        # 'Cookie': 'aywcUid=f9bBYPN9U3_20240407154209; aywcUid=f9bBYPN9U3_20240407154209; tet=1712548820089; tetm=1605A; tcv=V4; JSESSIONID=6A6327B39C9A0012F43ACC2D663A98AF',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get('https://wuqianun.top/detail/07AE4/ytBPCHWwGQMhWMFNf-ud5TIIF08', cookies=cookies,
                            headers=headers)


def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()
    # Print New Line on Complete
    if iteration == total:
        print()


def text():
    photo_links = san_model_2()
    task_length = len(photo_links)
    print(f"Hello ,task length is  {task_length}  ")
    for photo_link in photo_links:
        print(photo_link)
        download_links = get_photos_and_videos(photo_link)
        for link in download_links:
            download_file(link)
            print_progress_bar(photo_links.index(photo_link) + 1, task_length, prefix='Progress:', suffix='Complete ',
                               length=50)


def get_video_link(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Authorization': 'Basic eGllcGVlcmxlc3M6UGVlcmxlc3MxMjM=',
        'Connection': 'keep-alive',
        'Referer': 'https://tranniesintrouble.com/members/video.php',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }

    params = {
        'pageno': page,
        'q': '',
        'sort': 'latest',
        'perpage': '30',
    }

    response = requests.get('https://tranniesintrouble.com/members/video.php', params=params, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    # 查找所有的<a>标签
    for link in soup.find_all('a'):
        href = link.get('href')
        # 确保href存在
        if href and (str(href).endswith('.mp4') or str(href).endswith('.zip')):
            d_l = (href)
            links.append('https://tranniesintrouble.com/members/' + d_l)
    return links


if __name__ == "__main__":
    for i in range(1, 19):
        links = get_video_link(i)
        for link in links:
            if 'small_versions' not in link:
                download_file(link)
                print_progress_bar(links.index(link) + 1, len(links), prefix='Progress:', suffix='Complete ',
                                   length=50)
