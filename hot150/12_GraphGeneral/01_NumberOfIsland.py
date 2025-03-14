# 200
from typing import *


class Solution:
    # self try
    def numIslands1(self, grid: List[List[str]]) -> int:
        """
        把grid看作一个graph，其实岛屿的数量就是链接在一起的component的数量
        即我们用一个visited来记录访问过的位置（节点），然后遇到1就跑一遍dfs，即
        找到和当前的1有链接的所有节点，并将他们都记录到visited里面。于是，每个dfs就
        相当于找到一个island，我们最后返回dfs的次数即可
        """
        visited = set()  # 其实还有种方法(下面那个方法)就是直接把visited过的1设为0，这样就不需要visited了，因为只用看是1的地方!
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])

        """
        因为不像下面直接变0，我们需要用visited来去重！
        因为如果grid是
        [1, 1
         1, 1]
        那么dfs的时候第一个1的右边是1，右边的1的左边是原来的1，就会无穷recursion！
        """
        def dfs(i, j, visited):
            # 确保当前的ij，即dfs一定被调用在1上，确保和这个1链接的所有1都被找到并算到visited里
            if (i, j) not in visited:
                visited.add((i, j))
                for dx, dy in dxy:
                    if 0 <= i + dx < m and 0 <= j + dy < n:
                        if grid[i + dx][j + dy] == "0":  # neighbour是0则不继续dfs，仅标记visited
                            visited.add((i+dx, j+dy))
                            continue
                        dfs(i + dx, j + dy, visited)  # neighbour是1时说明有链接，则继续dfs

        ans = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if grid[i][j] == "0":
                        visited.add((i, j))
                    else:  # 仅在grid[i][j]为1时调用dfs
                        dfs(i, j, visited)
                        ans += 1
        return ans

    # 不用visited，而是把遇到的1变成0，这样只用看有1的地方就行，大大提升了效率
    def numIslands(self, grid: List[List[str]]) -> int:
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # dfs只run在是1的位置
            grid[i][j] = "0"  # 直接设为0，相当于visited了
            for dx, dy in dxy:
                if 0 <= i + dx < m and 0 <= j + dy < n and grid[i + dx][j + dy] == "1":
                    dfs(i + dx, j + dy)  # neighbour是1时说明有链接，则继续dfs
        ans = 0
        for i in range(m):
            for j in range(n):
                # visited的变成0了，相当于只用看是1的地方
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        return ans


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    sol = Solution()
    print(sol.numIslands(grid))
