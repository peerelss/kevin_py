# -*- coding: UTF8 -*-
'''
指定文件夹，
    打开txt文件 resource.txt
        从文件名生成文件夹名 resource
    按行读取，生成文件名  http：// tumblr.jpg 生成 tumblr.jpg
        如果被重定向，则不下在 history
        否则保存
'''
import requests
import os
import redis

url_resource = '/media/kevin/Backup/tumblr(2)'
url_target = '/media/kevin/Backup/images/'

# redis 相关的关键字
r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir = "redis_set_tumblr_dir"  # 保存所有已经下载过的tumblr的txt的文件名
redis_tumblr_dir_file_redirected = 'redis_set_tumblr_dir_file_redirected'  # 保存所有被重定向的url
redis_tumblr_dir_file_from_url = 'redis_set_tumblr_dir_file'  # 保存所有已被下载的url
redis_tumblr_dir_file_redirected_incr = 'redis_set_tumblr_dir_file_redirected_incr'  # 记录多少个被重定向


def get_url_from_file(t_tumblr):
    file_length = get_file_length(url_resource + '/' + t_tumblr)
    file_dir_name = str(t_tumblr).split('_')[0]
    if os.path.exists(url_target + file_dir_name):
        pass
    else:
        os.mkdir(url_target + file_dir_name)
    print(file_dir_name)
    temp = 0
    f = open(url_resource + '/' + t_tumblr, 'r')
    lines = f.readlines()

    for line in lines:
        temp = temp + 1
        str_line = str(line).replace('\n', '')
        if 'tumblr' in str_line:
            print('%s 一共 %d 行,当前 %d ' % (file_dir_name, file_length, temp))
            download_tumblr_jpg(str_line, file_dir_name)
    r_redis.sadd(redis_tumblr_dir, t_tumblr)
    f.close()


def download_tumblr_jpg(*jpg_url):
    file_name_t = str(jpg_url[0]).split('/')[-1]  # 文件名
    file_name_full = url_target + jpg_url[1] + '/' + file_name_t
    if r_redis.exists(file_name_t) and os.path.exists(r_redis.get(file_name_t)):
        print('%s 存在 from disk ' % file_name_t)
    elif r_redis.sismember(redis_tumblr_dir_file_from_url, file_name_t):
        print('%s 经被下载过 ' % jpg_url[0])
    elif r_redis.sismember(redis_tumblr_dir_file_redirected, file_name_t) or r_redis.sismember(
            redis_tumblr_dir_file_redirected, jpg_url[0]):
        print('%s  已经被重定向 from redis' % jpg_url[0])
        r_redis.incr(redis_tumblr_dir_file_redirected_incr)
    elif os.path.exists(file_name_full) or os.path.exists(
            file_name_full.replace('daddywantskitten0', 'daddywantskitten')):
        print('%s 已存在' % jpg_url[0])
    else:
        html = requests.get(jpg_url[0])
        if html.history:
            print('%s  已经被重定向 from network' % jpg_url[0])
            r_redis.incr(redis_tumblr_dir_file_redirected_incr)
            r_redis.sadd(redis_tumblr_dir_file_redirected, file_name_t)
        else:
            with open(file_name_full, "wb") as file:
                file.write(html.content)
            print('%s  正在下载ing  from network' % jpg_url[0])
            r_redis.sadd(redis_tumblr_dir_file_from_url, file_name_t)
            r_redis.sadd(redis_tumblr_dir_file_from_url, jpg_url[0])
            r_redis.set(file_name_t, file_name_full)


def get_file_length(file):
    file_length = 0
    with open(file, 'r+') as myFile:
        read_file = myFile.read
        buffer = read_file(1024 * 1024)
        while buffer:
            file_length += buffer.count('\n')
            buffer = read_file(1024 * 1024)
    if file_length != 0:
        file_length += 1
    myFile.close()
    print(str(file_length))
    return file_length


if __name__ == "__main__":
    if os.path.isdir(url_resource):
        t_file = os.listdir(url_resource)
        for t in t_file:
            if str(t).endswith('txt') and ('json' in str(t) or 'tumblr' in str(t)):
                print(str(t))

                if r_redis.sismember(redis_tumblr_dir, str(t)):
                    print("已经下载过")
                else:
                    get_url_from_file(str(t))
