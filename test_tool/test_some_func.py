# -*- coding: UTF8 -*-
import os
import cmath
import redis

# 连续子序列最大和

def l_lts(nums):
    n = len(nums)
    ll = [1] * n
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                ll[i] = max(ll[i], ll[j] + 1)
    return max(ll)


# 1,暴力求解
def get_max_sum(nums):
    l = len(nums)
    max_sum = nums[0]
    for i in range(0, l - 1):
        for j in range(i + 1, l):
            sum = 0
            for k in range(i, j):
                sum = sum + nums[k]
            max_sum = max(max_sum, sum)
            # print(str(sum))
    return max_sum


# 2，尝试用动态规划/递归 寻找以第L结尾的最大值
def get_m_sum(nums):
    for i in range(1, len(nums)):
        nums[i] = max(nums[i - 1], 0) + nums[i]
    return max(nums)


def get_nums_by_tar(con, target):
    if target == 0:
        print(r)
        return
    elif target < 0:
        return
    for i in range(0, len(con)):
        r.append(con[i])
        get_nums_by_tar(con[i:], target - con[i])
        r.pop(-1)


def get_nums_by_target(candidates, target):
    get_nums_by_tar(candidates, target)
import redis

# 创建一个redis sorted set 来保存所有的文件类型
sorted_set_type_name = 'redis_file_type_kevin_6'
set_name = 'redis_file_dir_history'  # 记录已经扫描过得文件夹历史
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

if __name__ == '__main__':
    file_dir=r'C:\Users\kevin\Downloads\tumblr_txt_all3'
    if os.path.exists(file_dir):
        for f in sorted(os.listdir(file_dir)):
            print(f)
