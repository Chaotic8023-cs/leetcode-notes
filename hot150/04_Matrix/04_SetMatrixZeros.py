# 73
from typing import *
from utils.pprintdp import pprintdp


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeroRows = set()
        zeroCols = set()
        """
        用两个set分别记录要清零的行和列，第一次遍历记录，第二次遍历清零即可
        """
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)
        for i in range(m):
            for j in range(n):
                if i in zeroRows or j in zeroCols:
                    matrix[i][j] = 0

    # O(1) space
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        i0 = any(v == 0 for v in matrix[0])
        j0 = any(matrix[j][0] == 0 for j in range(m))
        """
        我们用matrix的第一行和第一列来直接记录需要清零的行和列，
        但是问题是如果记录了会覆盖掉原来的在row1和col1的数字，如果原来
        就有0的话我们就不知道到底该不该也把row1和col1清零。所以我们一开始
        就先看第一行和第一列有没有0，有的话就记True，之后我们就可以遍历内部的
        矩阵，若matrix[i][j]==0则直接记录到matrix[i][0]（第一列）和
        matrix[0][j]（第一行）中。然后再遍历一次内部矩阵来根据第一行和第一列的0来清零。
        最后如果一开始第一行和第一列有0，则再把第一行和第一列全清零即可。
        """
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if i0:
            for j in range(n):
                matrix[0][j] = 0
        if j0:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    sol = Solution()
    sol.setZeroes(matrix)
    print(matrix)

