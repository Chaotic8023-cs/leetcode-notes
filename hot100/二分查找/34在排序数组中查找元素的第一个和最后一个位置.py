from typing import *


"""
记：找哪边就给哪边条件加=且除掉=的情况；左右分别返回left和left - 1
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftmost(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) >> 1
                if target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left if 0 <= left < len(nums) and nums[left] == target else -1

        def rightmost(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) >> 1
                if target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left - 1 if 0 <= left - 1 < len(nums) and nums[left - 1] == target else -1

        return [leftmost(nums, target), rightmost(nums, target)]





