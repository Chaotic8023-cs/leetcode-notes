from typing import *


"""
01背包：把和为s的数组分为等和的两部分，则相当于往一个s // 2的背包里放物品，看最后物品价值是否等于背包容量。此时nums中的每个数既是重量又是价值，如果
最后s // 2的背包重量 == 价值，说明nums中的一个子集的和为s // 2，那么剩下的数的和也是s // 2，也就说明等和子集存在。
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:  # 如果和不是2的倍数，那么一定不能分割出来两个等和的子集
            return False
        # 常规01背包做法，nums[i]既是重量又是价值
        capacity = s // 2
        dp = [[0] * (capacity + 1) for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            for j in range(capacity + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - nums[i - 1]] + nums[i - 1])
        return dp[len(nums)][capacity] == capacity  # 看价值是否等于背包容量，等于则说明这个选的这些数字的和为s // 2，那么剩余的数就是和为s // 2的另一个子集




