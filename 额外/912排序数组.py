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



# 归并排序（切片）
class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1, l2):
            m, n = len(l1), len(l2)
            ans = []
            i, j = 0, 0
            while i < m and j < n:
                if l1[i] < l2[j]:
                    ans.append(l1[i])
                    i += 1
                else:
                    ans.append(l2[j])
                    j += 1
            if i < m:
                ans.extend(l1[i:])
            elif j < n:
                ans.extend(l2[j:])
            return ans
        
        def mergesort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            l1_sorted = mergesort(nums[:mid])
            l2_sorted = mergesort(nums[mid:])
            return merge(l1_sorted, l2_sorted)

        return mergesort(nums)


# 归并排序（索引）
class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1, l2):  # 和切片版一致
            m, n = len(l1), len(l2)
            ans = []
            i, j = 0, 0
            while i < m and j < n:
                if l1[i] < l2[j]:
                    ans.append(l1[i])
                    i += 1
                else:
                    ans.append(l2[j])
                    j += 1
            if i < m:
                ans.extend(l1[i:])
            elif j < n:
                ans.extend(l2[j:])
            return ans

        # 索引版，性能好
        def mergesort(nums, left, right):  # [left, right) 左闭右开，同二分（都是闭区间的话不好处理）
            if right - left <= 1:  # 实际上只会是 == 1（只有一个元素），不会到出现 left == right的情况
                return nums[left:right]
            mid = (left + right) >> 1
            l1 = mergesort(nums, left, mid)
            l2 = mergesort(nums, mid, right)
            return merge(l1, l2)

        return mergesort(nums, 0, len(nums))