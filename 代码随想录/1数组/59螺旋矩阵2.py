from typing import *


"""
可以硬写4个for循环（见代码随想录），但条件太难想，还是记下面这个换方向的好

补充：如果起始位置改为右上角，且逆时针旋转，例如：
    3 2 1
    4 9 8
    5 6 7
则只需更改dirs和起始的(x, y)即可：
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x, y = 0, n - 1
"""
class Solution:
    """
    纯模拟：规定行走顺序的(dx, dy)，每次根据当前的方向走一步，并计算下一步的坐标，如果下一步的坐标越界或已经走过（填过了），则换方向
    """
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 行走顺序对应的(dx, dy)：右，下，左，上
        i, j, curr_dir = 0, 0, 0  # i，j为当前的坐标，curr_dir为当前的方向，即dirs中的
        # 每次根据当前的方向走一步，并更新下一步的位置
        for v in range(1, n * n + 1):
            ans[i][j] = v
            x, y = i + dirs[curr_dir][0], j + dirs[curr_dir][1]  # 根据当前的方向算下一步的坐标
            if x < 0 or x >= n or y < 0 or y >= n or ans[x][y]:  # 如果下一步的位置超出边界或已经走过了，则更新方向
                curr_dir = (curr_dir + 1) % len(dirs)
                x, y = i + dirs[curr_dir][0], j + dirs[curr_dir][1]
            i, j = x, y
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(3))
