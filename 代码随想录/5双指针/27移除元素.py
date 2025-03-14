from typing import *


class Solution:
    """
    二刷：双指针，j用来遍历数组，i用来记录当前存放的位置，如果nums[j]是不等于val的元素，则赋值到i处。
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        n = len(nums)
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i