from typing import *
from collections import deque
# https://programmercarl.com/kamacoder/0099.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%95%B0%E9%87%8F%E6%B7%B1%E6%90%9C.html
# https://programmercarl.com/kamacoder/0099.%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%95%B0%E9%87%8F%E5%B9%BF%E6%90%9C.html


class Solution:
    """
    DFS：遍历gird，遇到岛屿就调用DFS把当前岛屿能走的位置全部标记（即visited）这样每到一个岛屿计数器就加1，同时调用的dfs会把当前岛屿
    的所有陆地位置标记成visited，下次dfs就会从第二个岛屿开始
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j, visited):
            # 把当前岛屿遍历完，起始位置为grid[i][j]
            visited[i][j] = True
            for dx, dy in directions:
                next_x, next_y = i + dx, j + dy
                # 只遍历不越界且为岛屿的下一个位置
                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y] and grid[next_x][next_y] == "1":
                    dfs(grid, next_x, next_y, visited)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        ans = 0
        # 遍历grid，每遇到一个"1"，就调用dfs把当前岛屿上的所有位置搜完，这样下一次开始深搜就会从下一个岛屿开始
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    ans += 1
                    dfs(grid, i, j, visited)
        return ans

    """
    BFS版本：其他都一样，只是把dfs换成bfs。要注意的是加入q前就要标记visited，这样可以防止重复的加到q里出来再判断，可以节省时间！
    """
    def numIslands1(self, grid: List[List[str]]) -> int:
        def bfs(grid, i, j, visited):
            # 把当前岛屿遍历完，起始位置为grid[i][j]
            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    next_x, next_y = x + dx, y + dy
                    if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y] and grid[next_x][next_y] == "1":
                        visited[next_x][next_y] = True  # 加入前就判断是否到过
                        q.append((next_x, next_y))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        ans = 0
        # 遍历grid，每遇到一个"1"，就调用dfs把当前岛屿上的所有位置搜完，这样下一次开始深搜就会从下一个岛屿开始
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    ans += 1
                    bfs(grid, i, j, visited)
        return ans





if __name__ == '__main__':
    sol = Solution()
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(sol.numIslands(grid))