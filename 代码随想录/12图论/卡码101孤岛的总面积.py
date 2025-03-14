# https://kamacoder.com/problempage.php?pid=1173
"""
思路：先沿着外围走一遍把挨着外围的岛屿变成水，再用常规的计算岛屿面积计算剩下的岛屿（即不与周围接壤的岛屿）
"""

def dfs_make_water(i, j, grid, visited, m, n):
    visited[i][j] = True
    grid[i][j] = 0  # 变成水
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    for dx, dy in directions:
        next_x, next_y = i + dx, j + dy
        if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
            count += dfs_make_water(next_x, next_y, grid, visited, m, n)
    return 1 + count

def dfs(i, j, grid, visited, m, n):
    visited[i][j] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    for dx, dy in directions:
        next_x, next_y = i + dx, j + dy
        if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
            count += dfs(next_x, next_y, grid, visited, m, n)
    return 1 + count

def main():
    # 读取数据
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().split())))
    # 先沿着外围走一遍把挨着外围的岛屿变成水
    visited = [[False] * n for _ in range(m)]
    for j in range(n):
        if grid[0][j] == 1:
            dfs_make_water(0, j, grid, visited, m, n)
        if grid[m - 1][j] == 1:
            dfs_make_water(m - 1, j, grid, visited, m, n)
    for i in range(m):
        if grid[i][0] == 1:
            dfs_make_water(i, 0, grid, visited, m, n)
        if grid[i][n - 1] == 1:
            dfs_make_water(i, n - 1, grid, visited, m, n)
    # 再按照经典岛屿面积求剩下的岛屿的面积总和（剩下的岛屿即不挨外围的待遇）
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                ans += dfs(i, j, grid, visited, m, n)
    # 打印答案
    print(ans)


"""
思路2：优先看这个
先把四个边上的每个1的位置进行dfs，即我们把所有跟边接壤的岛屿进行visited标记。然后就可以遍历中间部分，把所有剩下的孤岛（没visited）的面积
统计出来。所以就是只需要全局共享一个visited就可以，不需要直接变成水。
"""


def main1():
    # 读取数据
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    # 解题
    visited = [[False] * m for _ in range(n)]
    # 所有边上的位置进行dfs，把挨着边的岛屿都标记visited
    for j in range(m):
        if not visited[0][j] and grid[0][j] == 1:
            dfs1(grid, 0, j, visited, n, m)
        if not visited[n - 1][j] and grid[n - 1][j] == 1:
            dfs1(grid, n - 1, j, visited, n, m)
    for i in range(n):
        if not visited[i][0] and grid[i][0] == 1:
            dfs1(grid, i, 0, visited, n, m)
        if not visited[i][m - 1] and grid[i][m - 1] == 1:
            dfs1(grid, i, m - 1, visited, n, m)
    # 再统计孤岛的面积
    ans = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if not visited[i][j] and grid[i][j] == 1:
                ans += dfs1(grid, i, j, visited, n, m)
    # 打印答案
    print(ans)


def dfs1(grid, i, j, visited, n, m):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited[i][j] = True
    count = 0
    for dx, dy in dirs:
        nx, ny = i + dx, j + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
            count += dfs1(grid, nx, ny, visited, n, m)
    return 1 + count


if __name__ == '__main__':
    main()