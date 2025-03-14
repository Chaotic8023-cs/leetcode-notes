# 5
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True  # 初始化对角线
        # 最长的palindrome的start和end
        pstart, pend = 0, 0
        """
        含义：
        dp[i][j]表示s[i:j]是不是palindrome
        初始化：
        一个char一定是palindrome，所以我们初始化对角线上的(即dp[i][i])都为True
        其余默认False
        状态转移方程：
        有两种情况
            1. 如果ij只差1，说明是挨着的两个char，我们只需看两个char是否一样，即
            s[i] == s[j]
            2. 如果ij差的比1大，那么s[i:j]是palindrome的条件是s[i]和s[j]一样，且
            同时i到j中间那一段也是palindrome（在回文两头加相同字母还是回文），即
            s[i] == s[j] and dp[i+1][j-1] (== True)
        遍历顺序：
        由于ij差的比1大时我们要看中间那段，即dp[i+1][j-1]，所以我们得先遍历ij差1的，
        再遍历ij差2的，以此类推。
        如s = "babad"，遍历顺序如下（下图dp中数字代表第几步）：
            1. 我们初始化对角线（）
            2. 遍历对角线右上方的对角线
            3. ...
        
                    0 |     1 |     2 |     3 |     4
                ---------------------------------------------
                    0 |     1 |     2 |     3 |     4 |     5
                    1 |     0 |     1 |     2 |     3 |     4
                    2 |     0 |     0 |     1 |     2 |     3
                    3 |     0 |     0 |     0 |     1 |     2
                    4 |     0 |     0 |     0 |     0 |     1
                    
        也就是说我们斜着遍历，这样能保证后面检查dp[i][j]时dp[i+1][j-1]已经赋值过了
        注意左下角不用遍历，因为dp[i][j]和dp[j][i]等效，而且我们只看正向substring，
        不要反向的。
        """

        """
        这里这个loop就是上述的遍历方法：
        (省略初始化对角线)
        iter1： 01, 12, 23, 34
        iter2: 02, 13, 24
        iter3: 03, 14
        iter4: 04
        我们发现i的end每次减1，j和i之间的差每个循环加1，所以就是以下写法
        """
        gap = 1
        for iend in range(n-1, -1, -1):
            for i in range(iend):
                j = i + gap

                if j-i == 1:  # adjacent chars
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                if dp[i][j]:
                    if j - i > pend - pstart:
                        pstart, pend = i, j

            gap += 1

        # pprintdp(dp)
        return s[pstart:pend+1]

    # 一个比上面自己写的更好的遍历方式
    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True  # 初始化对角线
        # 最长的palindrome的start和end
        pstart, pend = 0, 0
        """
        遍历思路：
        对于dp[i][j]依赖于dp[i+1][j-1]
            1. i依赖于i+1，即前面i依赖于后面的i，所以i可以从后往前遍历
            2. j依赖于j-1，即后面的j依赖于前面的j，所以j可以从前往后遍历
        于是就相当于 （下图dp中数字代表第几步）：
        
                            0 |     1 |     2 |     3 |     4
                ---------------------------------------------
                    0 |     1 |     5 |     5 |     5 |     5
                    1 |     0 |     1 |     4 |     4 |     4
                    2 |     0 |     0 |     1 |     3 |     3
                    3 |     0 |     0 |     0 |     1 |     2
                    4 |     0 |     0 |     0 |     0 |     1
                    
        (省略初始化对角线)
        iter1：34
        iter2: 23, 24
        iter3: 12, 13, 14
        iter4: 01, 02, 03, 04
        """
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):

                if j-i == 1:  # adjacent chars
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                if dp[i][j]:
                    if j - i > pend - pstart:
                        pstart, pend = i, j

        return s[pstart:pend + 1]


if __name__ == '__main__':
    s = "babad"
    sol = Solution()
    print(sol.longestPalindrome(s))


