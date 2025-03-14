from typing import *



class Solution:
    """
    和#647回文子串的双指针法（找所有）一样，只是改成只要最长的那个即可！
    """
    def longestPalindrome(self, s: str) -> str:
        def extend(s, i, j, n):
            nonlocal ans, max_len
            while i >= 0 and j < n and s[i] == s[j]:
                if j - i + 1 > max_len:  # 当前的回文子串更长
                    max_len = j - i + 1
                    ans = s[i:j + 1]
                i, j = i - 1, j + 1

        ans = ""
        max_len = 0  # 记录当前最长的
        n = len(s)
        for i in range(n):
            extend(s, i, i, n)  # 以一个字母s[i]为中心，作为起点往两边扩展
            extend(s, i, i + 1, n)  # 以两个字母s[i]和s[i + 1]为中心，作为起点往两边扩展
        return ans

    """
    动态规划：和#647回文子串的动规法也一样，只是改成只要最长的那个即可！
    """
    def longestPalindrome_dp(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = s[0]
        max_len = 1
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    # 每次如果[i,j]是更长的回文子串则更新max_len和ans
                    if dp[i][j] and j - i + 1 > max_len:
                        max_len = j - i + 1
                        ans = s[i:j + 1]
        return ans





