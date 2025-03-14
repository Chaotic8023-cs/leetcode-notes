# 63
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        """
        和#62 UniquePath一样，只是加上了额外检查，
        如果上面一格为障碍，则不加上面的（设为0），左边同理
        """
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:  # skip obstacles
                    continue
                # only add #paths from non-obstacle cells
                top = dp[i-1][j] if obstacleGrid[i-1][j] != 1 else 0
                left = dp[i][j-1] if obstacleGrid[i][j-1] != 1 else 0
                dp[i][j] = top + left
        return dp[m-1][n-1]


if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid))

