from typing import *
import heapq
from collections import Counter


class Solution:
    """
    最小堆（优先队列）：这题和#215第K大的元素思路一样。我们要找前K个高频元素，即要找最大的那K个频率，所以用一个大小为K的最小堆就可以。这个
    最小堆用来存储最大的那K个元素，当大小超过K时，就会把小的pop出去，最后只留下最大的那K个在堆里。
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        mp = Counter(nums)
        for num, cnt in mp.items():
            heapq.heappush(pq, (cnt, num))  # heapq会使用iterable中的第一个元素作为key
            if len(pq) > k:
                heapq.heappop(pq)
        ans = []
        while pq:
            ans.append(heapq.heappop(pq)[1])
        return ans
