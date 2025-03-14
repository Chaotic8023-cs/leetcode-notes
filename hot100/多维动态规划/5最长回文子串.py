from typing import *


"""
最长回文子串用双指针比动规好记，所以即双指针即可。
"""
class Solution:
    """
    双指针：从回文中点往外扩散。遍历s，每个位置上以1个字母或2个字母为中点往外扩散，看回文子串最长多长。
    """
    def longestPalindrome(self, s: str) -> str:
        def extend(i, j):
            nonlocal ans, max_len
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    ans = s[i:j + 1]
                i, j = i - 1, j + 1  # i左移，j右移，即往两边扩散

        ans, max_len = "", 0
        for i in range(len(s)):  # ans初始化为空，所以这里必须遍历到len(s)才不会漏答案，下标越界在extend中已经检查过了所以不需要担心
            extend(i, i)  # 中心为1个字母
            extend(i, i + 1)  # 中心为2个字母
        return ans

    """
    动态规划：
    dp[i][j]表示子串[i,j]是否为回文。如果s[i] == s[j]相等，则：
        1. 如果i == j或j = i + 1，即如果是一个字母或两个字母，则dp[i][j]一定为True
        2. 如果i > j + 1，即如果ij差2及以上，则dp[i][j] = dp[i + 1][j - 1]，也就是看中间部分是否为回文（ij都往中间退一格）
    从递推公式看出dp[i][j]是从左下推出来的，所以遍历顺序为从下到上，从左到右
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
                    if dp[i][j] and j - i + 1 > max_len:
                        max_len = j - i + 1
                        ans = s[i:j + 1]
        return ans



