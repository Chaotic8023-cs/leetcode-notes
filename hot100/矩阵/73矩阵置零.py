from typing import *


class Solution:
    """
    O(m + n)额外空间解法：先遍历一遍记录要设成0的行和列，再遍历一遍设0即可
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = set(), set()  # 或者用两个boolean数组也行
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for r in row:
            for j in range(n):
                matrix[r][j] = 0
        for c in col:
            for i in range(m):
                matrix[i][c] = 0

    """
    O(1)额外空间解法：用矩阵的第一行和第一列记录要清零的列和行。当然，提前记录第一行和第一列是否要被清零，然后再用它们来记录。
    """
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        i0 = any(v == 0 for v in matrix[0])  # 第一行是否需要被清零
        j0 = any(matrix[i][0] == 0 for i in range(m))  # 第一列是否需要被清零
        # 遍历剩余的部分，并用第一行和第一列进行记录
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # 再遍历一次进行设0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 看看矩阵第一行是否要设0
        if i0:
            for j in range(n):
                matrix[0][j] = 0
        if j0:
            for i in range(m):
                matrix[i][0] = 0







