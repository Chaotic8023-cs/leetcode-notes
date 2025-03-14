# 97
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if len(s3) != m + n:
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        """
        含义：
        dp[i][j]表示用s1的前i个字母和s2的前j个字母能否构成s3的前i+j个字母
        状态转移方程：
        当我们看dp[i][j]时，当前s3中最后一个字母有两种情况：
            1. 当前s3的最后一个字母属于s1，即s3[i+j-1] == s1[i-1]
                我们则看s1的前i-1个字母和s2的前j个字母
                能否组成s3的前i+j-1个字母，即dp[i-1][j]。
                如果能，则其加上当前的s1的第i个字母，就能组成s3的前i+j个字母
                eg: xxxxxx + s1第i个字母 = s3前i+j个字母
                    需满足：dp[i-1][j] == True， 即xxxxxx能构成s3前i+j-1个字母
                
            2. 当前s3的最后一个字母属于s2，即s3[i+j-1] == s2[j-1]
                我们则看s1的前i个字母和s2的前j-1个字母
                能否组成s3的前i+j-1个字母，即dp[i][j-1]。
                如果能，则其加上当前的s2的第j个字母，就能组成s3的前i+j个字母
                eg: xxxxxx + s2第j个字母 = s3前i+j个字母
                    需满足：dp[i][j-1] == True， 即xxxxxx能构成s3前i+j-1个字母
        两种情况只要有一种可以，就代表当前用s1的前i个字母和s2的前j个字母能组成s3的前i+j个字母！
        初始化：
        dp[0][0] = True，s1和s2取0个字母可以组成s3取0个字母
        因为dp[i][j]由dp[i-1][j]或dp[i][j-1]得来，所以我们先初始化第一列和第一行：
            1. 第一列：即只用s1，不用s2，最多能构成s3开头的多少
            2. 第一行：即只用s2，不用s1，最多能构成s3开头的多少
        然后ij就可以都从1开始顺序遍历到结尾
        """
        for i in range(1, m+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = True
            else:  # s1最多到此位置就和s3开头不同了，直接停止
                break
        for j in range(1, n+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = True
            else:  # s2最多到此位置就和s3开头不同了，直接停止
                break
        for i in range(1, m+1):
            for j in range(1, n+1):
                curr_s3_idx = i + j - 1
                # s3当前的结尾可以属于s1也可以属于s2，任意一种满足即可构成当前的s3
                dp[i][j] = ((s3[curr_s3_idx] == s1[i-1] and dp[i-1][j])
                            or
                            (s3[curr_s3_idx] == s2[j - 1] and dp[i][j-1]))
        pprintdp(dp)
        return dp[m][n]

    # 更简洁的初始化
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if len(s3) != m+n:
            return False
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        """
        我们也可以只初始化dp[0][0]
        然后加上对i和j的判断即可顺带完成第一行和第一列的初始化
        """
        for i in range(m+1):
            for j in range(n+1):
                curr_s3_idx = i+j-1
                if i > 0 and s3[curr_s3_idx] == s1[i - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                if j > 0 and s3[curr_s3_idx] == s2[j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
        pprintdp(dp)
        return dp[m][n]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    sol = Solution()
    print(sol.isInterleave(s1, s2, s3))
    print(sol.isInterleave1(s1, s2, s3))

