# https://programmercarl.com/kamacoder/0095.%E5%9F%8E%E5%B8%82%E9%97%B4%E8%B4%A7%E7%89%A9%E8%BF%90%E8%BE%93II.html
"""
有负权重环的最短路径：在普通Bellman Ford中我们做n-1次循环，既然有环，所以多做一次循环后minDist还会减小（因为负权重环一直走会无穷小）就可以
用来判断有没有环
"""

def bellman_ford(n, m, edges, start, goal):
    minDist = [float('inf')] * (n + 1)  # 记录目前到所有节点的最短距离
    minDist[start] = 0
    parent = [-1] * (n + 1)  # 记录所有节点的前驱节点，最后用来路径还原
    # 所有边松弛n次，第n次看minDist是否还减小
    for loop in range(n):
        updated = False
        for i, j, w in edges:
            # 如果目前能从起点到j（即目前i能到达：minDist[i] != float('inf')）且当前边可以松弛（当前到i的最短路径加上边ij比之前到j的距离更短，即边ij可以松弛）
            if minDist[i] != float('inf') and minDist[i] + w < minDist[j]:
                minDist[j] = minDist[i] + w
                updated = True
                parent[j] = i
        if not updated:  # 如果本轮没有更新，则说明所有的路径都为最短了，提前停止
            break
        if loop == n - 1 and updated:  # 第n次循环后还减小，则证明有负权重环
            return "circle", None

    if minDist[goal] != float('inf'):
        path = reconstruct_path(parent, start, goal)
        return minDist[goal], path
    else:
        return "unconnected", None


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
    print(cost)
    # print(path)



if __name__ == '__main__':
    main()

