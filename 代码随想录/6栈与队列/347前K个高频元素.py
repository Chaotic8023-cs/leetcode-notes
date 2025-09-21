from typing import *
import heapq
from collections import Counter


class Solution:
    """
    最小堆（优先队列）：这题和#215第K大的元素思路一样。我们要找前K个高频元素，即要找最大的那K个频率，所以用一个大小为K的最小堆就可以。这个
    最小堆用来存储最大的那K个元素，当大小超过K时，就会把小的pop出去，最后只留下最大的那K个在堆里。
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        min_heap = []
        for v, f in cnt.items():
            heapq.heappush(min_heap, (f, v))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [v for f, v in min_heap][::-1]  # min_heap是从小到大，因为要TopK，所以反转一下。（虽然题目要求以任意顺序返回，但是这里取反一下最终返回的就是按频率倒排）
