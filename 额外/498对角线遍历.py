from typing import *
from collections import deque


"""
层序遍历：
模拟太不好记了，所以用层序遍历。把矩阵当成graph做，起点是(0, 0)，然后做层序遍历，固定方向为[(0, 1), (1, 0)]，即我们得到的是
按右上到左下方向的层序遍历结果。
    例子：
        对于矩阵：
        1 2 3
        4 5 6
        7 8 9
        我们会得到: [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
因为题目是z字形的遍历，所以我们把结果中的偶数层进行reverse即可：[[1], [2, 4], [7, 5, 3], [6, 8], [9]]
最终把所有层展开即可return。

注意：这里visited必须是加入q前就要设为True，因为在加入下一层的节点时会存在重复，且这些节点还没有"真正的visited"！
"""
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        dirs = [(0, 1), (1, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        ans = []
        q = deque([(0, 0)])
        # 层序遍历
        while q:
            curr_level = []
            for _ in range(len(q)):
                x, y = q.popleft()
                curr_level.append(mat[x][y])
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True  # 提前visited
                        q.append((nx, ny))
            ans.append(curr_level)
        # 对结果中的偶数层进行反转
        for i in range(len(ans)):
            if i % 2 == 0:
                ans[i].reverse()
        # 最后flatten一下返回即可
        return [i for l in ans for i in l]


if __name__ == '__main__':
    sol = Solution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.findDiagonalOrder(mat))




