from typing import *


"""
利用#191的方法，计算设置位的个数，即1的个数。
2的幂都是"1000..."的形式，只要设置位的个数等于1，说明就是2的幂
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cnt = 0
        while n > 0:
            cnt += 1
            n &= n - 1
        return cnt == 1
        









