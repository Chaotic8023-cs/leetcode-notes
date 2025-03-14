from collections import defaultdict
from typing import *


"""
滑动窗口：i为左指针，右指针j用来遍历，每次把s[j]加入到哈希表中做统计，然后只要当前s[j]有重复左指针右移。
相当于我们每次记录以j为结尾（包含）的最长无重复子串的长度。

总结：只要当前字母c没重复右指针就一直右移，遇到当前字母重复后(count[c] > 1)，左指针一直右移直到当前字母无重复（count[c] == 1）后，
更新max_len
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)  # 哈希表用来记录每个字母出现的次数
        i = 0
        ans = 0
        for j, c in enumerate(s):
            count[c] += 1
            # 如果此时count[c] > 1，即当前字符出现重复，则一直向右移动左指针直到不重复为止
            while count[c] > 1:
                count[s[i]] -= 1  # i是左指针，所以count[s[i]]一定 >= 1，不会出现count[s[i]]减之后变成负数
                i += 1
            ans = max(ans, j - i + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = " "
    print(sol.lengthOfLongestSubstring(s))







