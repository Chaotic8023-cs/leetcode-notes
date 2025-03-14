# 66
from typing import *


class Solution:
    """
    Naive: 直接从右到左一位一位看
    优化方向：因为是加1，所以有进位的情况一定是9+1，也就是说如果进位一定是1
    所以可以从右往左给每个位置的数直接+1再对10求余，如果不为0则说明没有进位，直接返回
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] < 10:
            return digits
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            a = digits[i] + carry
            if a < 10:
                digits[i] = a
                carry = 0  # 重置carry，因为之后还要检查有没有carry，此处<10所以没没有carry了
                break
            digits[i] = a % 10
            carry = a // 10
        if carry:
            digits.insert(0, carry)
        return digits

    # 按上述优化过的，不用记
    class Solution:
        def plusOne1(self, digits: List[int]) -> List[int]:
            n = len(digits)
            for i in range(n - 1, -1, -1):
                digits[i] += 1
                digits[i] %= 10
                if digits[i] != 0:
                    return digits
            return [1] + digits


if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([9]))

