# https://programmercarl.com/kamacoder/0047.%E5%8F%82%E4%BC%9Adijkstra%E6%9C%B4%E7%B4%A0.html
import heapq
from math import inf
"""
Dijkstra：单源非负权重最短路径
"""

"""
Dijkstra朴素版：和prim很像，其实能找到所有节点到原点的最短路径（路线）
    1. 找到当前距离start最小的节点curr
    2. 把当前节点curr加入路径
    3. 更新minDist
最后如果minDist[goal]不为无穷，则说明找到了最短路径。同时，minDist中的所有节点都记录了到它们的最短路径，通过parent数组同样能还原到
所有节点的最短路径。
"""
def dijkstra(n, m, graph, start, goal):
    minDist = [float('inf')] * (n + 1)  # 记录所有节点到原点的最近距离
    minDist[start] = 0
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    for _ in range(n):
        # 1. 找到当前距离start最小的节点curr
        curr = -1
        minCost = float('inf')
        for j in range(1, n + 1):
            if not visited[j] and minDist[j] < minCost:
                minCost = minDist[j]
                curr = j
        if curr == -1:  # 找不到能到达的节点了，提前结束
            break
        # 2. 把当前节点curr加入路径
        visited[curr] = True
        # 3. 更新minDist
        for v in range(1, n + 1):
            # 如果当前路经curr -> v（到curr的cost加上curr到v的cost）比之前v的minDist小，就更新minDist[v]
            if not visited[v] and graph[curr][v] < inf and minDist[curr] + graph[curr][v] < minDist[v]:
                minDist[v] = minDist[curr] + graph[curr][v]
                parent[v] = curr  # 记录parent以便复原路径

    # 此时minDist[goal]就是goal距离原点start的最小距离
    if minDist[goal] == float('inf'):
        return -1, None
    else:
        return minDist[goal], reconstruct_path(parent, start, goal)

def reconstruct_path(parent, start, goal):  # 通过parent数组从终点向起点出发重建路径，因为dijkstra计算了start到任何节点的最短距离，所以可以重建start到任何节点的最短路径
    curr = goal
    path = []
    while curr != -1:  # 这样就自动把start包含了，因为parent[start] = -1
        path.append(curr)
        curr = parent[curr]
    path = path[::-1]
    if path[0] == start:  # 有路径（有可能某些goal到不了，所以要检查）
        return path
    return None


"""
用堆（优先队列）的dijkstra：即aip课上学的
"""
def dijkstra_optimized(n, m, graph, start, goal):
    pq = []
    heapq.heappush(pq, (0, start, [start]))  # cost, start, path
    best_g = {}  # 和minDist一样，来记录start到各个节点目前的最短距离。同时作为closed list来使用，即充当了visited
    best_g[start] = 0
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return cost, path
        for v in range(1, n + 1):
            # 对于下一个节点j，在curr到j有连接的情况下：1. j没访问过 或 2. 当前路径的累计cost小于best_g[j]，即re-opening
            if graph[node][v] < inf and (v not in best_g or cost + graph[node][v] < best_g[v]):
                best_g[v] = cost + graph[node][v]
                heapq.heappush(pq, (cost + graph[node][v], v, path + [v]))
    return -1, None

"""
使用邻接表更好一些：
v, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
"""
def dijkstra_optimized_1(graph, v, e, start, goal):
    start_node = (0, start, [start])  # cost, curr_node, path
    pq = []
    heapq.heappush(pq, start_node)
    best_g = {start: 0}
    while pq:
        cost, curr, path = heapq.heappop(pq)
        if curr == goal:
            return cost, path
        for n, w in graph[curr]:
            if n not in best_g or cost + w < best_g[n]:
                best_g[n] = cost + w
                heapq.heappush(pq, (cost + w, n, path + [n]))
    return -1, None


def main():
    # 读取数据
    n, m = map(int, input().split())
    graph = [[inf] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        i, j, w = map(int, input().split())
        graph[i][j] = w  # 注意：graph是单向的!!!
    # 解题
    cost, path = dijkstra(n, m, graph, 1, n)
    # 打印结果
    print(cost)
    # print(path)


if __name__ == '__main__':
    main()


