from typing import *


class Solution:
    """
    贪心：因为尽可能大，所以我们只能做减法，但是前面减的话那就减大了，所以我们从后往前遍历做减法。如果第i个比第i-1个小，因为只能做减法，
    所以此时就算把第i个减到0还是比第i-1个小，所以我们干脆把i-1位上减1同时第i位变成9（相当于原数减去对10^n求余然后再减1，n从1一直递增）。
    例如：321
        第一次看，321中1比2小 -> 变为319
        第二次看，319中1比3小 -> 变为299
    """
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = str(n)
        for i in range(len(s) - 1, 0, -1):
            if s[i] < s[i - 1]:
                n -= n % (10 ** (len(s) - i)) + 1  # 前一位-1，当前位变为9
                s = str(n)
        return n

    """
    直接进行运算，不转str。记上面那个，好记！
    """
    def monotoneIncreasingDigits1(self, n: int) -> int:
        # 先统计n的位数
        nums_digits, i = 0, 1
        x = n
        while x > 0:
            x //= 10
            nums_digits += 1
            i += 1
        # 然后从后往前看nums_digits - 1次，即两位两位进行比较
        for i in range(1, nums_digits):
            if (n % (10 ** i)) // (10 ** (i - 1)) < (n % (10 ** (i + 1))) // (10 ** i):  # 如果后面那位比前面那位小
                n -= (n % (10 ** i)) + 1  # 前一位-1，后一位变9
                i += 1
        return n


if __name__ == '__main__':
    sol = Solution()
    n = 321
    print(sol.monotoneIncreasingDigits(n))







