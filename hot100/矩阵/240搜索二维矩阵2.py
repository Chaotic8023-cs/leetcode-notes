from typing import *


"""
注意，此题和#74搜索二维矩阵相比不再是一直排序好的，本题matrix只是每一行和每一列是排序好的，而不是全局是排序好的，所以不能直接二分。
解法就是每行用一次二分即可。更高级的方法就不记了。
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) >> 1
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            return -1
        for i, nums in enumerate(matrix):
            if bs(nums, target) != -1:
                return True
        return False



