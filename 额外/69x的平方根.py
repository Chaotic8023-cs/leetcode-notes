from typing import *


"""
二分法
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:  # 处理x=1的情况
            return x
        left, right = 0, x // 2 + 1
        while left < right:
            mid = (left + right) >> 1
            if mid ** 2 <= x:
                left = mid + 1
            else:
                right = mid
        """
        循环结束的前一个循环中，一定走的是left = mid + 1，此时mid * mid <= x，那么left = mid + 1就是第一个平方大于x的数
        所以最后返回left - 1！
        """
        return left - 1

