# 57
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    # 一次遍历解法
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        istart, iend = newInterval
        ans = []
        inserted = False
        for start, end in intervals:
            # case1: current interval less than whole newInterval
            if end < istart:
                ans.append([start, end])
            # case2: current interval greater than whole newInterval
            elif iend < start:
                # insert the newInterval once
                if not inserted:
                    ans.append([istart, iend])
                    inserted = True
                # insert current interval
                ans.append([start, end])
            # case3: current interval overlapped with newInterval
            else:
                """
                只要有重叠，就的合并，所以干脆直接把当前的interval合并到newInterval里，
                相当于我们把当前的interval也看作要insert的了。
                这样直到第一次遇到case1和case2（即newInterval整个大于或小于当前的inteval），
                就可以直接插入合并了的newInterval了！
                """
                istart = min(start, istart)
                iend = max(end, iend)
        """
        如果最后一个interval也能和newInterval合并，说明intervals遍历完了但还没插入
        我们插入即可
        """
        if not inserted:
            ans.append([istart, iend])
        return ans

    # 我们可以直接把newInterval加进来再sort一下，然后直接用#56题的merge
    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        i = 0
        n = len(intervals)
        while i < n:
            start, end = intervals[i]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= end:
                """
                只要这个interval的start比前一个的end小（或相等），则可以merge
                为了每次比较前一个end，即目前merge了的end，我们同时需要更新end
                """
                if intervals[j][1] > end:
                    end = intervals[j][1]
                j += 1
            ans.append([start, end])
            i = j
        return ans

    # 自己写的抽象insert
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals
        istart, iend = newInterval
        ans = []
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            if end < istart or istart > iend:  # initial non-overlapping intervals
                ans.append(intervals[i])
                i += 1
            else:  # start to overlap
                # use the smaller one as the overlapped start
                ostart = min(start, istart)
                j = i
                # find the first interval that has end > iend
                while j < len(intervals) and intervals[j][1] < iend:
                    # this means intervals[j] are within the newInterval
                    j += 1
                if j < len(intervals):
                    start, end = intervals[j]
                    if iend < start:  # no overlap with this j
                        ans.append([ostart, iend])
                        i = j
                    else:  # has overlap with this j
                        ans.append([ostart, end])
                        i = j + 1
                    istart = iend + 1
                else:  # iend > end of the last interval
                    ans.append([ostart, iend])
                    break
        return ans


if __name__ == '__main__':
    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    # newInterval = [4, 8]
    # [[1,2],[3,10],[12,16]]
    intervals = [[1, 5]]
    newInterval = [6, 8]
    sol = Solution()
    print(sol.insert(intervals, newInterval))
