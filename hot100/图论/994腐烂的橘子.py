from collections import deque
from typing import *


"""
BFS：模拟过程，因为所有的腐烂橘子同时传染周围的新鲜橘子，所以不能像岛屿面积一样一个一个进行搜索。我们一开始先遍历一次grid，
往q里加入所有腐烂的橘子，同时统计新鲜橘子的个数。然后进行BFS，这里每一轮BFS要确保当前所有的腐烂橘子都往外扩散一格，所以用
的是“层序遍历”的思想，每轮开始前q中有多少腐烂橘子我们这轮就扩散几次。最后如果新鲜橘子全部被传染了，就返回轮数（ans）即可。
注意，因为往q里加的都是腐烂橘子，所以我们不需要把新鲜橘子标记为腐烂橘子（1变成2）！

为什么不光while q还要一个while fresh > 0?
加入到q中时是本轮传染开始前，所以只有还剩新鲜橘子时，本轮传染才能开始且算作1分钟！最后一轮传染时，把剩下的新鲜橘子都传染了，同时这些被传染的橘子都被加入到q中。
但之后到while q时再没有剩余的新鲜橘子了，但q中加入的是刚才被传染的最后的那些新鲜橘子，也就是q中还有东西，但最后这个循环就不能算，所以要加一个fresh > 0的条件
来保证计数正确！
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(grid, rotted, fresh, visited):
            q = deque(rotted)
            ans = 0
            while q and fresh > 0:  # 目前有腐烂的橘子，且还剩下新鲜橘子时，本轮传染开始。每轮四周扩散一格，相当于过了1分钟
                ans += 1
                for _ in range(len(q)):  # “层序遍历”：确保每一轮中所有腐烂的橘子都往外扩散一格
                    x, y = q.popleft()
                    for dx, dy in dirs:
                        next_x, next_y = x + dx, y + dy
                        if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True  # 加入q前就标记visited，节省时间
                            fresh -= 1
                            q.append((next_x, next_y))
            return ans if fresh == 0 else -1

        # 统计新鲜橘子个数，并收集所有腐烂橘子
        fresh = 0
        rotted = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotted.append((i, j))
                    visited[i][j] = True
        # 进行BFS
        return bfs(grid, rotted, fresh, visited)





if __name__ == '__main__':
    sol = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(sol.orangesRotting(grid))





