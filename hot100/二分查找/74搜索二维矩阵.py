from typing import *


"""
只是普通二分加上了1d坐标转2d
"""
class Solution:
    """
    同找最左边的target
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = (left + right) >> 1
            r, c = mid // n, mid % n
            if target <= matrix[r][c]:
                right = mid
            else:
                left = mid + 1
        r, c = left // n, left % n
        return True if 0 <= left < m * n and matrix[r][c] == target else False

    """
    直接返回版
    """
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = (left + right) >> 1
            r, c = mid // n, mid % n  # 1d坐标转2d
            if matrix[r][c] == target:
                return True
            elif target < matrix[r][c]:
                right = mid
            else:
                left = mid + 1
        return False






