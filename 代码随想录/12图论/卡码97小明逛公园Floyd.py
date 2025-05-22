# https://programmercarl.com/kamacoder/0097.%E5%B0%8F%E6%98%8E%E9%80%9B%E5%85%AC%E5%9B%AD.html
"""
Floyd-Warshall算法：多源最短路径，正负权重都可以（但不能有负权环）。核心思想是动态规划。
引入中间节点k，即递推公式：
    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
的含义为：ij的距离=min(当前ij的最短距离，经过一个中间节点k的距离)
"""
def floyd(n, d):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])  # 递推公式
    return d


def main():
    # 读取数据（初始化distance）
    n, m = map(int, input().split())
    d = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        # 双向道路
        d[u][v] = w
        d[v][u] = w
    q = int(input())
    plan = []
    for _ in range(q):
        plan.append(tuple(map(int, input().split())))
    # 解题
    d = floyd(n, d)
    # 打印结果
    for src, dest in plan:
        if d[src][dest] != float('inf'):
            print(d[src][dest])
        else:
            print(-1)


if __name__ == '__main__':
    main()




