from typing import *


"""
1. dp数组下标含义：dp[i][j]表示s[0,i]的子串中有多少种不同的t[0,j]的子串（dp数组和字符串下标对应）
2. 递推公式：由于是求不同种类的个数，类比爬楼梯的方法个数，此时递推就不+1。分两种情况
    1. 当前字母相同：dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        1. dp[i - 1][j - 1]：s和t都少一个字母的方法数
        2. dp[i - 1][j]：还有s少一个字母，也就是s的前面部分本来就有完整t的个数
    2. 当前字母不同：dp[i][j] = dp[i - 1][j]
        即方法数等于s删除一个字母后所包含的当前t子串的个数（因为当前字母不同，方法数就等于往前少一各字母能包含多少各当前的t）
    
3. 初始化：第一列表示s[0,i]有多少种不同的方法组成t[0]，所以第一列中遇到相等的字母方法数就+1；第一行表示s[0]就一个字母有多少种不同的方式
    组成t[0,j]，显然只有j=0时如果两个字母相同才有1种，但是初始化第一列时已经把dp[0][0]考虑了，所以第一行就不用初始化了
4. 遍历顺序：正序遍历
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # 初始化
        dp = [[0] * n for _ in range(m)]
        count = 0
        for i in range(m):
            if s[i] == t[0]:
                count += 1
            dp[i][0] = count
        # 由于第一行表示s[0]中有没有t[j]，所以只用看t的第一个字母和s[0]一样不，在往后s的一个字母肯定不能包含多余一个字母的t，但是第一列已经给dp[0][0]初始化了，所以就不用管了
        # 遍历
        for i in range(1, m):
            for j in range(1, n):
                if s[i] == t[j]:  # 当前字母相同
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  # st各退一格 + s删除一个字母
                else:  # 当前字母不同
                    dp[i][j] = dp[i - 1][j]  # 由s删除一个字母的来
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    sol = Solution()
    s = "babgbag"
    t = "bag"
    print(sol.numDistinct(s, t))


