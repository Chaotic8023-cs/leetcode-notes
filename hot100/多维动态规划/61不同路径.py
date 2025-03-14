from typing import *


"""
动态规划：
还是爬楼梯方法个数的思想，由于是只能往下和往右，所以dp[i][j]只能从上和左推出来。
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # 从上和左推出来
        return dp[m - 1][n - 1]





