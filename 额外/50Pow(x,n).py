from typing import *


"""
快速幂：2 ^ 8 = 2 ^ (4 + 4) = 2 ^ 4 * 2 ^ 4, 2 ^ 9 = 2 ^ (4 + 4 + 1) = 2 * 2 ^ 4 * 2 ^ 4
即x ^ n = 
    1. n为偶数：x ^ (n // 2) * x ^ (n // 2)
    2. n为奇数：x * x ^ (n // 2) * x ^ (n // 2)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:  # 应对负数幂
            return 1 / x
        y = self.myPow(x, n >> 1)
        if n & 1:  # 二进制下最右边一位是1，即奇数
            return x * y * y
        else:  # 偶数
            return y * y





