# -*- coding: UTF8 -*-
from concurrent.futures import ThreadPoolExecutor
import requests
import os
import redis

'''
每一个文件的下载链接全部完成之后再开启下一个任务
'''
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

urls = [3, 2, 4]  # 并不是真的url
urls_s = [[3, 2, 4], [1, 7, 5], [9, 8, 1]]
url_resource = '/media/kevin/Backup/tumblr(2)/'


# 参数times用来模拟网络请求的时间
def init_file(f_file_name):
    if '.txt' in f_file_name:
        print(f_file_name + '  is beginning')
        a_file = open(url_resource + f_file_name, "r")
        list_of_lists = []
        for line in a_file:
            stripped_line = line.strip()
            if stripped_line:
                list_of_lists.append(stripped_line)
        a_file.close()
        executor = ThreadPoolExecutor(max_workers=8)
        all_task = [executor.submit(down_file, url) for url in list_of_lists]

        for future in as_completed(all_task):
            data = future.result()
            print("in main: get page {}s success".format(data))
        print(f_file_name + '  is end')
        return True
    else:
        return True


def down_file(url):
    pass
    # print('url = ' + url);


# -*- coding: UTF8 -*-
from concurrent.futures import ThreadPoolExecutor
import requests
import os
import redis

'''
每一个文件的下载链接全部完成之后再开启下一个任务
'''
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    #print("get page {}s finished".format(times))
    return times


urls = [3, 2, 4]  # 并不是真的url
urls_s = [[3, 2, 4, 2, 4], [1, 7, 5, 2, 4], [1, 1, 1, 2, 4]]

if __name__ == "__main__":
    executor = ThreadPoolExecutor(max_workers=6)
    for urls in urls_s:
        print("beginning")
        all_task = [executor.submit(get_html, url) for url in urls]
        for future in as_completed(all_task):
            data = future.result()
            print("in main: get page {}s success".format(data))
        print('end')

if __name__ == "__main__":
    if os.path.isdir(url_resource) and False:
        file_list = os.listdir(url_resource)
        for f_file in file_list:
            init_file(f_file)
