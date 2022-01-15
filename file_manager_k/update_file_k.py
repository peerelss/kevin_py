# -*- coding: UTF8 -*-
import os
import pymysql
import ntpath
import redis
import shutil

db = pymysql.connect(host='localhost',
                     user='test',
                     password='test1234',
                     database='test_file_manager')
int_type = 100 * 1024 * 1024
key_worlds = '地址'


def delete_by_key_world(key_worlds):
    args = '%' + key_worlds + '%'
    sql = 'select * from runoob_tbl where runoob_file_size > %d' % (int_type)
    # sql = "select * from runoob_tbl where runoob_file_name like '%s'  " % args
    sql_delete = "delete from runoob_tbl where runoob_file_name like '%s' " % args
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        name_ = str(row[1])
        name_abs = row[2]

        print('name = %s abs = %s ' % (row[1], row[2]))
        # os.remove(name_abs)
    cursor.close()


'''
    c = db.cursor()
    try:
        c.execute(sql_delete)
        db.commit()
    except:
        print('except')

    db.close()
'''


def delete_file_by_dir(dir_abs):
    args = dir_abs + '%'
    sql = "delete from runoob_tbl where runoob_file_name_abs like '%s'  " % args
    if os.path.isdir(dir_abs):
        shutil.rmtree(dir_abs)
        pass
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()


if __name__ == "__main__":
    delete_file_by_dir("/media/kevin/My Passport/ph/cmv00148")
    # delete_by_key_world(key_worlds)
