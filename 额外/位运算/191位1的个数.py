from typing import *


"""
每次看最右边的一位是不是1。
如何看n的最右边一位是否为1：用n和1做bitwise AND即可。
例如：
n = 111 -> n & 1 = 111 & 001 = 1，说明最右边是1
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n & 1
            n >>= 1
        return ans




