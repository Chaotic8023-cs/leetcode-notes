from typing import *


class Solution:
    """
    找区间交集：我们要一根箭射尽可能多的气球，所以要找区间的交集。
    """
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        n = len(points)
        ans = 0
        i = 0
        while i < n:
            l, r = points[i]
            i += 1
            # 只要当前区间和目前的[l,r]存在交集，则更新[l,r]为交集。也就是说只要交集存在，则一直更新交集（缩小交集）。
            while i < n and points[i][0] <= r:
                l, r = max(l, points[i][0]), min(r, points[i][1])  # lr更新为和当前区间的交集（l取大的，r取小的）
                i += 1
            ans += 1
        return ans

    """
    自己写的：即找区间的交集，从左到右遍历，我们想要一根箭射尽可能多的气球，所以只要当前区间和前面的有重叠就说明一箭能射穿。为了方便找重叠，
    我们可以按区间起始点进行排序，这样我们判断下一个区间是否有重合就只用看下一个区间的start是否在当前区间的end前。
    """
    def findMinArrowShots1(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        points = sorted(points, key=lambda x: x[0])
        i = 0
        while i < n:
            l, r = -float('inf'), float('inf')  # 用来计算交集，只要有交集就说明当前这一箭能射穿
            ans += 1  # 放一箭
            # 有相交就一直遍历，即求这一箭最多能射穿多少气球
            while i < n and points[i][0] <= r:
                l, r = points[i][0], min(r, points[i][1])  # 当前第i个区间和前面的相交，因为后面的start一定更大（排序了），所以相交后的start一定就是当前的start
                i += 1
        return ans




if __name__ == '__main__':
    sol = Solution()
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(sol.findMinArrowShots(points))



