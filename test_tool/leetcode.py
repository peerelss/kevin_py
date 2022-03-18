class Solution(object):
    result = []
    r = []

    def get_nums_by_tar(self, con, target):
        if target == 0:
            print(self.r)
            self.result.append(self.r[:])
            return
        elif target < 0:
            return
        for i in range(0, len(con)):
            self.r.append(con[i])
            self.get_nums_by_tar(con[i:], target - con[i])
            self.r.pop(-1)

    def combinationSum(self, candidates, target):
        self.get_nums_by_tar(candidates, target)
        print(self.result)


Solution().combinationSum([2, 3, 6, 7], 7)
