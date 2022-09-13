# -*- coding: UTF8 -*-
import pymongo
import redis

'''
1.从数据库读取女优所有非合计的作品（参演人数<=4)，获取番号
2.从本地搜索番号 
    2.1 使用everything sdk搜索。如果结果里有文件且文件较大，则视为已存在，如果不存在，则输出番号

'''