import pymysql
import redis

set_name = 'redis_file_dir_history'  # 记录已经扫描过得文件夹历史
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

db = pymysql.connect(host='localhost',
                     user='test',
                     password='test1234',
                     database='test_file_manager')

cursor = db.cursor()
sql = "insert into runoob_tbl(runoob_file_name,runoob_file_name_abs,runoob_file_size,runoob_des,file_type)values " \
      "(%s, %s,%s, %s, %s)"
cursor.execute(sql, ('name', 'abss', 40, 'dess', 2))
db.commit()
db.close()
