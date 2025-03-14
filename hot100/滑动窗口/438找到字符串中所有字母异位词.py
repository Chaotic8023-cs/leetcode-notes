from typing import *
from collections import Counter

"""
滑动窗口：用一个哈希表维护一个长度等于p的滑动窗口里的字母count，每次往右移动一格，然后看窗口是否为anagram
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        ans = []
        target = Counter(p)  # 目标p的count
        count = Counter(s[:n - 1])  # 滑动窗口的count，窗口从s的开头出发，一开始的长度为p的长度少一个字母
        # 遍历s，每次给窗口末尾添加一格字母，开头减少一个字母，保证窗口大小一直是len(p)
        for i in range(n - 1, m):
            count[s[i]] += 1  # 窗口末尾添加一个字母，此时长度就等于p
            if count == target:  # 检查是否是anagram
                ans.append(i - n + 1)
            count[s[i - n + 1]] -= 1  # 在移动前把窗口开头减少一个字母
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "cbaebabacd"
    p = "abc"
    print(sol.findAnagrams(s, p))













if __name__ == '__main__':
    sol = Solution()
    s = "cbaebabacd"
    p = "abc"
    print(sol.findAnagrams(s, p))

