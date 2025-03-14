# 09
from typing import *


class Solution:
    """
    从数字直接入手
    我们想办法把x的后半部分进行反转，来和x的前半部分进行比较：
    初始化y为0，每次取x的末尾一个数，即用x % 10，来加到y里面，
    一直循环直到y == x或y > x
    例子：
    1. 1221
        iter1: x = 122, y = 1
        iter2: x = 12, y = 12 (x == y)
    2. 12521
        iter1: x = 1252, y = 1
        iter2: x = 125, y = 12
        iter3: x = 12, y = 125 (x = y // 10)
    """
    def isPalindrome(self, x: int) -> bool:
        # 小于0的和个位数为0的正整数一定不是回文
        if x < 0 or (x and x % 10 == 0):
            return False
        # 反转x的后面的数字和前面的进行比较
        y = 0
        while y < x:
            last_x_digit = x % 10
            y = y * 10 + last_x_digit  # 每次先给y×10再加个位数，就不用额外存一个power来记录当前应该是10的几次方了
            x //= 10
        return x == y or x == y // 10

    # Naive: 直接转成string做
    def isPalindrome1(self, x: int) -> bool:
        x = str(x)
        left, right = 0, len(x) - 1
        while left < right:
            if x[left] != x[right]:
                return False
            left, right = left + 1, right - 1
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(0))