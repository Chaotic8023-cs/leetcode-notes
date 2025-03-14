# 27
from typing import *


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # index of elements not equal to val (to remain)
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k


if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    sol = Solution()
    print(sol.removeElement(nums, val))
    print(nums)