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
    'user_uuid': '52d1e308-968a-4ef5-bed1-3bb6060b5f30',
    'cf_clearance': 'dmcmSIW9ZroOvgHWGdvFg0BS_vwG5tIitpd59ZkzPYw-1745064078-1.2.1.1-O7UYq7c691gpNqwaoUWVp_U9b2Vn4QIV84xRdgomkTHegUxEeiLlmy_ZVI4mvv2_FtyUmSzb9Mt3YCRMwSATLMzcDvHkoxW0D8C7kZ24L6zAhD9oRoIFxH0uuMABtOOHRK6mfCEhUd8yqk4q1Fl07FY81K2cgp51w6GMAyh8apk9yfgeD9dG3m9Fht4FcQT6..yJlsTItQ6ATNCVS2Hw13M9wAWRPfT0MwDs87F69vO6fdndEt4vcFSsRTNkyRNPLtOahs_tqdz9Px5LWd1sJMfvWpCnMDikYOGr6LCguy0IL_MRta1yvBMOXtpn.3.8r.UQUU1qLpwRWbdNYKIVbOCGcrvdYvKZDeIKZdgNvms',
    'search_history': '[%22mbyd%22%2C%22migd-049%22%2C%22BOBO%22%2C%22JFYG%22%2C%22wdi%22%2C%22iptd-519%22]',
    'XSRF-TOKEN': 'eyJpdiI6IjlVcXFRMWJvOEFlNnZoNnlabkIyU2c9PSIsInZhbHVlIjoiNTVpczR0VytSbjcxQXVOZHZFWWoxbm4xODZlQXUyQzVvbitVdHdDUXltWUx6MGcxTE5sSWRCQXBLcmhmejkwd3JjVC8yTDJVQ3dKWTVJQTdxcnY1ckh6Uy9oVWppYmlNYmNrZ0Q1NmxYWGhNVDJBVjZRdU1YUHNZaGVBQnVXdEciLCJtYWMiOiIwMzZiOWZmNWVmNjY4MDFkYjk5NTc4M2E5NzQ1YWFhY2EzNGQ3Mzc2MDM5ZmRiODc1MWJjMWU1YmUxMTAzODlhIiwidGFnIjoiIn0%3D',
    'missav_session': 'eyJpdiI6IjkzQU1sMStGM2hLRDVZQ3pKN2t6S3c9PSIsInZhbHVlIjoiMXZDcHZCcjNsTVlybGhEeWRRTHhOay9qYy85MDlNZVZyZndaLzdvR0U0eG1VLzdYRFpTWm0xVzN2UGlUcGtWWTAybUo3dWt2S2FyUEZnTmYwWmdvRmIwWTE1MWlpdjJIVWtFSE01R1hjMnhoczdzRHZ4SVhBYm5ld293N05iNEgiLCJtYWMiOiI1NDMyYmZjZTk2OTZjOTlhMDBjZTBjMGRjMzg0OGQ5MzdlMzhlNGZkYzVmNWI2NjNlZWVmOTllMGM5OTJkYmI3IiwidGFnIjoiIn0%3D',
    'EQOHSUoHkhnxo1ZnsLM6ubuLKtFYofFr5YnN4QDt': 'eyJpdiI6IkJmL0loRURLMGVSdjRac3FEREgxSlE9PSIsInZhbHVlIjoiWFJZb3NRT1pNaGpaQ3lqZkZOZTM3N2ZXaUxJQkd2d21PTmFLem45eVNuMmRkT1A0NHpURFBLMHA4YWZ1eGRJLzA2N0FKem5pekFvSFVvUGU5TllQT21wamljYVpLVEdJVmxzOHNWRGtVTVVSSXpydVJyVHp1djdvK0d4dm9mUkwzbWVOK3lBWUlFV1NwN29wVFU1c0JlN013dE92c1hFbGgyemZ6SXNqMy9OaWpIQ0svblhPc2E1SUZLaFlRYVpEZEpxcmVlQWplb0lFd09OUVBMbXRCNTlTU0M3WktYeEt4ekhUWVlHWTZxcysyNmx1cUNVYUh4a1hONXduREw2bmkzenBZY25tZU82OENiMGNlWTN0bjQ5enRvMjlyKzEyNXZmY2dlVjRZcGVIYlVOUFprOWd6STBWQ3BCQndrYS90UlN2Z0oyUXBrdnVVY1g0aHVtcVNiVnBRSjhDWjhTTzVoZXlSOTViMEw5ZC9FeVlZNkZSRCsxNlZITmF3N2FFT05aTGFlRXk5SHhKUDE1SUt2VmE4Zz09IiwibWFjIjoiNmY2M2E3YTRmYjg1OGFjZTQ5ZmNkMTRiMjM4MjA3NjZkYWQ0ZDRhMWQ1YjNkNGE2ODEwMjdlZjdiNmIyZTVmOSIsInRhZyI6IiJ9',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://missav123.com/dm23/cn/actresses/%E4%BA%8C%E5%AE%AB%E5%92%8C%E9%A6%99?page=25',
    'Connection': 'keep-alive',
    # 'Cookie': 'user_uuid=52d1e308-968a-4ef5-bed1-3bb6060b5f30; cf_clearance=dmcmSIW9ZroOvgHWGdvFg0BS_vwG5tIitpd59ZkzPYw-1745064078-1.2.1.1-O7UYq7c691gpNqwaoUWVp_U9b2Vn4QIV84xRdgomkTHegUxEeiLlmy_ZVI4mvv2_FtyUmSzb9Mt3YCRMwSATLMzcDvHkoxW0D8C7kZ24L6zAhD9oRoIFxH0uuMABtOOHRK6mfCEhUd8yqk4q1Fl07FY81K2cgp51w6GMAyh8apk9yfgeD9dG3m9Fht4FcQT6..yJlsTItQ6ATNCVS2Hw13M9wAWRPfT0MwDs87F69vO6fdndEt4vcFSsRTNkyRNPLtOahs_tqdz9Px5LWd1sJMfvWpCnMDikYOGr6LCguy0IL_MRta1yvBMOXtpn.3.8r.UQUU1qLpwRWbdNYKIVbOCGcrvdYvKZDeIKZdgNvms; search_history=[%22mbyd%22%2C%22migd-049%22%2C%22BOBO%22%2C%22JFYG%22%2C%22wdi%22%2C%22iptd-519%22]; XSRF-TOKEN=eyJpdiI6IjlVcXFRMWJvOEFlNnZoNnlabkIyU2c9PSIsInZhbHVlIjoiNTVpczR0VytSbjcxQXVOZHZFWWoxbm4xODZlQXUyQzVvbitVdHdDUXltWUx6MGcxTE5sSWRCQXBLcmhmejkwd3JjVC8yTDJVQ3dKWTVJQTdxcnY1ckh6Uy9oVWppYmlNYmNrZ0Q1NmxYWGhNVDJBVjZRdU1YUHNZaGVBQnVXdEciLCJtYWMiOiIwMzZiOWZmNWVmNjY4MDFkYjk5NTc4M2E5NzQ1YWFhY2EzNGQ3Mzc2MDM5ZmRiODc1MWJjMWU1YmUxMTAzODlhIiwidGFnIjoiIn0%3D; missav_session=eyJpdiI6IjkzQU1sMStGM2hLRDVZQ3pKN2t6S3c9PSIsInZhbHVlIjoiMXZDcHZCcjNsTVlybGhEeWRRTHhOay9qYy85MDlNZVZyZndaLzdvR0U0eG1VLzdYRFpTWm0xVzN2UGlUcGtWWTAybUo3dWt2S2FyUEZnTmYwWmdvRmIwWTE1MWlpdjJIVWtFSE01R1hjMnhoczdzRHZ4SVhBYm5ld293N05iNEgiLCJtYWMiOiI1NDMyYmZjZTk2OTZjOTlhMDBjZTBjMGRjMzg0OGQ5MzdlMzhlNGZkYzVmNWI2NjNlZWVmOTllMGM5OTJkYmI3IiwidGFnIjoiIn0%3D; EQOHSUoHkhnxo1ZnsLM6ubuLKtFYofFr5YnN4QDt=eyJpdiI6IkJmL0loRURLMGVSdjRac3FEREgxSlE9PSIsInZhbHVlIjoiWFJZb3NRT1pNaGpaQ3lqZkZOZTM3N2ZXaUxJQkd2d21PTmFLem45eVNuMmRkT1A0NHpURFBLMHA4YWZ1eGRJLzA2N0FKem5pekFvSFVvUGU5TllQT21wamljYVpLVEdJVmxzOHNWRGtVTVVSSXpydVJyVHp1djdvK0d4dm9mUkwzbWVOK3lBWUlFV1NwN29wVFU1c0JlN013dE92c1hFbGgyemZ6SXNqMy9OaWpIQ0svblhPc2E1SUZLaFlRYVpEZEpxcmVlQWplb0lFd09OUVBMbXRCNTlTU0M3WktYeEt4ekhUWVlHWTZxcysyNmx1cUNVYUh4a1hONXduREw2bmkzenBZY25tZU82OENiMGNlWTN0bjQ5enRvMjlyKzEyNXZmY2dlVjRZcGVIYlVOUFprOWd6STBWQ3BCQndrYS90UlN2Z0oyUXBrdnVVY1g0aHVtcVNiVnBRSjhDWjhTTzVoZXlSOTViMEw5ZC9FeVlZNkZSRCsxNlZITmF3N2FFT05aTGFlRXk5SHhKUDE1SUt2VmE4Zz09IiwibWFjIjoiNmY2M2E3YTRmYjg1OGFjZTQ5ZmNkMTRiMjM4MjA3NjZkYWQ0ZDRhMWQ1YjNkNGE2ODEwMjdlZjdiNmIyZTVmOSIsInRhZyI6IiJ9',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'If-Modified-Since': 'Sat, 19 Apr 2025 04:21:29 GMT',
    'Priority': 'u=0, i',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


def get_title_and_url(page):
    target_url = f"https://missav123.com/dm23/cn/actresses/%E4%BA%8C%E5%AE%AB%E5%92%8C%E9%A6%99?page={page}"
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

if __name__ == '__main__':
    for i in range(1,25):
        result_id= get_title_and_url(i)
        for av_id in result_id:
           if not if_file_exist_with_size(av_id['alt'].replace("-"," "),100):
               print(av_id["alt"])
        time.sleep(4)