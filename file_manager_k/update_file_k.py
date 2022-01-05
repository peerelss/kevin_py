# -*- coding: UTF8 -*-
import os
import pymysql
import ntpath
import redis

db = pymysql.connect(host='localhost',
                     user='test',
                     password='test1234',
                     database='test_file_manager')
int_type = 4
key_worlds = '隨時'
args = '%' + key_worlds + '%'
# sql = 'select * from runoob_tbl where file_type > %d' % (int_type)
sql = "select * from runoob_tbl where runoob_file_name like '%s'  " % args
sql_delete = "delete from runoob_tbl where runoob_file_name like '%s' " % args
cursor = db.cursor()
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    name_ = str(row[1])
    name_abs = row[2]

    print('name = %s abs = %s ' % (row[1], row[2]))
    os.remove(name_abs)
cursor.close()

c = db.cursor()
try:
    c.execute(sql_delete)
    db.commit()
except:
    print('except')

db.close()
