# https://programmercarl.com/kamacoder/0102.%E6%B2%89%E6%B2%A1%E5%AD%A4%E5%B2%9B.html
"""
思路：和孤岛的总面积相反，我们就先把挨着四周岛屿都变成2，然后再过一边普通的岛屿数量dfs，把遇到的所有岛屿都-1，
这样就鼓捣因为是1就会变成0，外围岛屿因为是2就会变成1.
"""

def dfs_increment(i, j, grid, visited, m, n):
    visited[i][j] = True
    grid[i][j] = 2
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        next_x, next_y = i + dx, j + dy
        if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
            dfs_increment(next_x, next_y, grid, visited, m, n)

def dfs(i, j, grid, visited, m, n):
    visited[i][j] = True
    grid[i][j] -= 1  # 都-1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        next_x, next_y = i + dx, j + dy
        if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
            dfs(next_x, next_y, grid, visited, m, n)

def main():
    # 读取数据
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().split())))
    # 先沿着外围走一遍把挨着外围的岛屿+1变成2
    visited = [[False] * n for _ in range(m)]
    for j in range(n):
        if grid[0][j] == 1:
            dfs_increment(0, j, grid, visited, m, n)
        if grid[m - 1][j] == 1:
            dfs_increment(m - 1, j, grid, visited, m, n)
    for i in range(m):
        if grid[i][0] == 1:
            dfs_increment(i, 0, grid, visited, m, n)
        if grid[i][n - 1] == 1:
            dfs_increment(i, n - 1, grid, visited, m, n)
    # 再按照经典岛屿数量问题把每个岛屿都-1，这样孤岛会变成0，挨着周围的岛会变成1（因为之气都改成2了）
    visited = [[False] * n for _ in range(m)]  # 重置visited，因为全部岛屿都要-1
    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0 and not visited[i][j]:  # 条件改成 > 0因为此时有1和2
                dfs(i, j, grid, visited, m, n)
    # 打印答案
    for i in range(m):
        for j in range(n - 1):  # 最后不能多一个空格，所以最后一个要单独打印
            print(grid[i][j], end=" ")
        print(grid[i][n - 1])


"""
思路2：优先看这个，同卡码101孤岛的总面积思路2
其实不用先把挨着外围的岛屿+1，这样最后普通dfs会把外围岛屿重复计算一次。
我们直接用一个统一的visited数组，先把外围岛屿标记visited，最后再遍历中心区域（没visited）的岛屿进行“沉没”即可。
"""


def main1():
    # 读取数据
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    # 解题
    visited = [[False] * m for _ in range(n)]
    # 先看四个边缘，把所有挨着边缘的孤岛进行visited标记
    for j in range(m):
        if not visited[0][j] and grid[0][j] == 1:
            dfs1(grid, 0, j, n, m, visited)
        if not visited[n - 1][j] and grid[n - 1][j] == 1:
            dfs1(grid, n - 1, j, n, m, visited)
    for i in range(n):
        if not visited[i][0] and grid[i][0] == 1:
            dfs1(grid, i, 0, n, m, visited)
        if not visited[i][m - 1] and grid[i][m - 1] == 1:
            dfs1(grid, i, m - 1, n, m, visited)
    # 再遍历中间部分孤岛，将其沉没
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if not visited[i][j] and grid[i][j] == 1:
                dfs1_rm(grid, i, j, n, m, visited)
    # 打印答案
    for i in range(n):
        for j in range(m - 1):
            print(grid[i][j], end=" ")
        print(grid[i][m - 1])


def dfs1(grid, i, j, n, m, visited):
    visited[i][j] = True
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in dirs:
        nx, ny = i + dx, j + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(grid, nx, ny, n, m, visited)


def dfs1_rm(grid, i, j, n, m, visited):
    visited[i][j] = True
    grid[i][j] = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in dirs:
        nx, ny = i + dx, j + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
            dfs1_rm(grid, nx, ny, n, m, visited)


if __name__ == '__main__':
    main()