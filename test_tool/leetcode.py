class Solution(object):
    def get_nums_by_tar(self, con, target, temp, an, re):
        if target == 0:
            print(an)
            re.append(an[:])
            return
        elif target < 0:
            return
        else:
            for i in range(temp, len(con)):
                if i > temp and con[i] == con[i - 1]:
                    i = i + 1
                else:
                    an.append(con[i])
                    self.get_nums_by_tar(con, target - con[i], i + 1, an, re)
                    an.pop(-1)

    def combinationSum2(self, candidates, target):
        cons = sorted(candidates)
        ans = []
        res = []
        self.get_nums_by_tar(cons, target, 0, ans, res)
        return res


print(Solution().combinationSum2([1, 1, 2, 2, 5, 6, 6, 7], 8))
'''
还是考虑使用动态规划解决此题目
对于第n项，可以表示为现有n-1项的和
'''
