from typing import *

"""
1. dp数组下标含义：dp[i][j]为到达坐标(i, j)的不同路径的个数
2. 递推公式：dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    因为只能往右和下走，所以到坐标(i, j)只能从左边和上边过来，即到达左边的方法加到达右边的方法之和
3. 初始化：因为每个位置要看左边和上边，所以我们初始化第一行和第一列
4. 遍历顺序：从第二行开始从左到右遍历，这样就能保证每个遍历到的dp数组位置左边和上边都有值
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]  # 初始化：第一行第一列都为1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]



