from typing import *


"""
思路：拿mid和nums[0]比较，把数组分为两部分：如果mid大，则[0,mid]单增，反之[mid + 1:]单增。因为我们单独把mid拿出来做比较，所以
两部分是[0,mid)和(mid:len(nums) - 1]。
先二分然后看target是不是mid，如果不是就用mid和nums[0]作比较，如果nums[0] <= nums[mid]则[0, mid)单增，反之(mid:]单增。在两种单增区间内
再分两种情况，一个是在单增区间内，一个是不在，比较时一边的端点都用mid但不不含mid（因为mid一开始就看等不等于target了）。
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:  # [0, mid)单增：注意，这里条件要加=！
                if nums[0] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:  # (mid:]单增
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid
        return -1





