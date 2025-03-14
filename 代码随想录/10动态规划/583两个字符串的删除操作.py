from typing import *


"""
本题其实就是先求出最长公共子序列（#1143），然后剩余字母就是要删掉的。
其实这题可以按常规dp定义作，即定义dp[i][j]就是对应的两个子串要删除的最小次数，但我们就记最长公共子序列的方法就行了！
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # 初始化
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if word1[i] == word2[0]:
                dp[i][0] = 1
            elif i > 0:
                dp[i][0] = dp[i - 1][0]
        for j in range(n):
            if word2[j] == word1[0]:
                dp[0][j] = 1
            elif j > 0:
                dp[0][j] = dp[0][j - 1]
        # 遍历
        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # 求出最长公共子序列的长度后，要删除的就是两个字符串中除了最长公共子序列的字母数
        return m + n - 2 * dp[m - 1][n - 1]


"""
常规dp做法：
1. dp数组下标含义：dp[i][j]表示使得word1[0, i]和word2[0, j]相等需要的删除操作次数
2. 递推公式：
    1.  word1[i - 1] == word2[j - 1]：如果当前字母相等
        则所需删除次数就是各退一格需要的删除次数
    2. 如果当前字母不同：
        则取min：
            1. 使word1退一格和word2不变相等所需的次数 + 删掉word1中当前字母（1次删除操作），即dp[i - 1][j] + 1
            2. 使word2退一格和word1不变相等所需的次数 + 删掉word2中当前字母（1次删除操作），即dp[i][j - 1] + 1
3. 初始化：因为如果dp下标和字符串下标对应的化，第一行和第一列非常难初始化，所以我么dp数组中维度都+1，这样第一列就是
    word1有而word2为空，所以word1有几个字母就得删除几次。第一行同理。
4. 遍历顺序：正序
"""
class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp数组生成时mn都+1，这样第一行第一列就很好初始化了
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 初始化第一行第一列：删除到空需要多少步，即有几个字母就删几个字母
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        # 遍历：此时下标i对应word1[i - 1]，j对应word2[j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # 当前字母相同，则操作数等于各退一格的操作数
                    dp[i][j] = dp[i - 1][j - 1]
                else:  # 当前字母不同，则操作数等于删除word1或word2当前字母所需的1次操作，加上使剩余部分相同的操作数，两个中取min
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m][n]
