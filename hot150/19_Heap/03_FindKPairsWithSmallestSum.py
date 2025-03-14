# 373
from typing import *
import heapq
from collections import Counter
from itertools import count
import random


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        (sum(u, v), i, j): i是nums1的index，j是nums2的index
        一开始放nums1的前k个和nums2的第一个的pairs
        然后每次pop掉一个，并在允许的情况下push进去当前nums1的元素和nums2中的下一个元素

        原理：因为两个array是sorted，所以一开始先用nums2中最小的第一个元素和nums1的前k个元素匹配，
        再在循环中不断的加入nums2中下一小的元素。因为越前面的元素和一定越小，所以相当于第一个pop出来
        的index是(0, 0)，那么会加入(0, 1)，之后第二小的可能是(0, 1)或者一开始加入的(1, 0)
        """
        q = [(u + nums2[0], i, 0) for i, u in enumerate(nums1[:k])]
        heapq.heapify(q)
        ans = []
        while q and k > 0:
            _, i, j = heapq.heappop(q)  # sum, nums1_index, nums2_index
            ans.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                # 加入nums1的当前元素（i）和nums2的下一个元素（j+1）
                heapq.heappush(q, (nums1[i] + nums2[j+1], i, j+1))
            k -= 1
        return ans

    # naive: 直接把所有的pair都放进heap中然后pop前k个 -> 过不了，内存超了！
    def kSmallestPairs1(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        for u in nums1[:k]:
            for v in nums2[:k]:
                heapq.heappush(min_heap, (u + v, [u, v]))
        results = []
        for _ in range(k):
            results.append(heapq.heappop(min_heap)[1])
        return results


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    print(sol.kSmallestPairs(nums1, nums2, k))
