import redis
import os

r_redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
redis_str_tumblr_file_name_k_conn = 'redis_str_tumblr_file_name_k_conn'
redis_deplicate_file_count_python = 'redis_deplicate_file_count_python'
'''
set_name = 'redis_file_dir_history'  # 记录已经扫描过得文件夹历史
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.sadd(set_name, 'example')
print(r.smembers(set_name))

file_name = '/media/kevin/My Passport/movies/北条麻妃/empty'
str_end = os.path.splitext(file_name)[-1][1:]
print(str_end)
'''
filepath = '/media/kevin/Backup/images/'


def delete_the_same_file():
    if os.path.isdir(filepath):
        for i_file in os.listdir(filepath):
            # print(i_file)
            i_file_full = os.path.join(filepath, i_file)
            if os.path.isdir(i_file_full):
                for ii_file in os.listdir(i_file_full):
                    str_ii_file = str(ii_file)  # 文件名
                    ii_file_full = str(os.path.join(i_file_full, ii_file))  # 文件路径
                    if 'tumblr' in str_ii_file:
                        if r_redis.exists(str_ii_file):
                            if r_redis.get(str_ii_file) == ii_file_full:
                                pass
                            else:
                                print('different one')
                                print(ii_file_full)
                                print(r_redis.get(str_ii_file))
                                if os.path.exists(r_redis.get(str_ii_file)):
                                    print('exists')
                                    r_redis.incr(redis_deplicate_file_count_python)
                                    os.remove(ii_file_full)

                        else:
                            r_redis.set(str_ii_file, ii_file_full)


# /media/kevin/Backup/images/61zonevacbed/tumblr_od1d2frNia1rrho82o1_1280.jpg
def delete_test(file_full_path):  # 删除此文件夹下所有未下载完毕的文件
    list_dir = os.listdir(file_full_path)
    for f_file in list_dir:
        f_file_path = os.path.join(file_full_path, f_file)


if __name__ == "__main__":
    # delete_the_same_file()
    # delete_test()
    print(r_redis.get('redis_set_tumblr_dir_file_redirected_incr'))
    if (9999 + 1) % 1000 == 0:
        print('00')
