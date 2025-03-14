from typing import *


"""
动态规划：dp[i][j]表示word1前i个和word2前j个需要的操作数。创建dp数组时时ij都多加一行表示空字符串（即前0个字母）方便初始化。
递推公式：
    1. word1[i - 1] == word2[j - 1]：当前字母相等，不需要操作，操作数 = 都回退一格的操作数
    2. word1[i - 1] != word2[j - 1]：
        1> 替换：先保证两个word前半部分相同（都回退一格），然后再替换最后一个字母的其中一个，所以+1
        2> 增加/删除：一个表达式同时对应增加/删除（两种理解）
            【1】 dp[i - 1][j] + 1：word1删除掉最后一个字母，或word2后面增加一个字母。（删除：word1删除最后一个字母，所以时word1退一格和word2相等；增加：word2要增加一个字母，首先得当前的word2和word1少一个字母相等，所以增加的就是当前word1的最后一个字母）
            【2】 dp[i][j - 1] + 1：word2删除掉最后一个字母，或word1后面增加一个字母。（同理）
初始化：第一行第一列表示把一个word变成空字符串，所以只能删除，有几个字母就删除几次。
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 都多一行代表空字符串，方便初始化
        # 初始化：都变成空字符串，则之能删除，有几个字母就删除几次
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # 因为是1-index，所以访问原字符串时index要-1
                    dp[i][j] = dp[i - 1][j - 1]  # 第i个和第j个字母相等，则当前不需要操作，操作数=都回退1格的操作数
                else:  # 增加/删除，和替换
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[m][n]




