from typing import *

"""
似乎是完全背包可重复放入，然后求是否能装满，但如果按背包的思路做就复杂做不出来了，不如我们不想背包按常规动态规划思想做！
1. dp数组下标含义：dp[i]表示前i个字母是否能被组成
2. 递推公式：if dp[j] == True and s[j:i] in words: dp[i] = True
    即对于每个位置i，如果前面某个位置j已经能被组成了，然后j后面到i这个单词在字典中，则说明当前整个到i的子串能被组成
3. 初始化：
4. 遍历顺序：
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                # 由于用的1-index，dp[n]对应的就是s[n-1]，所以这里s[j:i]实际上是是第j个字母右边那个到第i个字母（包含）
                if dp[j] == True and s[j:i] in words:  # 如果前j个字母能被组成，第j个字母后面到第i个字母的子串在字典中，则整个前i个字母就能被组成
                    dp[i] = True
        return dp[len(s)]





