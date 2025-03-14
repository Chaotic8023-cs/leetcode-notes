# 13
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def romanToInt(self, s: str) -> int:
        hm = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        prev = hm[s[n-1]]
        ans = prev
        """
        反着来，如果前一个比后一个小，直接减去前一个即可
        如：IX
        我们先遍历到X，ans+=10，然后遍历到I发现比X小，则ans-=1即可
        因为从后往前的遍历除了特殊的那几（IV, IX...）个外罗马数字都是从小到大的
        """
        for i in range(n-2, -1, -1):
            curr = hm[s[i]]
            if curr < prev:
                ans -= curr
            else:
                ans += curr
            prev = curr
        return ans


if __name__ == '__main__':
    s = "MCMXCIV"
    # M = 1000, CM = 900, XC = 90 and IV = 4
    sol = Solution()
    print(sol.romanToInt(s))

