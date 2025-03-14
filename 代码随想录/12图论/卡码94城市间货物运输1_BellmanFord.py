# https://programmercarl.com/kamacoder/0094.%E5%9F%8E%E5%B8%82%E9%97%B4%E8%B4%A7%E7%89%A9%E8%BF%90%E8%BE%93I.html
"""
Bellman Ford：单源含负权重最短路径（但不允许存在负权重环，因为这样一直循环就可以无穷小）
算法核心：对所有边进行(n-1)次松弛，其中n为节点数
为什么进行(n-1)次松弛：对所有边松弛一次，相当于计算起点到达与起点一条边相连的节点的最短距离。起点到终点最多一共(n-1)条边，所以要进行(n-1)松弛。
"""

def bellman_ford(n, m, edges, start, goal):
    minDist = [float('inf')] * (n + 1)  # 记录目前从start到所有节点的最短距离
    minDist[start] = 0
    parent = [-1] * (n + 1)  # 记录所有节点的前驱节点，最后用来路径还原
    # 所有边松弛(n-1)次
    for _ in range(n - 1):
        updated = False
        for i, j, w in edges:
            # 如果目前能从起点到j（即目前i能到达：minDist[i] != float('inf')）且当前边可以松弛（当前到i的最短路径加上边ij比之前到j的距离更短，即边ij可以松弛）
            if minDist[i] != float('inf') and minDist[i] + w < minDist[j]:
                minDist[j] = minDist[i] + w
                updated = True
                parent[j] = i
        if not updated:  # 如果本轮没有更新，则说明所有的路径都为最短了，提前停止
            break

    if minDist[goal] != float('inf'):
        path = reconstruct_path(parent, start, goal)
        return minDist[goal], path
    else:
        return None, None


def reconstruct_path(parent, start, goal):  # bellman ford和dijkstra一样可以还原到任何节点的路径，需要注意的是不一样都能到，所以要检查起点是否为start
    curr = goal
    path = []
    while curr != -1:  # 这样就自动把start包含了，因为parent[start] = -1
        path.append(curr)
        curr = parent[curr]
    path = path[::-1]
    if path[0] == start:  # 有路径（有可能某些goal到不了，所以要检查）
        return path
    return None


def main():
    # 读取数据
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        i, j, w = map(int, input().split())
        edges.append((i, j, w))
    # 解题
    cost, path = bellman_ford(n, m, edges, 1, n)
    # 打印答案
    if cost is not None:
        print(cost)
        # print(path)
    else:
        print("unconnected")



if __name__ == '__main__':
    main()

