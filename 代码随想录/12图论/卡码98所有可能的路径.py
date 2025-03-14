# https://kamacoder.com/problempage.php?pid=1170

# 最终版：邻接表，直接返回count
def main():
    # 读取数据
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        s, t = map(int, input().split())
        graph[s].append(t)
    # 解题
    count = dfs(1, graph, [], n)
    if count == 0:
        print(-1)


def dfs(u, graph, path, n):
    if u == n:
        print_path(path + [u])
        return 1
    count = 0
    for v in graph[u]:
        count += dfs(v, graph, path + [u], n)
    return count


def print_path(path):
    for i in range(len(path) - 1):
        print(path[i], end=" ")
    print(path[len(path) - 1])

# 邻接矩阵
def main2():
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i][j] = 1

    ans = []
    dfs2(graph, 1, [1], ans, n)
    if not ans:
        print(-1)
    for path in ans:
        for i in range(len(path) - 1):
            print(path[i], end=" ")
        print(path[-1])


def dfs2(graph, node, path, ans, n):
    if node == n:
        ans.append(path[:])
    for i in range(n + 1):
        if graph[node][i] == 1:
            dfs2(graph, i, path + [i], ans, n)


# 邻接表
from collections import defaultdict
def main1():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)

    ans = []
    dfs(graph, 1, [1], ans, n)
    if not ans:
        print(-1)
    for path in ans:
        for i in range(len(path) - 1):
            print(path[i], end=" ")
        print(path[-1])

def dfs1(graph, node, path, ans, n):
    if node == n:
        ans.append(path[:])
    for j in graph[node]:
        dfs(graph, j, path + [j], ans, n)


if __name__ == '__main__':
    main()

