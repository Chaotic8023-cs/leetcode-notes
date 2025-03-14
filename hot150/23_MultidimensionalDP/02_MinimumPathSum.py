# 64
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        """
        dp[i][j]表示走到ij需要的最小sum
        初始化：先初始化dp[0][0]， 即左上角的
        然后分别沿着第一行和第一列进行累加，因为第一行和第一列只能直着走
        遍历方向：因为只能往右和下走，所以我们从左往右从上往下遍历
        状态转移方程：dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        即选左边格子和上边格子最小的，加上当前格子的number就是当前格子最小的sum
        """
        dp[0][0] = grid[0][0]  # initialize top left corner first
        # Then assign sum cumulatively along first row/col
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                # current min sum = min sum from either top or left + current number
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    sol = Solution()
    print(sol.minPathSum(grid))

