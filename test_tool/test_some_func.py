# -*- coding: UTF8 -*-
import os
import cmath


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


r = []


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


if __name__ == '__main__':
    get_nums_by_target([2, 3, 6, 7], 7)
