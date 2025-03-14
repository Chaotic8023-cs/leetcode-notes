from typing import *


class Solution:
    """
    双指针：其实本题双指针法更容易记且空间复杂度更低
    核心思想就是如果中间部分是回文，那么往两边各加一个相同的字母就也是回文。
    于是我们以每个字母为中心，往两边扩展，统计每个位置的回文数量最后求和。
    注意的是中心不部分可以是一个字母也可以是两个字母，所以最好分开统计这样清晰。
    """
    def countSubstrings(self, s: str) -> int:
        def extend(s, i, j, n):  # (字符串，起点i，终点j，字符串总长)
            count = 0
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i, j = i - 1, j + 1
            return count

        ans = 0
        n = len(s)
        for i in range(n):  # 注意：要遍历完整的len(s)，extend中已经检查了ij越界问题！如果range(n - 1)，则会漏算最后一个字母单独作为回文的情况！
            ans += extend(s, i, i, n)  # 以一个字母s[i]为中心，作为起点往两边扩展
            ans += extend(s, i, i + 1, n)  # 以两个字母s[i]和s[i + 1]为中心，作为起点往两边扩展
        return ans

    """
    1. dp数组下标含义：这题和前面的序列题都不一样，dp[i][j]表示子串[i,j]（左闭右闭）是否为回文，其中j >= i
    2. 递推公式：核心思想是如果中间部分是回文的话，那么两边各加一个相同的字母就也是回文！所以按中间部分的大小分情况
        1. j - i <= 1：dp[i][j] = True
            即要么i == j,一个字母肯定是回文；要么i和j相邻，如果字母相同就是回文
        2. j - i > 1：dp[i][j] = dp[i + 1][j - 1]
            即i和j相差大于1，那么如果中间部分（dp[i + 1][j - 1]）是回文且字母i和j相同，就是回文
    3. 初始化：一开始都是False
    4. 遍历顺序：重点！由于dp[i][j] = dp[i + 1][j - 1]，即dp[i][j]是由左下方的一格推出来的，所以应该
        从下到上从左到右遍历，即i倒序j正序遍历。同时，因为j >= i，j的for循环就从i开始!
    """
    def countSubstrings_dp(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):  # j >= i，因为我们看的是子串[i,j] (注：j从和i相等起步，所以我们就会把i == j的情况算上，即对角线，所以我们就不用初始化对角线！)
                if s[i] == s[j]:  # 只用看相等的情况，因为默认都是False
                    if j - i <= 1:
                        dp[i][j] = True
                        ans += 1  # 遇到一个子串ans就+1
                    else:  # j - i > 1:
                        dp[i][j] = dp[i + 1][j - 1]
                        if dp[i][j]:
                            ans += 1  # 遇到一个子串ans就+1
        return ans





