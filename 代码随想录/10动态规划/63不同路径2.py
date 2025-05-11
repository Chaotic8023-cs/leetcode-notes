from typing import *


"""
1. dp数组下标含义：dp[i][j]为到达坐标(i, j)的不同路径的个数
2. 递推公式：同62不同路径，但是要判断是否左边和上边有障碍物，有的话对应的方向就为0
3. 初始化：重点！此题起点和终点上都可能有障碍物，所以一开始全部先初始化成0。然后我们初始化第一行和第一列，此时如果遇到第一个障碍物则它后边的
    所有格子都为0
4. 遍历顺序：同62不同路径
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        # 初始化：第一行和第一列中，到第一个石头前全是1，剩下位置都是0
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        # 遍历
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:  # 遇到石头直接跳过就行，这样石头的dp值为0，相当于其它格子从石头不能过来
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]



