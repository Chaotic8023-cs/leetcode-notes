# 50
from typing import *


class Solution:
    """
    快速幂算法：
    我们不直接连乘（OlogN）,而是用分治法，每次算指数为n // 2的结果，最后答案就是两个乘起来
    注意，指数可能为负，所以多加一个n = -1的base case来处理
    列如：myPow(2, -3):
        1. 1st call  myPow(2, -3)
        2. 2nd call myPow(2, -2)，因为-3 // 2 = -2余1
        3. 3rd call myPow(2, -1)，因为-2 // 2 = -1余0（base case）
        然后从base case返回 2nd call，2^-1 = 0.5，此时n是-2为偶数，所以结果就是乘起来，即2^-1 * 2^-1 = 2 ^ -2
        然后返回到1st call，此时n是-3为奇数，所以最终的结果就是乘起来再乘x，即2^-2 * 2^-2 * 2 = 2^-2 * 2^-2 * 2^1 = 2^-3
    """
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return 1.0 / x
        y = self.myPow(x, n >> 1)  # n >> 1即right shift一位，也就是integer division by 2
        # n & 1能得最右边的bit，即如果1为奇数，0为偶数
        return y * y if n & 1 == 0 else y * y * x


if __name__ == '__main__':
    sol = Solution()
    print(sol.myPow(2, -3))
