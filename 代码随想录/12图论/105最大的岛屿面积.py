from typing import *
from collections import deque
# https://kamacoder.com/problempage.php?pid=1172


class Solution:
    """
    DFS：和200岛屿的数量一样，只是dfs函数要统计每个岛屿的面积。
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, visited):
            visited[i][j] = True
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            count = 0
            for dx, dy in directions:
                next_x, next_y = i + dx, j + dy
                if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    count += dfs(next_x, next_y, visited)
            return 1 + count  # 当前的位置(i, j)加上邻近的岛屿陆地位置


        m, n = len(grid), len(grid[0])
        ans = 0
        visited = [[False] * n for _ in range(m)]  # 所有dfs共享一个visited即可
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    ans = max(ans, dfs(i, j, visited))
        return ans

    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        """
        BFS版
        """
        def bfs(i, j, visited):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            count = 0
            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                x, y = q.popleft()  # 每次pop出一个计数加1
                count += 1
                for dx, dy in directions:
                    next_x, next_y = x + dx, y + dy
                    if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))
            return count

        m, n = len(grid), len(grid[0])
        ans = 0
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    ans = max(ans, bfs(i, j, visited))
        return ans




