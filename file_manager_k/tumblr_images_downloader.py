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
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED

url_resource = '/media/kevin/Backup/tumblr_txt_all3/'
url_target = '/media/kevin/Backup/images6/'
current_file = "default "
# redis 相关的关键字
r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_saved = "redis_set_tumblr_dir"  # 保存所有已经下载过的tumblr的txt的文件名
redis_tumblr_dir_file_redirected = 'redis_set_tumblr_dir_file_redirected'  # 保存所有被重定向的url
redis_tumblr_dir_file_from_url = 'redis_set_tumblr_dir_file'  # 保存所有已被下载的url
redis_tumblr_dir_file_redirected_incr = 'redis_set_tumblr_dir_file_redirected_incr'  # 记录多少个被重定向


def download_tumblr_jpg(*jpg_url):
    file_name_t = str(jpg_url[0]).split('/')[-1]  # 文件名
    file_name_full = url_target + file_path + '/' + file_name_t
    if r_redis.exists(file_name_t):
        pass
    elif r_redis.sismember(redis_tumblr_dir_file_from_url, file_name_t):
        pass
    elif r_redis.sismember(redis_tumblr_dir_file_redirected, file_name_t) or r_redis.sismember(
            redis_tumblr_dir_file_redirected, jpg_url[0]):
        r_redis.incr(redis_tumblr_dir_file_redirected_incr)
    elif os.path.exists(file_name_full):
        pass
    else:
        html = requests.get(jpg_url[0])
        if html.history:
            r_redis.incr(redis_tumblr_dir_file_redirected_incr)
            r_redis.sadd(redis_tumblr_dir_file_redirected, jpg_url[0])
            r_redis.sadd(redis_tumblr_dir_file_redirected, file_name_t)
        else:
            print(file_path)
            with open(file_name_full, "wb") as file:
                file.write(html.content)
            print('%s  正在下载ing  from network' % jpg_url[0])
            r_redis.sadd(redis_tumblr_dir_file_from_url, file_name_t)
            r_redis.sadd(redis_tumblr_dir_file_from_url, jpg_url[0])
            r_redis.set(file_name_t, file_name_full)


def init_list(*f_name):
    a_file = open(f_name[0], "r")
    print(f_name[0])
    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        if stripped_line:
            list_of_lists.append(stripped_line)
    a_file.close()
    file_dir_path = url_target + f_name[1]
    # print(list_of_lists)
    if os.path.exists(file_dir_path):
        pass
    else:
        os.mkdir(file_dir_path)
    executor = ThreadPoolExecutor(max_workers=4)
    all_task = [executor.submit(download_tumblr_jpg, (i)) for i in list_of_lists]
    wait(all_task, return_when=ALL_COMPLETED)
    r_redis.sadd(redis_tumblr_dir_saved, str(f_name[0]))


if __name__ == "__main__":
    if os.path.exists(url_resource) and os.path.isdir(url_resource):
        for i_file in (reversed(sorted(os.listdir(url_resource)))):
            current_file = i_file
            print(current_file)
            file_name = url_resource + current_file

            if r_redis.sismember(redis_tumblr_dir_saved,
                                 str(i_file)) or r_redis.sismember(redis_tumblr_dir_saved, str(file_name)):
                print("已经下载过 " + str(i_file))
            else:
                file_path = current_file.split('_')[0]
                init_list(file_name, file_path)
