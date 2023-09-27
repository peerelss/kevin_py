import json
import sys
import requests
import os
from bs4 import BeautifulSoup
import pymongo
import redis

r_path = 'L:\chromedown'
momj = 'https://pics.vpdmm.cc/digital/video/18momj00217/18momj00217pl.jpg'
sprd = 'https://pics.vpdmm.cc/digital/video/18sprd01531/18sprd01531pl.jpg'

if __name__ == '__main__':
    index = ''
    for i in range(1, 1532):
        if i < 10:
            index = '000' + str(i)
        elif i < 100:
            index = '00' + str(i)
        elif i < 1000:
            index = '0' + str(i)
        else:
            index = str(i)
        print('https://pics.vpdmm.cc/digital/video/18sprd0' + index + '/18sprd0' + index + 'pl.jpg')
