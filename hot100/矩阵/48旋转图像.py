from typing import *


"""
原：
[[1,2,3],
 [4,5,6],
 [7,8,9]
]

matrix[::-1]：
[[7,8,9],
 [4,5,6],
 [1,2,3]
]

zip(*matrix[::-1])：
zip([7,8,9],[4,5,6],[1,2,3]) = [7,4,1] [8,5,2] [9,6,3]
"""
class Solution:
    # 右旋
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = zip(*matrix[::-1])

    # 左旋：同理，只是顺序变成先zip原来的matrix然后倒排
    def rotate_left(self, matrix):
        matrix[:] = zip(*matrix)[::-1]





