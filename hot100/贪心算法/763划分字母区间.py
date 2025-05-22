from typing import *


"""
贪心：先遍历一边s获得所有字母最后一次出现的下标。然后，开始循环：每次取第一个字母为开头，初始化
curr_max为这个字母最后一次出现的下标，然后往后遍历，遇到每个字母都更新一次curr_max，直到
curr_max不再增加且我们遍历到curr_max了，则当前子串中的字母都仅出现在当前子串中。
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        # 先遍历一遍获取每个字母最后出现的下标
        last = {}
        for i in range(n):
            last[s[i]] = i
        # 然后每次选第一个字母作为起点，获取这个字母最后一次出现的位置，然后一直往后遍历，出现别的字母就和curr_max取max，直到curr_max不增大为止
        ans = []
        i = 0  # 每个子串的开头字母下标
        # 循环条件为：只要当前的开头i还没越界
        while i < n:
            curr_max = last[s[i]]
            j = i + 1
            while j < n and j <= curr_max:  # 结尾包含curr_max，因为curr_max是最后一次出现的下标，所以要包含
                curr_max = max(curr_max, last[s[j]])
                j += 1
            ans.append(j - i)
            i = j
        return ans

    # 用start记录每次的起始位置，继续用i遍历，这样更方便些
    def partitionLabels1(self, s: str) -> List[int]:
        n = len(s)
        last = {}
        for i in range(n):
            last[s[i]] = i
        ans = []
        i = 0
        while i < n:
            start = i
            curr_max = last[s[start]]
            i += 1
            while i <= curr_max:
                curr_max = max(curr_max, last[s[i]])
                i += 1
            ans.append(i - start)
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "qiejxqfnqceocmy"
    print(sol.partitionLabels(s))



