from typing import *


"""
动态规划：此题和一般子串子序列问题dp含义略有不同，一般的含义为以i为结尾及j为结尾，这里因为是两个且求的是非连续子序列，所以
定义dp[i][j]：text1[0, i]和text2[0, j]中最长的连续子序列的长度。注意，这里再是以ij为结尾，而是从0到ij
递推公式：#718最长重复子数组的基础上多了一条
    1. 如果text1[i] == text2[j]：都回退1格再+1，同#718。
    2. 如果text1[i] != text2[j]：各回退一格中取max。因为#718子数组是连续的，且定义是以ij为结尾，所以不相等的话长度就是0；此题
        因为不连续，不相等时还得继承前面已经有的相同子序列的长度，所以需要处理ij不相等的情况。
初始化：初始化也略微有所不同，因为此时dp定义是0到ij，所以初始化第一行和第一列的时候，只要一相等更新长度为1后，后面的下标都要继承这个1。
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        # 初始化
        for i in range(m):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            elif i > 0 and text1[i] != text2[0]:
                dp[i][0] = dp[i - 1][0]
        for j in range(n):
            if text2[j] == text1[0]:
                dp[0][j] = 1
            elif j > 0 and text2[j] != text1[0]:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  # 都回退一格
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 由于非连续，所以前半部分的非连续子序列也得算上，所以是从各回退一格中取max
        # 因为dp含义变成[0,i]和[0,j]范围内的最长重复子序列了，所以直接返回dp[m - 1][n - 1]
        return dp[m - 1][n - 1]








