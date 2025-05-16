from typing import *
# https://programmercarl.com/kamacoder/0106.%E5%B2%9B%E5%B1%BF%E7%9A%84%E5%91%A8%E9%95%BF.html


class Solution:
    """
    不用DFS或BFS的岛屿题：此题只有一个岛屿，所以不用DFS寻找，直接遍历grid即可。我们看每个格子的四周，如果是水或者边界则给周长贡献一条边。
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        next_x, next_y = i + dx, j + dy
                        # 检查陆地格子的四周：if 旁边是水 or 旁边是边界（越界了） 则周长+1（为什么越界也算：想象grid全是1，那么周长就是全越界的地方！）
                        if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or grid[next_x][next_y] == 0:  # 越界 or 0
                            ans += 1
        return ans







