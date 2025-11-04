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


"""
改编：要求返回数组
"""
class Solution1:
    def maxSubArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [[0, 1] for _ in range(n)]  # dp[i][0]存最大和，dp[i][1]存以i为结尾的最大和的子数组的长度（默认为1）
        dp[0][0] = nums[0]
        max_sum, max_idx, max_l = nums[0], 0, 1  # 记录一个全局最大：最大和、最大和出现的位置（结尾）、最大和数组的长度
        for i in range(1, n):
            if dp[i - 1][0] + nums[i] > nums[i]:  # 若和前面连上更大
                dp[i][0] = dp[i - 1][0] + nums[i]
                dp[i][1] = dp[i - 1][1] + 1  # 当前最大和子数组的长度 = 前半部分的长度 + 1
            else:  # 否则最大和就是nums[i]，此时不更新最大和数组长度，因为默认就是1
                dp[i][0] = nums[i]
            # 遍历时就统计全局最大
            if dp[i][0] > max_sum:
                max_sum = dp[i][0]
                max_idx = i
                max_l = dp[i][1]
        # print(f"max_sum: {max_sum}, arr: {nums[max_idx - max_l + 1:max_idx + 1]}")
        return nums[max_idx - max_l + 1:max_idx + 1]  # 最后我们知道最大子数组出现的位置（结尾，即max_idx），和长度，于是往前推就能得到最大的子数组了


# 上面Solution1的简化版：初始化时直接每个位置初始化成 nums[i]，这样遍历的时候就不用else专门赋值了；同时，不用单独记录max_l，因为最后可以直接从 dp[max_idx][1] 取得
class Solution2:
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


# 记录最大和和长度的dp数组分开的写法
class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[i] for i in range(n)]
        l = [1] * n  # 记录每个下标的最大和对应的子数组长度
        dp[0] = nums[0]
        max_sum, max_idx = nums[0], 0
        for i in range(1, n):
            if dp[i - 1] + nums[i] > nums[i]:
                dp[i] = dp[i - 1] + nums[i]
                l[i] = l[i - 1] + 1
            if dp[i] > max_sum:
                max_sum = dp[i]
                max_idx = i
        return sum(nums[max_idx - l[max_idx] + 1:max_idx + 1])