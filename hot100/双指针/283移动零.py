from typing import *


class Solution:
    """
    双指针：因为要保留非零元素相对顺序，那我们就从前到后遍历，遇到非零元素就往前放到i处
    """
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 0  # i：当前非零元素能放的位置；j：遍历指针
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1







