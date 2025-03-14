# 120
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*(i+1) for i in range(n)]
        """
        dp[i][j]表示走到triangle[i][j]的最小sum
        初始化：因为从上往下走，我们只需初始化三角的最上层一个即可
        遍历顺序：因为从上往下走，从第二层开始往下一层一层遍历
        状态转移方程：每当看dp[i][j]，由于从一层的i到下层只能到i或者i+1
        我们就先求能从上层过来的index：即j或者j-1，当然我们需要排除掉超出上层范围的index
        然后我们去最小的那个，再加上当前的triangle[i][j]即为当前位置的最小sum
        最后我们返回最后一层的最小的那个sum，即为path的终点
        """
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])):
                prev_idx = [j, j-1]  # indices come from previous level
                # need to remove indices out of range
                prev_min = min(dp[i-1][j] for j in prev_idx
                               if 0 <= j < len(triangle[i-1]))
                # current min = prev min + current value
                dp[i][j] = prev_min + triangle[i][j]
        # last level's min is the end point of the path
        return min(dp[n-1])


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    sol = Solution()
    print(sol.minimumTotal(triangle))

