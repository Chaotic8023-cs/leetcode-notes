from typing import *


"""
看似是完全背包，但用背包问题做就复杂了，所以我们按常规dp思路做。
dp[i]：前i个字母是否能用wordDict组成（1-index）
递推公式：看i前面是否存在某个位置j，如果前j个字母能被组成，且后面的子串[j+1:i]在wordDict中，则说明前i个字母能被组成。这里index
初始化：用1-index是因为对于s中包含第一个字母的子串出现在字典中，需要dp[0] = True。
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        d = set(wordDict)
        dp = [False] * (n + 1)  # 1-index
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                # 由于用的1-index，dp[n]对应的就是s[n-1]，所以这里s[j:i]实际上是是第j个字母右边那个到第i个字母（包含）
                if dp[j] and s[j:i] in d:  # 如果前j个字母能被组成，第j个字母后面到第i个字母的子串在字典中，则整个前i个字母就能被组成
                    dp[i] = True
        return dp[n]


