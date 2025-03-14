from typing import *


"""
本题直接双指针线性搜索就行，不用动规。

用动态规划的话，本题其实和#1143一样，也就是求最长公共子序列，最后看求出来的公共子序列长度是否和s相等即可。
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i += 1
            j += 1
        return i == len(s)


if __name__ == '__main__':
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))



