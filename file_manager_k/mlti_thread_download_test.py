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

url_resource = '/media/kevin/Backup/xiepe/'

import os
import redis

temp = 0


def find_if_multi_file(file_dir):
    f_list = os.listdir(file_dir)
    for f in f_list:
        f_str = str(f)
        if f_str.endswith('gif') or f_str.endswith('jpg') or f_str.endswith(
                'pnj') or f_str.endswith('gifv') or f_str.endswith('jpeg') or f_str.endswith('png'):
            full_name = file_dir + '/' + f_str
            if 'avatar' in f_str:
                os.remove(full_name)
            else:
                if r_redis.sismember(redis_tumblr_dir_file_from_url, f_str):
                    file_full_dir = r_redis.get(f_str)
                    if file_full_dir != full_name:
                        print(file_full_dir)
                        os.remove(full_name)
                else:
                    pass
                    r_redis.set(f_str, full_name)
                    r_redis.sadd(redis_tumblr_dir_file_from_url, f_str)
                    r_redis.sadd(redis_tumblr_dir_file_from_url, full_name)


def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(102)
    return round(fsize, 2)


if __name__ == "__main__":
    if os.path.exists(url_resource) and os.path.isdir(url_resource):
        list_fi = os.listdir(url_resource)
        for i in list_fi:
            print(str(i))
            if os.path.isdir(url_resource + str(i)):
                find_if_multi_file(url_resource + str(i))
