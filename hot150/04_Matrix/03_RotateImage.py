# 48
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        """
         一个n*n的matrix顺时针旋转了90°相当于,这个需要找规律得到
            matrix[i][j] -> matrix[j][n-i-1]
        如何in-place变换：
            1. 先上下翻转，即
                matrix[i][j] -> matrix[n-i-1][j]
            2. 再按主对角线翻转，即ij互换：
                matrix[n-i-1][j] -> matrix[j][n-i-1]
        """
        # 上下翻转: matrix[i][j] -> matrix[n-i-1][j]
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        # 主对角线对称翻转: matrix[n-i-1][j] -> matrix[j][n-i-1]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    sol.rotate(matrix)
    print(matrix)
