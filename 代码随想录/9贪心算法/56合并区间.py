from typing import *


class Solution:
    """
    贪心：每次取第一个区间[l,r]，然后遍历后面的区间看是否重叠（start <= r），如果能重叠就一直更新r，知道没法重叠了则加入当前合并好的区间
    （l就是一开始第一个区间的l，r是遍历中重叠区间的最大的那个r）
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])  # 按start进行排序，方便判断重叠
        i = 0
        while i < n:
            l, r = intervals[i][0], intervals[i][1]
            i += 1
            while i < n and intervals[i][0] <= r:  # 能重叠就一直加
                r = max(r, intervals[i][1])
                i += 1
            ans.append([l, r])
        return ans


if __name__ == '__main__':
    sol = Solution()
    intervals = [[0, 4], [1, 4]]
    print(sol.merge(intervals))
