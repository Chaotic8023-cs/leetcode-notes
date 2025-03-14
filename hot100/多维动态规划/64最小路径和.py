from typing import *


"""
动态规划：和#62不同路径思路一样，只是递推公式变了。
递推公式：此题dp[i][j]表示到grid[i][j]的最小路径和，因为ij是从左或上过来，所以就是左和上的最小路径和 + 当前格子的值。
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        s = 0
        for i in range(m):
            s += grid[i][0]
            dp[i][0] = s
        s = 0
        for j in range(n):
            s += grid[0][j]
            dp[0][j] = s
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]  # 两个过来的方向选路径和小的那个
        return dp[m - 1][n - 1]



