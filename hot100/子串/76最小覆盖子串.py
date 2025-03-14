from typing import *
from collections import Counter
from math import inf


"""
自己写的
双指针+哈希表计数：
基本思路：我们一直右移右指针j直到区间内囊括了t的所有字母，此时尽可能的右移左指针i使得区间尽可能的缩小，同时还能囊括t的所有字母，最后更新答案
解决方案：用一个哈希表count统计区间内的所有字母，一个contribution_count来统计当前区间内对组成t有贡献的字母数（同时还用作判断当前区间是否囊括t了），
我们每次首先右移j，直到当前区间囊括了t。然后尽可能的右移i来缩小区间，直到当前区间还囊括t且缩到最小，就可以更新ans了。最后，i右移1位来继续下一个循环的寻找。
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        target = Counter(t)
        contribution_count = 0
        i, j = 0, 0
        curr = Counter()
        min_len, ans = inf, ""
        while j < m:
            # 右移j，使得当前区间囊括t
            while j < m and contribution_count < n:
                # 要先检查当前字母是否有贡献，再把他加入到curr中
                if s[j] in target and curr[s[j]] < target[s[j]]:
                    contribution_count += 1
                curr[s[j]] += 1
                j += 1
            # 当前区间囊括t了：即当前区间内对组成t有贡献的字母数够了。此时[i,j)囊括t，j不包含因为j最后+=1了
            # 如果j越界了还没有攒够contribution_count，则while loop结束
            if contribution_count == n:
                # 尽可能的右移i来缩小区间：以下两种情况可以去除当前字母s[i]：1. s[i]不在t中 2. s[i]在t中但当前区间中的s[i]有多余
                while s[i] not in target or curr[s[i]] > target[s[i]]:
                    curr[s[i]] -= 1
                    i += 1
                # 此时窗口[i, j)尽可能短且囊括t，我们更新ans
                if j - i < min_len:
                    min_len = j - i
                    ans = s[i:j]
                # i右移一位来继续寻找下一个可能的区间：此时区间是当前最小的囊括t的区间，经过上面一个while后当前区间开头一定是t中的一个字母，所以还要contribution_count -= 1
                curr[s[i]] -= 1
                contribution_count -= 1
                i += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "bdab"
    t = "ab"
    print(sol.minWindow(s, t))










