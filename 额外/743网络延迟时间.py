from typing import *
from collections import *
import heapq




class Solution:
    """
    Dijkstra单源非负权重最短路径
    """
    def dijkstra(self, graph, start):
        pq = []
        heapq.heappush(pq, (start, 0, [start]))  # start, cost, path
        best_g = {start: 0}  # 有visited的作用，防止cycle
        while pq:
            curr, cost, path = heapq.heappop(pq)
            for node, w in graph[curr]:
                if node not in best_g or (cost + w) < best_g[node]:
                    best_g[node] = cost + w
                    heapq.heappush(pq, (node, cost + w, path + [node]))
        return best_g
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        best_g = self.dijkstra(graph, k)
        if all(i in best_g for i in range(1, n + 1)):  # 所有节点都有找到最短路径
            return max(best_g.values())  # 信号到达所有节点的时间即到达最远节点的时间
        else:
            return -1  # 有到达不了的节点：Dijkstra跑完有节点没有最短路径
        



