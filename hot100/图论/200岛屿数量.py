from typing import *


"""
dfs：每遇到一个陆地，就调用dfs把这片陆地全标记为0，然后ans += 1
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j, grid):
            grid[i][j] = '0'
            visited[i][j] = True
            for dx, dy in dirs:
                next_i, next_j = i + dx, j + dy
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == '1' and not visited[next_i][next_j]:
                    dfs(next_i, next_j, grid)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # 每遇到一个陆地，就调用dfs把这片陆地全标记为0
                    dfs(i, j, grid)
                    ans += 1
        return ans





