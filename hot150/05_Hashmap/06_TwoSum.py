# 1
from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}  # key: num, value: index
        for idx, num in enumerate(nums):
            if target-num in hm:
                return [idx, hm[target-num]]
            hm[num] = idx


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))
