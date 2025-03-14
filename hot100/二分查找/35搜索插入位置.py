from typing import *


"""
记：左开右闭，while用<，最后返回l
"""
class Solution:
    """
    同找到最左边的target
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l

    """
    提前返回版
    """
    def searchInsert1(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l




