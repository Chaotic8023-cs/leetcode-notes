from typing import *
import random


"""
直接排序：快排
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def partition(nums, l, r):
            pivot_idx = random.randint(l, r)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            i = j = l
            while j < r:
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def quicksort(nums, l, r):
            if l < r:
                pivot_idx = partition(nums, l, r)
                quicksort(nums, l, pivot_idx - 1)
                quicksort(nums, pivot_idx + 1, r)

        quicksort(nums, 0, len(nums) - 1)


"""
三路快排：
i：指向当前0的区域的最右边位置（初始为-1，表示尚未找到0）
j：指向当前2的区域的最左边位置（初始为len(nums)，表示尚未找到2）
即排序完nums应当被分成了3个部分：0在[:i]，1在[i + 1, j - 1]，2在[j:]。
然后第三个指针k用来遍历数组，初始时k = 0。
循环条件：while k < j，即当前下标还在第三部分的左边，就需要继续
循环中：
    1. nums[k] == 0：则当前元素0应该放在当前0的右边界i的右边一位，即放在i + 1处，放好之后更新0的右边界i为i + 1，同时更新k为k + 1。
    2. nums[k] == 2：则当前元素2应该放在当前2的左边界的左边一位，即放在j - 1处，放好后更新2的左边界j为j - 1，不更新k，也就是说下标k还要再检查一次
    3. nums[k] == 1：遇到元素1不用动，因为它是中间的第二部分

为什么第一种情况需要更新 k，而第二种情况不需要？
当前元素为0时，交换后 nums[k] 必然是0，因为交换过来的i+1来自左边，所以一定是之前处理过的，就不需要检查了。
当前元素为2时，交换后 nums[k] 是来自k右边的还未遍历到的区域的元素，因此需要重新判断交换后的 nums[k] 是什么，所以不能移动 k。
"""
class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = -1, n
        k = 0
        while k < j:
            if nums[k] == 0:
                nums[k], nums[i + 1] = nums[i + 1], nums[k]
                i += 1
                k += 1
            elif nums[k] == 2:
                nums[k], nums[j - 1] = nums[j - 1], nums[k]
                j -= 1
            else:  # nums[k] == 1
                k += 1






