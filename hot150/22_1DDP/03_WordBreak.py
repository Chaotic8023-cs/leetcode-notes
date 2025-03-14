# 139
from typing import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict set for fast access
        hm = set(wordDict)
        """
        dp[i]代表string前i个字母能不能由wordDict组成
        dp[0] = True：空的string设成True一遍s里第一个word能match到
        每次考虑dp[i]时，看之前有没有一个位置j为True（前j个能用wordDict组成）
        且j后面到当前位置的substring在wordDict里
        相当于看前面是否有能合成的substring + 一个wordDict里的word
        """
        # 注意这里是1-based index
        dp = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            # 注意index，dp要比s的index大1，这里我们要看j后面的 (j+1到i, inclusive)，
            # 即dp[j+1:i+1]，换成s的话对应的都要-1，即s[j:i]!
            dp[i] = any(dp[j] and s[j:i] in hm for j in range(i))
        return dp[-1]


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))
