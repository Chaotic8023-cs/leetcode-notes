# 509
from typing import *


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        fibs = [0] * (n+1)
        fibs[0] = 0
        fibs[1] = 1
        for i in range(2, n+1):
            fibs[i] = fibs[i-1] + fibs[i-2]
        print(fibs)
        return fibs[n]


if __name__ == '__main__':
    n = 0
    sol = Solution()
    print(sol.fib(n))
