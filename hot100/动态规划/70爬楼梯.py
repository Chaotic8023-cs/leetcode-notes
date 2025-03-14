from typing import *


"""
动态规划：
dp[i]：爬i阶楼梯有几种方法
递推公式：dp[i] = dp[i - 2] + dp[i - 1]
    爬i-2阶的方法（然后一次爬两阶）+爬i-1阶的方法（然后一次爬一阶）。爬的2阶或1阶是算作前面所有方法的最后一步，所以没有+1。
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)  # 1-index
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]





