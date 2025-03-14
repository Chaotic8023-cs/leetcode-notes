from typing import *


"""
1. dp数组下标含义：dp[i][j]表示text1和text2中[0,i]和[0,j]所对应的子串中的最长公共子序列的长度
    注意：前三个题#300，#674，#718都是定义以ij为结尾的，这里因为不连续且有两个字符串，所以我们不能定义以ij为结尾的，不然我们就没法
    找到前一个状态了！
2. 递推公式：
    1. 如果text1[i] == text2[j]：dp[i][j] = dp[i - 1][j - 1] + 1
        即比它们小1的子串中的最长公共子序列的长度 + 1
    2. 如果text1[i] != text2[j]:dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        即text1和text2各少一个字母时的最长公共子序列，取max
        为什么要考虑当前两个字母ij不相等的情况呢？因为本体不是连续的，不相等的情况前面可能也有不连续的公共子序列，所以当前dp[i][j]
        的值就不一定是0，所以得考虑！因为当前ij字母不相等，所以转化为两个子问题的最大值，即个减少一个字母取最大值！
3. 初始化：此题就和#674连续子序列初始化有变化了，因为现在不连续且dp定义不是以ij结尾，而是到i到j整个前面的子串，所以第一行和第一列
    只要碰到和对方第一个字母相等的情况，后面所有的下标都要初始化成1！
4. 遍历顺序：
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # 初始化：只要相等一次，那么后面所有的地方都是1，因为本题不连续，所以dp定义的是到ij的前面整个子串中的最大长度！
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            elif i > 0:
                dp[i][0] = dp[i - 1][0]
        for j in range(n):
            if text2[j] == text1[0]:
                dp[0][j] = 1
            elif j > 0:
                dp[0][j] = dp[0][j - 1]
        # 遍历
        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # 因为不连续，如果当前ij字母不相等的情况，它们前面也可能有匹配上的公共子序列，所以值不一定是0，得考虑！
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    sol = Solution()
    text1 = "oxcpqrsvwf"
    text2 = "shmtulqrypy"
    print(sol.longestCommonSubsequence(text1, text2))



