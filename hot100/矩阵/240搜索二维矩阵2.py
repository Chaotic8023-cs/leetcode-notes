from typing import *


"""
注意，此题和#74搜索二维矩阵相比不再是一直排序好的，本题matrix只是每一行和每一列是排序好的，而不是全局是排序好的，所以不能直接二分。
解法就是每行用一次二分即可。
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


"""
巧妙解法：由于每行每列都是排序好的，所以可以从右上角开始进行一个类似二分的线性搜索
从右上角 (0, n - 1) 开始搜索，对于当前位置 (i, j)：
        1. 若 matrix[i][j] 小于 target，说明该行值都比它小，可以排除这一行 → i += 1
        2. 若 matrix[i][j] 大于 target，说明该列值都比它大，可以排除这一列 → j -= 1
即i往下走，j往左走 -> 往i增加的方向、j减小的方向搜索，也就是说从右上往左下搜索     
"""
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1  # 从右上角开始
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:  # 排除当前行
                i += 1
            else:  # matrix[i][j] > target，排除当前列
                j -= 1
        return False





