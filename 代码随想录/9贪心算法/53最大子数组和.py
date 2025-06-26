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


# 要求返回子数组
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # 观察普通dp的递推公式，这里我们直接给每个位置的最大和初始化成 nums[i]，长度初始化为1，这样只需要进行 dp[i - 1][0] + nums[i] > nums[i] 一次比较！
        dp = [[nums[i], 1] for i in range(n)]  # [以i为结尾的最大子数组和，以i为结尾的最大和子数组的长度]
        max_sum, max_idx = nums[0], 0
        for i in range(1, n):
            if dp[i - 1][0] + nums[i] > nums[i]:
                dp[i][0] = dp[i - 1][0] + nums[i]
                dp[i][1] = dp[i - 1][1] + 1
            if dp[i][0] > max_sum:
                max_sum = dp[i][0]
                max_idx = i
        max_len = dp[max_idx][1]
        return sum(nums[max_idx - max_len + 1:max_idx + 1])  # 拥有最大和的子数组就是 nums[max_idx - max_len + 1:max_idx + 1]



