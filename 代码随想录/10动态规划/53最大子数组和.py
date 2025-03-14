from typing import *


"""
动态规划：这题很直接，就是如果以前一个为结尾的子数组和为负数了（对当前元素做负贡献），我们就舍弃。
1. dp数组下标含义：dp[i]为以i为结尾（包含）的最大子数组和
2. 递推公式：dp[i] = max(dp[i - 1] + nums[i], nums[i])
    如果以前一个元素i-1的最大子数组和都为负数了，那么以当前结尾的最大子数组和就是当前元素一个
3. 初始化：dp[0] = nums[0]
4. 遍历顺序：正序遍历
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

    """
    常规for循环做法，和dp思路其实一样，用curr_sum记录当前的子数组和，如果小于0则抛弃
    """
    def maxSubArray1(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        ans = curr_sum
        n = len(nums)
        for i in range(1, n):  # 从第二个元素开始，因为测试样例有仅1个元素的数组
            if curr_sum < 0:  # 一定是加当前元素i之前判断是否抛弃
                curr_sum = 0
            curr_sum += nums[i]
            ans = max(ans, curr_sum)
        return ans




