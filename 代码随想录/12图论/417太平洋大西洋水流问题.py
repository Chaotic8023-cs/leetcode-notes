from typing import *
from collections import deque
# https://programmercarl.com/kamacoder/0103.%E6%B0%B4%E6%B5%81%E9%97%AE%E9%A2%98.html


class Solution:
    """
    思路：最直接的做法就是在每个位置进行dfs搜索，看能不能到达两个海洋，这样会超时。所以我们反过来解决问题，我们从四个边出发，往
    中间找相等或更高的，用dfs标记能到达的位置，最后返回两边都标记过的即可。
    为什么每个大洋可以公用一个visited？因为只要有一条路径置能到，下一个位置即使也能通过此路径到达就不用再标记一次了！
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i, j, marker):
            visited[i][j] = True
            marker[i][j] = True  # 标记此位置能到
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                next_x, next_y = i + dx, j + dy
                curr_h = heights[i][j]
                # 我们反向找，所以要找高度相等或升高的，即heights[next_x][next_y] >= curr_h
                if 0 <= next_x < m and 0 <= next_y < n and heights[next_x][next_y] >= curr_h and not visited[next_x][next_y]:
                    dfs(next_x, next_y, marker)

        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]  # 用来标记能到太平洋的
        atlantic = [[False] * n for _ in range(m)]  # 用来标记能到大西洋的
        # 太平洋：左，上
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)
        # 大西洋：右，下
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            dfs(i, n - 1, atlantic)
        for j in range(n):
            visited = [[False] * n for _ in range(m)]
            dfs(m - 1, j, atlantic)
        # 返回两边都能到的位置
        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans


"""
BFS版
"""
class Solution1:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        # 两个大洋共用一个marker：初始化内层必须用for _ in range，因为如果是[[False, False]] * n的话每行的所有列都共享同一个列表！
        marker = [[[False, False] for _ in range(n)] for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(i, j, visited, ocean_id):
            visited[i][j] = True
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                marker[x][y][ocean_id] = True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and heights[nx][ny] >= heights[x][y]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

        visited = [[False] * n for _ in range(m)]
        # 太平洋
        for j in range(n):
            bfs(0, j, visited, 0)
        for i in range(m):
            bfs(i, 0, visited, 0)
        visited = [[False] * n for _ in range(m)]
        # 大西洋
        for j in range(n):
            bfs(m - 1, j, visited, 1)
        for i in range(m):
            bfs(i, n - 1, visited, 1)
        ans = []
        for i in range(m):
            for j in range(n):
                if marker[i][j][0] and marker[i][j][1]:
                    ans.append([i, j])
        return ans











