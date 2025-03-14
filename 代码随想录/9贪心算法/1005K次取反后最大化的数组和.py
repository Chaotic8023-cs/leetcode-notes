from typing import *
import heapq


class Solution:
    """
    贪心：每次选最小的数进行取反，用一个优先队列就行了。
    每次选最小的数进行取反解决了：
        1. 如果有负数，最小的负数取反相当于加上了最大能加的
        2. 如果没负数，则最小的正数取反相当于减少了最小的能减的
    """
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):  # 每次选最小取反，一共取反k次
            i = heapq.heappop(nums)
            heapq.heappush(nums, -i)
        return sum(nums)




