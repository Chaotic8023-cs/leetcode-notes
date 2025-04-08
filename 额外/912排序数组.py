from typing import *
import random


# 能过力扣测试的快排：专门处理数组里数全相等的情况
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(left, right):
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            i = left
            for j in range(left, right):
                if nums[j] < pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
                j += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i

        def quick_sort(left, right):
            if left < right:
                pidx = partition(left, right)
                """
                应对所有数都一样的那个测试样例：
                把要继续partition的左右区间[l, pivot_idx-1]和[pivot_idx+1,r]继续缩小
                只要pivot左右两侧的数和pivot相等，就可以分别往对应方向缩!
                """
                l, r = pidx - 1, pidx + 1
                while l >= 0 and nums[l] == nums[l + 1]:
                    l -= 1
                while r < len(nums) and nums[r] == nums[r - 1]:
                    r += 1
                quick_sort(left, l)
                quick_sort(r, right)

        quick_sort(0, len(nums) - 1)
        return nums


