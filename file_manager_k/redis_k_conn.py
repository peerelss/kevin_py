import redis
import os

'''
set_name = 'redis_file_dir_history'  # 记录已经扫描过得文件夹历史
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.sadd(set_name, 'example')
print(r.smembers(set_name))

file_name = '/media/kevin/My Passport/movies/北条麻妃/empty'
str_end = os.path.splitext(file_name)[-1][1:]
print(str_end)
'''
filepath = '/media/kevin/My Passport'
if os.path.isdir(filepath):
    for root, files_, dirs_ in os.walk(filepath):
        if not os.listdir(root):
            print(root)
            os.rmdir(root)
