class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)

        results = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                print(nums[i], nums[i - 1])
                continue
            print(str(i + 1))
            self.find_two_sum(nums, i + 1, len(nums) - 1, -nums[i], results)

        print(results)
        return results

    def find_two_sum(self, nums, left, right, target, results):
        last_pair = None
        while left < right:
            if nums[left] + nums[right] == target:
                if (nums[left], nums[right]) != last_pair:
                    results.append([-target, nums[left], nums[right]])
                last_pair = (nums[left], nums[right])
                right -= 1
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1


Solution().threeSum([-100, -2, -2, -1, -1, -1, 0, 0, 0, 1, 1, 2, 2, 4])
