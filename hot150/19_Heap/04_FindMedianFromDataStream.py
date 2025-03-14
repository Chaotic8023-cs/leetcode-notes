# 295
from typing import *
import heapq
from collections import Counter
from itertools import count
import random


class MedianFinder:
    """
    我们用两个优先队列：min heap和max heap
    其中min存较大的一半数，max存较小的的一半数，使得min的个数要么等于max，要么比max多1个，所以最终median就是：
    1. 如果和为奇数：较大一半的最小的那个，即min的root
    2. 如果和为偶数：(较小的一半的最大的那个+较大的一半的最小的那个) / 2，即min和max分别pop掉一个然后求平均

    如何加新的数字：
    思路就是我们一直往min加，同时为了保证个数差在一个范围内，如果min比max多了2，则从min往max转移一个。
    因为min存的是较大的一半，所以我们每次先往max插入这个新的num，然后pop掉一个（也就是当前小的那一半的最大的元素）加入到min。也就是说max
    的作用就是找到最大的元素然后插入到min中。最后为了保证min和max各一半或min多一个，当min比max多两个的时候我们往max转移1个，也就是把较大
    的一半的最小的那个插入到较小的一半中，使得min和max的个数相等。
    """

    def __init__(self):
        self.min_heap = []  # 存较大的一半
        self.max_heap = []  # 存较小的一半

    def addNum(self, num: int) -> None:
        # 插入max heap
        heapq.heappush(self.max_heap, -num)  # 存-num，因为heapq默认从小到大排序
        # 把max heap中最大的元素加入到min heap中
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        # 检查min heap的大小，如果min heap比max heap多两个，则往max heap转移1个，使得min heap要么等于max heap，要么比max多1个
        if len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + (-self.max_heap[0])) / 2  # 注意max heap中存的是-num！
        else:
            return self.min_heap[0]


# 用二分法找到插入的位置（#35），使得arr一直是sorted，这样findMedian直接返回中间的数即可
class MedianFinder1:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        i = self.find_insert_pos(num)
        self.arr.insert(i, num)

    def findMedian(self) -> float:
        mid = (len(self.arr) - 1) // 2
        if len(self.arr) % 2 == 1:
            return self.arr[mid]
        else:
            return (self.arr[mid] + self.arr[mid + 1]) / 2

    def find_insert_pos(self, target):
        l, r = 0, len(self.arr)
        while l < r:
            mid = (l+r) // 2
            if self.arr[mid] >= target:
                r = mid
            else:  # arr[mid] < target
                l = mid + 1
        return l


if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())
    mf.addNum(3)
    print(mf.findMedian())




