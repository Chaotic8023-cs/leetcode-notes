# 221
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ms = 0  # maximum area of square （初始最大面积设）
        dp = [[0]*n for _ in range(m)]
        """
        含义：
        dp[i][j]表示以matrix[i][j]为右下角的最大正方形的边长
        如果matrix[i][j]为0，则dp[i][j]为0，因为它不在任何一个正方形里
        如果只有一个空，同时那个空上数字为1，则它在dp里为1，因为它自己就是个
        正方形，边长为1
        状态转移方程：
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        我们需要看dp[i][j]的左边一格，上边一格，和左上对角一格。如果dp[i][j]能
        构成更大的一个正方形，则左、上、左上分别得保证底边、右侧边、左上方都在这个
        大正方形内，即这三个格子都是大正方形的边长减1。这三个中最小的那个决定了当前
        格子能组成的最大的正方形：
        比如最小的为0，即当前正方形只能是它自己，大小为1
        比如最小为1，说明三个方向只能保证1的长度，那么加上自己这格就能组成边长为2的正方形
        初始化：
        由于dp[i][j]要看左、上、左上三个格子，则需要初始化第一行和第一列
        遍历顺序：从第二行和第二列开始，顺序遍历完正个matrix，同时记录当前最大的面积
        """
        # 初始化，同时看第一行第一列又没有1，有的话初始最大面积设为1
        for j in range(n):
            if matrix[0][j] == "0":
                dp[0][j] = 0
            else:
                dp[0][j] = 1
                ms = 1
        for i in range(m):
            if matrix[i][0] == "0":
                dp[i][0] = 0
            else:
                dp[i][0] = 1
                ms = 1
        # 从第二行第二列开始顺序遍历
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    ms = max(ms, dp[i][j] ** 2)
        pprintdp(dp)
        return ms


if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
    sol = Solution()
    print(sol.maximalSquare(matrix))
