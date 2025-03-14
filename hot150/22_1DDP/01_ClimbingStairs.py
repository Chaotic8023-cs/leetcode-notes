# 70
from typing import *


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [0] * n  # dp[i]表示爬i+1节楼梯的方法
        dp[0] = 1  # 爬1节楼梯有1种方法
        dp[1] = 2  # 爬2节楼梯有2种方法
        """
        爬三节楼梯的话，可以看成从从之前的节数走一步的来，
        即从1节爬1次（2节），或从2节爬1次（1节）
        所以爬三节的爬法等于爬一节的爬法加上爬2节的爬法
        """
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]


if __name__ == '__main__':
    n = 2
    sol = Solution()
    print(sol.climbStairs(n))


