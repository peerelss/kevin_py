import os

import requests
from bs4 import BeautifulSoup
import sys

'''
url = 'https://66.media.tumblr.com/7c375d77501b7da572544db91c4475c6/tumblr_mgq4qqxWOL1r600xqo1_1280.jpg'

con = requests.get(url)
if con.history:
    print('fuck ')
else:
    print(con.status_code)

t_url = 'sexdoll-die-gummipuppe_json1.txt'
print(t_url.split('_')[0])
import  redis
r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
'''
file_length = 0


def get_file_length():
    global file_length
    with open(r"/media/kevin/Backup/txt_2/sexdoll-die-gummipuppe_json1.txt", 'r+') as myFile:
        read_file = myFile.read
        buffer = read_file(1024 * 1024)
        while buffer:
            file_length += buffer.count('\n')
            buffer = read_file(1024 * 1024)
    if (file_length != 0):
        file_length += 1
    print(str(file_length))


if __name__ == "__main__":
    # get_file_length()
    file_dir = '/media/kevin/Backup/tumblr(2)'
    if os.path.isdir(file_dir):
        file_list = os.listdir(file_dir)
        for f in file_list:
            print(str(f))
