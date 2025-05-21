from collections import defaultdict
# https://kamacoder.com/problempage.php?pid=1177
"""
DFS：从1进行dfs全部遍历一遍，然后看是不是所有节点都遍历到了。
"""

# 使用邻接表 + visited计数（比cnt计数方便一些）
def main():
    def dfs(curr, g, visited, n, k):
        visited.add(curr)
        cnt = 1
        for n in g[curr]:
            if n not in visited:
                cnt += dfs(n, g, visited, n, k)
        return cnt

    n, k = map(int, input().split())
    g = defaultdict(list)
    for _ in range(k):
        s, t = map(int, input().split())
        g[s].append(t)
    visited = set()
    cnt = dfs(1, g, visited, n, k)
    if len(visited) == n:
        print(1)
    else:
        print(-1)

# 使用邻接表 + cnt计数
def main1():
    def dfs(curr, g, visited, n, k):
        visited[curr] = True
        cnt = 1
        for n in g[curr]:
            if not visited[n]:
                cnt += dfs(n, g, visited, n, k)
        return cnt

    n, k = map(int, input().split())
    g = defaultdict(list)
    for _ in range(k):
        s, t = map(int, input().split())
        g[s].append(t)
    visited = [False] * (n + 1)
    cnt = dfs(1, g, visited, n, k)
    if cnt == n:
        print(1)
    else:
        print(-1)

"""
如果是下面这种写法：
    def dfs(curr, g, visited, n, k):
        cnt = 1
        for n in g[curr]:
            if not visited[n]:
                visited[n] = True
                cnt += dfs(n, g, visited, n, k)
                # visited[n] = False  # 不能回溯！
        return cnt

则：
    1. 不能回溯：因为我们每个节点不走第二次，这样cnt才是visit过的节点数！如果回溯了则可能一个节点visit多次（如果有多个路径穿过这个节点）
    2. 一开始一定要设置 visited[1] = True：节点1一开始的visited要设为True，因为dfs中只设了neighbor的visited！
"""

# 使用邻接矩阵 + visited计数
def main2():
    # 读取数据
    n, k = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]  # 适应1-index
    for _ in range(k):
        i, j = map(int, input().split())
        graph[i][j] = 1
    # 解题
    def dfs(i, visited):
        visited.add(i)
        for j in range(1, n + 1):  # 注意：节点从1开始！
            if graph[i][j] == 1 and j not in visited:
                dfs(j, visited)

    visited = set()
    dfs(1, visited)
    # 打印结果
    if len(visited) == n:  # 所有节点都遍历到了
        print(1)
    else:
        print(-1)


if __name__ == '__main__':
    main()







