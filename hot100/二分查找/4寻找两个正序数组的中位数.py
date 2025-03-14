from typing import *
import heapq


"""
取自：#295数据流的中位数
"""
class MedianFinder:
    def __init__(self):
        self.minQ = []
        self.maxQ = []

    def addNum(self, num):
        heapq.heappush(self.maxQ, -num)
        heapq.heappush(self.minQ, -heapq.heappop(self.maxQ))
        if len(self.minQ) > len(self.maxQ) + 1:
            heapq.heappush(self.maxQ, -heapq.heappop(self.minQ))

    def findMedian(self):
        if len(self.minQ) == len(self.maxQ) + 1:
            return self.minQ[0]
        else:
            return (self.minQ[0] - self.maxQ[0]) / 2


"""
直接按#295做，把两个数组当成数据流即可。二分边界条件太难记了，所以直接用堆即可。
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mf = MedianFinder()
        for i in nums1:
            mf.addNum(i)
        for j in nums2:
            mf.addNum(j)
        return mf.findMedian()










