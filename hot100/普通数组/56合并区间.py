from typing import *

"""
其实用一个指针就行了
每次取当前的第一个区间作为基底，从后一个区间开始遍历，只要有交集就合并（对r取max）
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        i = 0
        ans = []
        while i < n:
            l, r = intervals[i]  # 每次取第一个
            i += 1
            while i < n and intervals[i][0] <= r:  # 然后从后一个开始遍历，有交集的就扩展r
                r = max(r, intervals[i][1])
                i += 1
            ans.append([l, r])
        return ans






