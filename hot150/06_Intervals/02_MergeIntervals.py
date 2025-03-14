# 56
from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on start of each interval, so we can traverse sequentially
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

    # 更简洁一点的
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on start of each interval, so we can traverse sequentially
        intervals = sorted(intervals, key=lambda x: x[0])
        # merged start and end, initially just first interval
        mstart, mend = intervals[0]
        ans = []
        for start, end in intervals[1:]:
            # case1: merged end less than current start, cannot merge anymore
            if mend < start:
                ans.append([mstart, mend])
                # update the merged to current start and end start new merging process
                mstart, mend = start, end
            else:  # current start <= mend, can be merged
                # mstart no need to update as intervals are sorted based on start
                mend = max(mend, end)
        # insert the merged part, as we have not yet inserted the last merged interval
        ans.append([mstart, mend])
        return ans





if __name__ == '__main__':
    intervals = [[1,4],[2,3]]
    sol = Solution()
    print(sol.merge(intervals))
