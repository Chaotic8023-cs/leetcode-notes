from typing import *


class Solution:
    """
    此题动态规划更直接：
    1. dp数组含义：dp[i]表示以i为结尾的最大子数组和，
    2. 初始化：dp[0]只有一个元素所以就是它本身。
    3. 状态转移：选最大
        1. 到前一个位置的最大子数组和加上当前元素
        2. 当前元素自己
    即我们看如果当前最大的子数组加上了当前元素更大了，则加上当前元素；如果加上了当前元素还没当前元素本身大（即当前最大子数组和为负），
    则抛弃当前最大的子数组，即结尾为i的最大子数组就是i一个元素。
    """
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

    """
    贪心：其实和dp的思路一样，只是换了种写法
    """
    def maxSubArray1(self, nums: List[int]) -> int:
        ans = -float('inf')
        curr_sum = 0
        for num in nums:
            # 如果当前sum（不算当前num）为正数我们就累加，否则抛弃
            if curr_sum >= 0:
                curr_sum += num
            else:
                curr_sum = num
            ans = max(ans, curr_sum)
        return ans




