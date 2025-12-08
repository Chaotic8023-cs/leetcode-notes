from typing import *
from collections import Counter
import heapq


"""
最小堆：找前k个高频元素其实就是在频率数组中找最大的k个数，所以我们用一个哈希表记录频率 + 一个大小为k的最小堆记录较大的k个数即可。
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        min_heap = []
        for num, count in cnt.items():
            heapq.heappush(min_heap, (count, num))  # heapq默认按元组的第一个元素排序，所以这里先放频率，再放元素
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [x[1] for x in min_heap]  # 此时最小堆存的就是最大的那k个，我们返回全部

    # 排序法：直接对构造好的 Counter 按次数倒排，然后取前k个
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        vs = sorted(cnt.items(), key=lambda x: x[1], reverse=True)  # 按 cnt 排序
        return [v for v, _ in vs[:k]]
        


