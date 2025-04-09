from typing import *


"""
二分法
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        # 根号x不会超过x // 2（因为舍弃小数部分），所以+1使得右区间为开区间
        left, right = 1, x // 2 + 1
        while left < right:
            mid = (left + right) >> 1
            if mid * mid > x:
                right = mid
            else:  # mid * mid <= x
                left = mid + 1
        """
        循环结束的前一个循环中，一定走的是left = mid + 1，此时mid * mid <= x，那么left = mid + 1就是第一个平方大于x的数
        所以最后返回left - 1！
        """
        return left - 1

