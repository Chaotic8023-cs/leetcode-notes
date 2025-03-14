from typing import *
import random


# 能过力扣测试的快排：专门处理数组里数全相等的情况
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(l, r):
            pivot_idx = random.randint(l, r)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            i = l
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[r], nums[i] = nums[i], nums[r]
            return i

        def quicksort(l, r):
            if l < r:
                pivot_idx = partition(l, r)
                """
                应对所有数都一样的那个测试样例：
                把要继续partition的左右区间[l, pivot_idx-1]和[pivot_idx+1,r]继续缩小
                只要pivot左右两侧的数和pivot相等，就可以分别往对应方向缩!
                """
                lr, rl = pivot_idx - 1, pivot_idx + 1
                while lr >= 0 and nums[lr] == nums[lr] + 1:
                    lr -= 1
                while rl < len(nums) and nums[rl] == nums[rl - 1]:
                    rl += 1
                quicksort(l, lr)
                quicksort(rl, r)

        quicksort(0, len(nums) - 1)
        return nums


