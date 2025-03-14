from typing import *


"""
二刷：四数之和 -> 2个for加双指针
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums = sorted(nums)
        for i in range(n):
            if nums[i] > target and nums[i] > 0 and target > 0:  # i剪枝
                break
            if i - 1 >= 0 and nums[i] == nums[i - 1]:  # i去重
                continue
            for j in range(i + 1, n):
                if nums[i] + nums[j] > target and target > 0:  # j剪枝
                    break
                if j - 1 >= i + 1 and nums[j] == nums[j - 1]:  # j去重
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        # left, right去重
                        left, right = left + 1, right - 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
        return ans
