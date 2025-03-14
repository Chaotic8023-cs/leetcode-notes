from typing import *


class Solution:
    """
    暴力解法
    其他解法如KMP就不记了
    """
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n):
            if haystack[i: i + m] == needle:
                return i
        return -1
