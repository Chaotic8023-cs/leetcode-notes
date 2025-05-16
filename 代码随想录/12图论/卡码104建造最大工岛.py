# https://kamacoder.com/problempage.php?pid=1176
"""
思路：暴力解法就是一个一个0试，但是每次都会进行多余的遍历。所以，我们进行一次遍历，把所有岛屿的面积存起来（每个岛屿用独立的marker进行标记，再
根据marker把面积存起来，用于后面的去重）。然后再看每个0的位置填起来根哪些岛屿接壤即可。检查每个0时只用看上下左右有没有marker，有的话加上对应岛屿的面积即可。
需要注意的是一个0的上下左右可能和同一个岛屿接壤多次，所以需要去重！
"""


def main():
    # 读取数据
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    # 解题
    visited = [[False] * m for _ in range(n)]
    marker_idx = 2
    area = {}
    # 先统计所有岛屿的面积，并把所有岛屿按顺序从2开始进行标记
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 1:
                area[marker_idx] = dfs(grid, i, j, visited, n, m, marker_idx)
                marker_idx += 1
    # 再遍历grid，看每个位置填海所构成的最大面积
    ans = max(area.values()) if len(area.values()) > 0 else 0  # 最大面积初始化为所有岛屿的最大面积（测试用例中有一个grid只有一个1，那么填海就不会进行，会返回0，所以ans应该初始化为未填海前最大的岛屿面积！）
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:  # 当前位置为水，能填海
                curr_area = 1
                islands = set()  # 用set去重：周围四个位置的岛屿可能存在重复
                for dx, dy in dirs:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > 1 and grid[nx][ny] not in islands:  # 四周这个位置是岛屿
                        curr_area += area[grid[nx][ny]]
                        islands.add(grid[nx][ny])
                ans = max(ans, curr_area)
    # 打印答案
    print(ans)


def dfs(grid, i, j, visited, n, m, marker_idx):
    visited[i][j] = True
    grid[i][j] = marker_idx
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    count = 0
    for dx, dy in dirs:
        nx, ny = i + dx, j + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
            count += dfs(grid, nx, ny, visited, n, m, marker_idx)
    return 1 + count


if __name__ == '__main__':
    main()


