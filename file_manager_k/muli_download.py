# -*- coding: UTF8 -*-
'''
指定文件夹，
    打开txt文件 resource.txt
        从文件名生成文件夹名 resource
    按行读取，生成文件名  http：// tumblr.jpg 生成 tumblr.jpg
        如果被重定向，则不下在 history
        否则保存
'''

from concurrent.futures import ThreadPoolExecutor
import requests
import os
import redis

url_resource = '/media/kevin/Backup/tumblr_txt_all3'
url_target = '/media/kevin/Backup/images2/'

# redis 相关的关键字
r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_saved = "redis_set_tumblr_dir"  # 保存所有已经下载过的tumblr的txt的文件名
redis_tumblr_dir_file_redirected = 'redis_set_tumblr_dir_file_redirected'  # 保存所有被重定向的url
redis_tumblr_dir_file_from_url = 'redis_set_tumblr_dir_file'  # 保存所有已被下载的url
redis_tumblr_dir_file_redirected_incr = 'redis_set_tumblr_dir_file_redirected_incr'  # 记录多少个被重定向
file_name = r'/media/kevin/Backup/tumblr_txt_all3/'
file_path = 'zirtamail'


def download_tumblr_jpg(*jpg_url):
    file_name_t = str(jpg_url[0]).split('/')[-1]  # 文件名
    file_name_full = url_target + file_path + '/' + file_name_t
    if r_redis.exists(file_name_t) and os.path.exists(r_redis.get(file_name_t)):
        print('%s 存在 from disk ' % r_redis.get(file_name_t))
    elif r_redis.sismember(redis_tumblr_dir_file_from_url, file_name_t):
        print('%s 经被下载过 ' % jpg_url[0])
    elif r_redis.sismember(redis_tumblr_dir_file_redirected, file_name_t) or r_redis.sismember(
            redis_tumblr_dir_file_redirected, jpg_url[0]):
        print('%s  已经被重定向 from redis' % file_name_t)
        r_redis.incr(redis_tumblr_dir_file_redirected_incr)
    elif os.path.exists(file_name_full) or os.path.exists(
            file_name_full.replace('daddywantskitten0', 'daddywantskitten')):
        print('%s 已存在' % jpg_url[0])
    else:
        html = requests.get(jpg_url[0])
        if html.history:
            print('%s  已经被重定向 from network' % jpg_url[0])
            r_redis.incr(redis_tumblr_dir_file_redirected_incr)
            r_redis.sadd(redis_tumblr_dir_file_redirected, jpg_url[0])
            r_redis.sadd(redis_tumblr_dir_file_redirected, file_name_t)
        else:
            with open(file_name_full, "wb") as file:
                file.write(html.content)
            print('%s  正在下载ing  from network' % jpg_url[0])
            r_redis.sadd(redis_tumblr_dir_file_from_url, file_name_t)
            r_redis.sadd(redis_tumblr_dir_file_from_url, jpg_url[0])
            r_redis.set(file_name_t, file_name_full)


def init_list():
    a_file = open(file_name, "r")
    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        if stripped_line:
            list_of_lists.append(stripped_line)
    a_file.close()
    file_dir_path = url_target + file_path
    # print(list_of_lists)
    if os.path.exists(file_dir_path):
        pass
    else:
        os.mkdir(file_dir_path)
    executor = ThreadPoolExecutor(max_workers=8)
    for i in list_of_lists:
        executor.submit(download_tumblr_jpg, i)


if __name__ == "__main__":
    current_file = 'sex-n-stunners_tumblr_.txt'
    file_name = file_name + current_file
    file_path = current_file.split('_')[0]
    init_list()

