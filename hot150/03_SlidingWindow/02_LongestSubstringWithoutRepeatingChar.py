# 3
from typing import *


class Solution:
    # 相当于固定start，移动end
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = set()
        n = len(s)
        res = 0
        for end in range(n):
            while end < n and s[end] not in hm:
                hm.add(s[end])
                end += 1
            res = max(res, len(hm))
            hm.clear()
        return res

    # 双指针 (相当于固定end，移动start)
    """
    start:end 记录当前最长的无重复substring (Invariant)
    遍历s，只要当前的char出现在set里，说明end
    之前有重复的，我们就一直把start右移，直到
    start:end里没有和当前char重复的位置。于是我
    们就可以把当前char加入set，更新ans即可。
    """
    def lengthOfLongestSubstring1(self, s: str) -> int:
        ss = set()
        start, ans = 0, 0
        for end, c in enumerate(s):
            while c in ss:
                ss.remove(s[start])
                start += 1
            ss.add(c)
            ans = max(ans, end - start + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))
