# -*- coding: UTF8 -*-
from concurrent.futures import ThreadPoolExecutor
import requests
import os
import redis
# redis 相关的关键字
r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_saved = "redis_set_tumblr_dir"  # 保存所有已经下载过的tumblr的txt的文件名
redis_tumblr_dir_file_redirected = 'redis_set_tumblr_dir_file_redirected'  # 保存所有被重定向的url
redis_tumblr_dir_file_from_url = 'redis_set_tumblr_dir_file'  # 保存所有已被下载的url
redis_tumblr_dir_file_redirected_incr = 'redis_set_tumblr_dir_file_redirected_incr'  # 记录多少个被重定向
import time
import datetime

import os

'''
每一个文件的下载链接全部完成之后再开启下一个任务
'''
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

urls = [3, 2, 4]  # 并不是真的url
urls_s = [[3, 2, 4], [1, 7, 5], [9, 8, 1]]
url_resource = '/media/kevin/Backup/tumblr_txt_all2/'


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
    # print("get page {}s finished".format(times))
    return times


urls = [3, 2, 4]  # 并不是真的url
urls_s = [[3, 2, 4, 2, 4], [1, 7, 5, 2, 4], [1, 1, 1, 2, 4]]


# if __name__ == "__main__":
#     executor = ThreadPoolExecutor(max_workers=6)
#     for urls in urls_s:
#         print("beginning")
#         all_task = [executor.submit(get_html, url) for url in urls]
#         for future in as_completed(all_task):
#             data = future.result()
#             print("in main: get page {}s success".format(data))
#         print('end')

def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(102)
    return round(fsize, 2)


if __name__ == "__main__":
    if os.path.exists(url_resource) and os.path.isdir(url_resource):
        list_fi=os.listdir(url_resource)
        for i in list_fi:
            if 'bdsmlr' in str(i):
                print(str(i))
