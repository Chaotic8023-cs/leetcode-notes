# 62
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        """
        dp[i][j]表示到达(i, j)的不同路径数
        因为只能向右或向下走，(i, j)只能从上边一格或左边一格过来
        即到达(i, j)的路径数等于上边一格的加上左边一格子的
        状态转移方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        初始化：因为需要上和左，我么就初始化dp matrix的第一行和第一列，都是1
        因为走到第一行或第一列只有一种走法！
        遍历顺序：根据状态转移方程，我们可以按照从左往右从上到下的方式遍历
        """
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        pprintdp(dp)
        # return the bottom right corner, which is the END of the matrix
        return dp[m-1][n-1]


if __name__ == '__main__':
    m = 3
    n = 2
    sol = Solution()
    print(sol.uniquePaths(m, n))