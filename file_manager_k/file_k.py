# -*- coding: UTF8 -*-
import os
import pymysql
import ntpath
import redis

# 创建一个redis sorted set 来保存所有的文件类型
sorted_set_type_name = 'redis_file_type_kevin_6'
set_name = 'redis_file_dir_history'  # 记录已经扫描过得文件夹历史
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

db = pymysql.connect(host='localhost',
                     user='test',
                     password='test1234',
                     database='test_file_manager')

'''for root, dirs, files in os.walk('/media/kevin/My Passport/down115', topdown=False):
    if not files and not dirs:
        os.rmdir(root)
        #print(root)'''
allpath = []
rootdir = "/media/kevin/My Passport"

video_0 = {'avi', 'mp4', 'mpg', 'wmv'}
image_1 = {'jpg', 'png', 'gif'}
txt_2 = {'txt'}
html_3 = {'html', 'htm'}
torrent_4 = {'torrent'}
soft_5 = {'exe'}

type_list_known = ['avi', 'mp4', 'mpg', 'wmv', 'jpg', 'png', 'gif', 'txt', 'html', 'htm', 'torrent', 'ext']


def getallfile(path):
    if r.sismember(set_name, path):
        print(" 文件夹已被扫描 %s" % (path))
        return
    allfilelist = os.listdir(path)
    # 遍历该文件夹下的所有目录或者文件
    for file_1 in allfilelist:
        filepath = os.path.join(path, file_1)
        # 如果是文件夹，递归调用函数
        if os.path.isdir(filepath):

            for root, files_, dirs_ in os.walk(filepath):
                if not files_ and not dirs_:
                    print(root)
                    os.rmdir(root)
                else:
                    getallfile(filepath)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(filepath):
            print(filepath)
            if filepath.endswith('url') or filepath.endswith('cfg'):
                os.remove(filepath)
            else:
                insert_file_info_to_db(filepath)
            # allpath.append(filepath)
    r.sadd(set_name, path)
    print('add to set %s' % (path))
    # print(allpath)


def get_type_from_name(name):
    if not '.' in str(name):
        return -1
    str_end = os.path.splitext(name)[-1][1:]
   # r.sadd(sorted_set_type_name, str_end)
    if str_end in video_0:
        return 0
    elif str_end in image_1:
        return 1
    elif str_end in txt_2:
        return 2
    elif str_end in html_3:
        return 3
    elif str_end in torrent_4:
        return 4
    return 5


# 将文件信息插入数据库  文件名（非空），文件路径（非空）,文件大小，描述，文件类型
# 0-视频，1-图片 2-txt
def insert_file_info_to_db(file_abs):
    sql = "insert into runoob_tbl(runoob_file_name,runoob_file_name_abs,runoob_file_size,runoob_des,file_type)values " \
          "(%s, %s,%s, %s, %s)"
    str_file = os.path.basename(file_abs)
    # print(str_file)
    int_file_size = os.path.getsize(file_abs)
    # print(str(int_file_size))
    int_file_type = get_type_from_name(str_file)
    # print(str(int_file_type))
    # print('\n')
    val_sql = (str_file, file_abs, int_file_size, os.path.dirname(file_abs), int_file_type)
    cursor = db.cursor()
    try:
        cursor.execute(sql, val_sql)
        db.commit()
    except:
        print('except')
        db.rollback()
    cursor.close()


if __name__ == "__main__":
    getallfile(rootdir)
    # insert_file_info_to_db('/media/kevin/My Passport/movies/北条麻妃/SVDVD-138.mp4')
