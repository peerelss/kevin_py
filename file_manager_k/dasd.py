import time

from image.sdk_every_thing_http import if_file_exist_with_size
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from urllib.parse import urljoin


def txt_2_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    return lines


cookies = {
    'existmag': 'mag',
    'age': 'verified',
    'dv': '1',
    'PHPSESSID': 'vkomj5hrq242mt6i8hgo6rdhv4',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    # 'Cookie': 'existmag=mag; age=verified; dv=1; PHPSESSID=vkomj5hrq242mt6i8hgo6rdhv4',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Priority': 'u=0, i',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


def get_title_and_url(page):
    target_url = f"https://missav123.com/cn/search/FLAV?page={page}"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 720},
            locale="zh-CN"
        )
        page = context.new_page()
        page.goto(target_url)
        elements = page.query_selector_all("a.text-secondary")
        results = []
        for el in elements:
            href = el.get_attribute("href")
            alt = el.get_attribute("alt")
            text = el.inner_text().strip()

            # 处理相对链接为绝对链接
            full_href = urljoin(target_url, href) if href else None

            results.append({
                "href": full_href,
                "alt": alt,
                "text": text
            })
        # 输出结果
        browser.close()
        return results


def get_url_info_by_pyweb():
    for i in range(1, 37):
        print(str(i))
        result_id = get_title_and_url(i)
        for av_id in result_id:
            av_title = av_id['alt']
            if not if_file_exist_with_size(av_title.replace('-uncensored-leak', '').replace("-chinese-subtitle", ""), 100):
                print(av_title)
        time.sleep(6)


def is_avid_a_single(avid):
    try:
        response = requests.get(f'https://www.javbus.com/{avid}', cookies=cookies, headers=headers)
        response.raise_for_status()
        html = response.text
        # 用 BeautifulSoup 解析网页
        soup = BeautifulSoup(html, 'html.parser')
        avatar_boxes = soup.find_all(class_="avatar-box")
        # 输出数量
        return len(avatar_boxes) <= 4
    except Exception as e:
        print("解析网页时出错:", e)
        return True


def is_avid_single_and_not_exist():
    url_list = txt_2_list('dasd.txt')
    for url_id in url_list:
        if len(url_id) > 5 and is_avid_a_single(url_id.replace('-uncensored-leak', '').replace('-chinese-subtitle','')):
            print(url_id)
        time.sleep(1)


if __name__ == '__main__':
   get_url_info_by_pyweb()
   # is_avid_single_and_not_exist()
