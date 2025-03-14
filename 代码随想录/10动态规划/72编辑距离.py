from typing import *

"""
1. dp数组下标含义：dp[i][j]表示word1中前i个和word2中前j个需要的最小编辑次数（即word1[i]和word2[j]对应dp[i-1][j-1]），即index从1开始，i=0或j=0表示空字符串！
    注意：只有本题我们多加了空字符串的第0个维度，dp中1对应的才是字符串中第一个字母，因为本题初始化第一行和第一列很复杂，所以
    从空字符串开始初始化就会简单很多！
2. 递推公式：分两种情况
    1. 当前字母相同：dp[i][j] = dp[i - 1][j - 1]
        即当前不需要修改，那么需要的最小操作次数就是ij都回退一格（可以理解为使得前半部分相等所需要的操作数）
    2. 当前字母不相同：我们取三种操作中最小的次数，即取min
        1. 删除/增加word1或word2中的一个字母：
            1> word1: dp[i - 1][j] + 1 [删除word1/增加word2]
            2> word2: dp[i][j - 1] + 1 [删除word2/增加word1]
            注解：如果删除word1中的一个字母，那么i回退一格，可以理解为当前删除这一次算1个操作，加上使得少一个字母的word1和word2相同所需的操作数；同时，
            dp[i - 1][j] + 1也可以理解成给word2增加一个字母，即先使当前的word2和少一个字母的word1相同，再给word2添加那个少的字母就等于当前没少的word1。
            同理，dp[i][j - 1] + 1可以理解为word2删除一个字母，也可以理解为word1增加一格字母。也就是说前两个既包含了删除操作也包含了增加操作！
        2. 替换当前字母：dp[i - 1][j - 1] + 1
            例如abc和abd，当前我们看最后一个字母，我们需要替换word1中的c到d或word2中的d到c，但我们需要先使得它们两个的前半部分相同，
            所以就是都回退一格！
3. 初始化：第一列dp[i][0]指如何使word1[i]和空字符串相等，那么就是有几个字母删除几个，即dp[i][0] = i；第一行同理，dp[0][j] = j
4. 遍历顺序：正序遍历
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # 初始化
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        # 遍历
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 相同则不需要修改，那么就是都回退一格
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[m][n]




