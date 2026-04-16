from typing import *
from math import inf



"""
由于答案恰好只有一组，所以和三数之和一样使用三指针，只是维护一个最小diff。
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        min_diff, ans = inf, 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # 同样的，由于进行了排序了，可以跳过重复的i
                continue
            l, r = i + 1, n - 1
            while l < r:
                # 每次都比较
                s = nums[i] + nums[l] + nums[r]
                diff = abs(s - target)
                if diff < min_diff:
                    min_diff = diff
                    ans = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:  # 如果s == target，则是唯一解，直接返回
                    return target
        return ans



