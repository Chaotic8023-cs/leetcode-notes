from typing import *


class Solution:
    """
    思路：双指针法，把不等于val的元素（j）放到数组前面（i）
    i：指向可以存放下一个不等于val的元素的位置
    j：用来遍历数组
    我们遍历数组，如果当前的元素nums[j]不是val，那我们把它直接放到i处，即数组前面
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i, j = 0, 0
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 2]
    val = 2
    print(sol.removeElement(nums, val))
    print(nums)


