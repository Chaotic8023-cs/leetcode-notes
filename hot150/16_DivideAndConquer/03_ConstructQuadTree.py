# 427
from typing import *


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        dfs中我们先看当前的grid是否时leaf，即看是否都是0或1，如果是则return一个leaf
        否则我们递归子区域
        """
        def dfs(rowStart, colStart, rowEnd, colEnd):  # 参数记录当前subgrid的row和col的start和end的index
            # 看是否有0和1
            zero, one = 0, 0
            for i in range(rowStart, rowEnd+1):
                for j in range(colStart, colEnd+1):
                    if grid[i][j] == 1:
                        one = 1
                    else:
                        zero = 1
            isLeaf = zero + one == 1  # 如果都是0或1则当前的subgrid是leaf
            if isLeaf:
                return Node(grid[rowStart][colStart], True)
            # 如果不是leaf则递归四个子区域
            topLeft = dfs(rowStart, colStart, (rowStart+rowEnd)//2, (colStart+colEnd)//2)
            topRight = dfs(rowStart, (colStart+colEnd)//2+1, (rowStart+rowEnd)//2, colEnd)
            bottomLeft = dfs((rowStart+rowEnd)//2+1, colStart, rowEnd, (colStart+colEnd)//2)
            bottomRight = dfs((rowStart+rowEnd)//2+1, (colStart+colEnd)//2+1, rowEnd, colEnd)
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(0, 0, len(grid)-1, len(grid)-1)

        