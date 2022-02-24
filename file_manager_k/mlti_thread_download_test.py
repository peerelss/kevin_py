# -*- coding: UTF8 -*-
from concurrent.futures import ThreadPoolExecutor
import requests
import os
import redis

'''
每一个文件的下载链接全部完成之后再开启下一个任务
'''
