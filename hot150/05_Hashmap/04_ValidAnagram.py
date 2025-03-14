# 242
from typing import *
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        return s == t

    # 用hashmap的方法：Counter
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = Counter(s)
        for c in t:
            freq[c] -= 1
            if freq[c] < 0:
                return False
        return True

    # 也可以直接比较两个Counter
    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.isAnagram(s, t))
