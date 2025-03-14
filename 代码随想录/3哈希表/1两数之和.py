from typing import *


class Solution:
    """
    倒排索引：即ht[num] = index
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i, num in enumerate(nums):
            if target - num in ht:
                return [i, ht[target - num]]
            else:
                ht[num] = i