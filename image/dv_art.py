import psutil
import requests
from bs4 import BeautifulSoup
import re

cookies = {
    'existmag': 'mag',
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
    'Referer': 'https://www.javbus.com/',
    'Connection': 'keep-alive',
    # 'Cookie': 'existmag=mag; starinfo=glyphicon^%^20glyphicon-plus; 4fJN_2132_ulastactivity=ce7ehrRkSv1dhxLb1H4AULx3geEYlXcGi9JwS2dbZOiibkQkpOtc; 4fJN_2132_auth=c86eNEVgbUfFuUm8uba8QRsf9nt3AGNzOM6AEKqn2bqipi^%^2B2vfy5EAkD7TzdFZReyDu8dy8CjJsO4sUB5cb83zw6Em0; 4fJN_2132_lastcheckfeed=360788^%^7C1712523398; 4fJN_2132_nofavfid=1; dv=1; 4fJN_2132_visitedfid=36D2; 4fJN_2132_saltkey=KsQ0La8i; 4fJN_2132_lastvisit=1712274955; PHPSESSID=fs6m69p7u0nkh24i2bou0pfd94; 4fJN_2132_st_t=0^%^7C1712522614^%^7C77143bfb9ee2fd87952d093ed5c68cb8; 4fJN_2132_home_diymode=1; 4fJN_2132_seccodecSAfHzXCFY1W=33649.aec41f6f4462d73c7a; 4fJN_2132_st_p=360788^%^7C1714547485^%^7C2e8bc3a17fc46cecbec094480006a211; 4fJN_2132_viewid=tid_133058; 4fJN_2132_seccodecSe66M04=4590.8f6d9638130ea6aa17; 4fJN_2132_seccodecSS0E0vU=14021.67b9051126fe9ff19c; 4fJN_2132_seccodecSn0GiA0=54384.39bc15625c62e758ad; 4fJN_2132_lip=47.153.82.31^%^2C1712813361; bus_auth=cd0b7^%^2BQZENfAavhbLcSZt7Aa^%^2BDEGQCQxTyoLMMgVGPlLO0W6TQBOtZ7IQmI; 4fJN_2132_seccodecSAdw3uaiuLy=2058.0c94c479f516006adb; 4fJN_2132_seccodecSAL97a2btdZ=32216.f7ef2171d96b9a533b; 4fJN_2132_seccodecSARr7SkqEnK=32559.3750609d5e1345401c; 4fJN_2132__refer=^%^252Fforum^%^252Fhome.php^%^253Fmod^%^253Dspacecp^%^2526ac^%^253Dsearch^%^2526username^%^253Dbecks2002^%^2526searchsubmit^%^253Dyes; 4fJN_2132_seccodecSAMJ7CwFn2b=33021.6b8079d6ffada97765',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
import time


def get_script(av_id):
    # Fetch the webpage
    if len(av_id) > 5:
        response = requests.get('https://www.javbus.com/' + str(av_id).replace(' ', '-'), cookies=cookies,
                                headers=headers)
        html_content = response.content
        # Parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract <script> tags
        script_tags = soup.find_all('script')

        # Print the content of each script tag
        for script in script_tags:
            if script.string is not None and 'var gid' in script.string:  # This checks if the script tag contains anything
                values = re.findall(r'=\s*([^;]+);', script.string)
                return values


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
        for i in range(0, magnet_length):
            print(script_tags[i * 3 + 1]['href'])
            print(script_tags[i * 3 + 1].text)
        with open('magnet_av_id.txt', 'a', encoding='utf-8') as file:  # 使用追加模式'a'
            file.write(script_tags[0]['href'] + '\n')


def get_disk_info():
    # 获取磁盘分区信息
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== 分区设备：{partition.device} ===")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(f"  总容量: {partition_usage.total / (1024 ** 3):.2f} GB")
            print(f"  已用容量: {partition_usage.used / (1024 ** 3):.2f} GB")
            print(f"  可用容量: {partition_usage.free / (1024 ** 3):.2f} GB")
            print(f"  使用率: {partition_usage.percent}%")
        except PermissionError:
            # 某些特殊分区可能需要管理员权限才能访问
            print("  访问被拒绝。")


if __name__ == "__main__":
    read_lines = open(r'C:\Users\kevin\Documents\av_id_hd.txt', 'r', encoding='utf-8').readlines()
    for line in read_lines:

        result_v = get_script(line)
        if result_v:
            get_magnet_by_gid(result_v)
