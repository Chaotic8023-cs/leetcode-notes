from typing import *

"""
动态规划：如果当前累计和dp[i - 1]是负数，即对当前的nums[i]做负贡献，那么就舍弃前面的累计和，只保留当前的nums[i]
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)




