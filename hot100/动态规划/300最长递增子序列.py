from typing import *


"""
动态规划：
dp[i]：以i为结尾（包含）的最长递增子序列的长度
递推公式：遍历所有i前面的下标j，如果nums[i] > nums[j]，则以j结尾的递增子序列就可以加上nums[i]。对于所有前面的位置j，我们取max。
初始化：一开始每个位置最长的递增子序列就是它自己，即长度 = 1
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)





