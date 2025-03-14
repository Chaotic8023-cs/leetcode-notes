# 74
from typing import *

class Solution:
    """
    就是2D的binary search，我们把矩阵想象成一维的，start和end是矩阵的开头
    和末尾，每次求出的mid我们转换成2d坐标就行，
    即row = idx // num_elements, col = idx % num_elements

    eg:
    0 1 2 3
    4 5 6 7
    8 9 10 11

    上图为2d矩阵的1d index表示方法，mid为(0+11)//2 = 5,
    那么5的2d坐标为：row = 5 // 4 = 1, col = 5 % 5 = 1，即(1,1)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = (left + right) >> 1
            r, c = mid // n, mid % n
            if matrix[r][c] > target:
                right = mid
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                return True
        return False
        


        