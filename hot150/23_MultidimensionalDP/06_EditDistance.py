# 72
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        """
        含义：
        dp[i][j]表示word1的前i个字母变成word2的前j个字母需要的最少操作
        状态转移方程：
        当我们看dp[i][j]时，我们只看当前末尾的这两个字母，
        即word1第i个和word2第j个 -> word1[i-1]和word2[j-1]
        分两个情况：
            1. 当前末尾两字母相同，即word1[i-1] == word2[j-1]：
                那么当前末尾不需要操作，最小操作数就等于word1少了当前结尾变成word2少了当前结尾，即
                dp[i][j] = dp[i-1][j-1]
            2. 当前末尾两字母不同，即word1[i-1] != word2[j-1]：
                那我们就需要进行操作，根据题设，有三种操作所以有三种情况：
                    1> Insert:
                        dp[i][j-1] + 1
                        即word1变成少一个字母的word2需要的最少操作，加上增加一个字母变成word2的一次操作
                        +1是word1增加一个字母的操作
                    2> Delete:
                        dp[i-1][j] + 1
                        即word1删除一个字母变成word2需要的最少操作，加上删除这个字母需要的一次操作
                        +1是删除word1的一个字母的操作
                    3> Replace:
                        dp[i-1][j-1] + 1
                        即少一个字母的word1变成少一个字母word2需要的最少操作，加上替换word1的末尾的一次操作
                        +1是替换末尾一次的操作
                注意：
                    以上都是针对于word1进行的操作，但为什么在第一种情况里反而是j-1？
                    其实word1增加一个字母变成word2，就相当于word2减少一个字母变成word1，
                    是等效的。dp[i][j-1]+1 可以（针对word2，逆向理解）理解为word2减少一个字母变为word1
                    的最少操作加上减少这个字母的一次操作，也可以（针对word1，正向理解）理解为word1变为少一个字母的word2
                    需要的最少操作加上变之后增加一个字母的一次操作。
                    正向理解时，word1需要是少一个字母才能增加，所以 dp[i][j-1]+1 的“字面”意思就把word1变成
                    少一个字母的word2，然后增加一个字母变成word2的操作。它等效于反着理解，即word2删一个字母
                    变成word1。因为word1通过一系列操作变成word2，那么word2也可以通过同样的一些列逆操作变成word1！
                    
                    所以dp[i][j]可以是word1的前i个字母变为word2的前j个字母需要的最少操作，也可以是
                    word2的前j个字母变成word1的前i个字母需要的最小操作！
        初始化：
        因为dp[i][j]可以从上、左、左上三个格子得来，所以我们需要初始化第一行和第一列
        dp[0][0] = 0，即""变成""不需要操作
        第一列就是word1变成""（空word2）需要的最少操作，即当前word1有几个字母就delete几次即可
        第一行就是word2变成""（空word1）需要的最少操作，即当前word2有几个字母就delete几次即可
        遍历顺序：
        根据递推公式，我们需要从左到右，从上到下遍历     
        """
        # init
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        # iterate
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:  # ending char same
                    dp[i][j] = dp[i-1][j-1]
                else:  # ending char not same, need operation
                    # operation w.r.t word1 (equivalent to reverse operation w.r.t word2)
                    dp[i][j] = min(
                        dp[i][j-1] + 1,     # add
                        dp[i-1][j] + 1,     # delete
                        dp[i-1][j-1] + 1    # replace
                    )
        return dp[m][n]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    sol = Solution()
    print(sol.minDistance(word1, word2))

