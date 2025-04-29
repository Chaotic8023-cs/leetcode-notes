from typing import *


"""
硬模拟太麻烦，所以我们直接按顺序规定好4个方向，即右，下，左，上，然后就一直走，遇到超出边界或已经走过就改变方向即可

补充：如果起始位置改为右上角，且逆时针旋转，例如：
    1 2 3
    4 5 6 -> [3, 2, 1, 4, 7, 8, 9, 6, 5]
    7 8 9
则只需更改dirs和起始的(x, y)即可：
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x, y = 0, n - 1
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        visited = [[False] * n for _ in range(m)]
        x, y = 0, 0
        ans = []
        for _ in range(m * n):
            ans.append(matrix[x][y])
            visited[x][y] = True
            next_x, next_y = x + dirs[curr_dir][0], y + dirs[curr_dir][1]
            # 如果下一个位置越界或已经走过，那么就改变方向
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or visited[next_x][next_y]:
                curr_dir = (curr_dir + 1) % len(dirs)
                next_x, next_y = x + dirs[curr_dir][0], y + dirs[curr_dir][1]
            x, y = next_x, next_y
        return ans





