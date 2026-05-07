from typing import *


"""
典型记忆化搜索

直接每个位置dfs暴力会超时，所以需要记忆:
dp[i][j]: 以ij为起点的递增最长路径长度
同时我们注意到，搜索过程只需往更大的数走，不会重复，所以根本不需要visited。
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j):
            if dp[i][j] > 0:  # 如果算过，直接返回
                return dp[i][j]
            # 当前开始算自身1个
            ans = 1
            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                # 往更大的数搜索
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[i][j]:
                    ans = max(ans, 1 + dfs(nx, ny))
            dp[i][j] = ans  # 记忆
            return ans

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans
            


