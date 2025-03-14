# 12
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def intToRoman(self, num: int) -> str:
        hm = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        # 其实这用list of tuples就可以
        ans = ""
        idx = 0
        """
        一种贪心思想，从大到校尽可能多的应用当前最大的mapping
        """
        while num != 0:
            if num >= arr[idx]:
                num -= arr[idx]
                ans += hm[arr[idx]]
            else:
                idx += 1
        return ans


if __name__ == '__main__':
    num = 1994
    sol = Solution()
    print(sol.intToRoman(num))

