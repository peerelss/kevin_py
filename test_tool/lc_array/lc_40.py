import sys


class Solution:
    def jump(self, nums):
        nums[-1]=1
        re = [0] * len(nums)
        for i in reversed(range(0, len(nums) - 1)):
            temp_i =100000
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    if nums[i + j] > 0:
                        temp_i = min(temp_i, re[i + j] + 1)
            re[i] = temp_i
        print(nums)
        print(re)
        return re[0]


print(Solution().jump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))

'''
倒着算 数组长度为n
对第i个位置，到达结尾的（之考虑跳转一次（递归调用，所以之考虑一次））各种路径的可能性为
0-nums[i]  种，对于第j条路径，如果 j+nums[i+j]>n-i 则能到达 ，取最小值设置为nums[i]即可 
'''
