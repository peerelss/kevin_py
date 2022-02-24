# -*- coding: UTF8 -*-
'''
指定文件夹，
    打开txt文件 resource.txt
        从文件名生成文件夹名 resource
    按行读取，生成文件名  http：// tumblr.jpg 生成 tumblr.jpg
        如果被重定向，则不下在 history
        否则保存
'''
import redis

# redis 相关的关键字
r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_tumblr_dir_saved = "redis_set_tumblr_dir"  # 保存所有已经下载过的tumblr的txt的文件名


def init_list():
    list_s = [
        'japanesebdsmofficial_json1.txt',
        'jeanpaulfour_json1.txt',
        'jesseflanagan_json1.txt',
        'jolinaheavyrubberdoll_json1.txt',
        'justanotherhic_json1.txt',
        'k7nky - paul_json1.txt',
        'kastortroyncage_json1.txt'
    ]
    for i in list_s:
        r_redis.srem(redis_tumblr_dir_saved, i)


if __name__ == "__main__":
    init_list()
