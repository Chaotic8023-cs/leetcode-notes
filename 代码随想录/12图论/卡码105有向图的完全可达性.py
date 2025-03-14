# https://kamacoder.com/problempage.php?pid=1177
"""
DFS：从1进行dfs全部遍历一遍，然后看是不是所有节点都遍历到了。
"""


def main():
    # 读取数据
    n, k = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]  # 适应1-index
    for _ in range(k):
        i, j = map(int, input().split())
        graph[i][j] = 1
    # 解题
    def dfs(i, visited):
        visited.add(i)
        for j in range(n + 1):  # 注意：是1-indexed，所以要用n + 1！
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







