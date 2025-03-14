# 452
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def get_common(a, b):
            # 给两个interval a和b，返回它们的交集
            # 即arrow能同时射到这两个区间的范围
            starta, enda = a
            startb, endb = b
            if enda < startb:
                return None
            else:
                cstart = max(starta, startb)
                cend = min(enda, endb)
                return [cstart, cend]

        num_arrows = 0
        points = sorted(points, key=lambda x: x[0])
        # common start/end: 只记录重叠部分
        cstart, cend = points[0]
        """
        相当于反过来的insert，我们一直存一个交集，在此交集射箭能同时射中
        取过交集的intervals。当遇到无重叠部分的，则需要的arrow + 1，并
        重置交集到当前的interval
        """
        for start, end in points[1:]:
            if common := get_common([cstart, cend], [start, end]):
                cstart, cend = common
            else:
                # 当前interval无重叠，前一个交集就需要1根箭
                num_arrows += 1
                # 重置交集
                cstart, cend = start, end
        # +1因为我们总会剩一个，每次加的1是算在前一个交集的！
        return num_arrows + 1


if __name__ == '__main__':
    points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
    sol = Solution()
    print(sol.findMinArrowShots(points))
