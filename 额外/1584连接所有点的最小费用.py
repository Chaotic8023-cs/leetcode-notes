from typing import *

class DisjointSet:
    def __init__(self, size):
        self.parent = [-1] * size

    def find(self, a):
        if self.parent[a] < 0:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        self.parent[pb] = pa
        return True


"""
最小生成树模版题：直接统计edges，然后 并查集 + Kruskal 即可
"""
class Solution:
    def kruskal(self, edges, v):
        ds = DisjointSet(v)
        ans = 0
        cnt = 0
        for v1, v2, w in sorted(edges, key=lambda x: x[2]):
            if ds.union(v1, v2):
                ans += w
                cnt += 1
                if cnt == v - 1:  # 优化：MST中加入 v-1 条边时MST构建完成，提前结束，不用遍历完edges
                    break
        return ans

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        v = len(points)
        edges = []
        for i in range(v):
            for j in range(i + 1, v):
                x1, y1 = points[i]
                x2, y2 = points[j]
                w = abs(x1 - x2) + abs(y1 - y2)
                edges.append((i, j, w))
        return self.kruskal(edges, v)




