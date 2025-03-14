from typing import *


"""
二刷：三数之和 -> 1个for加双指针
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = []
        for i in range(n):
            if nums[i] > 0:  # i剪枝
                break
            if i - 1 >= 0 and nums[i] == nums[i - 1]:  # i去重
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    # left, right去重
                    left, right = left + 1, right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
        return ans



