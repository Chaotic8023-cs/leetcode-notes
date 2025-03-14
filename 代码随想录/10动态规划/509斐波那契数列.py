from typing import *


class Solution:
    """
    动态规划
    """
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]

    """
    递归
    """
    def fib1(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)





